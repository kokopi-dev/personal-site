#!/bin/bash
cd ..
set -e

if [ ! -d "/tmp/firefox-dev" ]; then
    echo "Creating firefox profile"
    mkdir -p /tmp/firefox-dev
    firefox -CreateProfile "dev-profile /tmp/firefox-dev"
    cat >> /tmp/firefox-dev/prefs.js << EOF
user_pref("browser.download.dir", "~/downloads");
user_pref("browser.download.folderList", 2);
EOF
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# PID file to track processes
PIDFILE=".dev.pids"

cleanup() {
    echo -e "\n${YELLOW}🛑 Shutting down development servers...${NC}"

    if [ -f "$PIDFILE" ]; then
        while read -r pid name; do
            if kill -0 "$pid" 2>/dev/null; then
                echo -e "${BLUE}   Stopping $name (PID: $pid)${NC}"
                kill "$pid" 2>/dev/null || true
            fi
        done <"$PIDFILE"
        rm -f "$PIDFILE"
    fi

    echo -e "\n${YELLLOW}Killing dev-profile browser"
    pkill -f "dev-profile"

    echo -e "${GREEN}✅ All processes stopped${NC}"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM EXIT

# Clear any existing PID file
rm -f "$PIDFILE"

echo -e "${GREEN}🚀 Starting development environment...${NC}"

# Start Templ watcher
# echo -e "${BLUE}📝 Starting Templ watcher...${NC}"
# templ generate --watch &
# TEMPL_PID=$!
# echo "$TEMPL_PID templ" >>"$PIDFILE"

# Wait a moment for templ to start
sleep 2

# Start Air for Go hot reloading
echo -e "${BLUE}🔥 Starting Air (Go hot reload)...${NC}"
air &
AIR_PID=$!
echo "$AIR_PID air" >>"$PIDFILE"

echo -e "${GREEN}✅ Development environment ready!${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop all services${NC}"

# wait for gin to start
sleep 2
firefox -P dev-profile -private-window http://localhost:3500 &

# Wait for Air process (main process)
wait $AIR_PID

