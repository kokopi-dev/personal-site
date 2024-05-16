/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: [
    "./static/**/*.{js,html}",
    "./templates/**/*.html",
    "./utils/styles/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        "c": {
          "primary": "#DAD4CA",
          "secondary": "#BFABCE",
          "base-100": "#1A1A1A",
          "base-200": "#292929",
          "primary-li": "#424242",
          "secondary-li": "#915C9E",
          "base-100-li": "#EEEEEE",
          "base-200-li": "#DCDCDC",
        }
      },
      animation: {
        "pulse-fast-short": "pulse 0.8s ease-in-out infinite"
      }
    },
  },
  plugins: [],
}

