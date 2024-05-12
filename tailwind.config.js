/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./static/**/*.{js,html}",
    "./templates/**/*.html",
    "./utils/styles/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        "brand": {
          "primary": "#DAD4CA",
          "secondary": "#BFABCE",
          "base-100": "#1A1A1A",
          "base-200": "#292929",
        }
      }
    },
  },
  plugins: [],
}

