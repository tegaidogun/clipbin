module.exports = {
  contents: [
    "./templates/**/*.html",
    "./static/**/*.js",
    "./**/*.py",  // if you're using Jinja in .py
  ],
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
