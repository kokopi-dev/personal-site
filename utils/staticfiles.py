#!/usr/bin/env python3
from pathlib import Path

def init_static():
    static = Path("static")
    if not static.is_dir():
        static.mkdir(parents=True, exist_ok=True)
