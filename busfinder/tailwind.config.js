/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    fontFamily: {
      roboto:['Roboto', 'sans-serif'],
    },
    extend: {
      colors:{
        primary: '#FF5F5D',
        secondary: '#3F7C85',
        tertiary: '#00CCBF',
        quaternary: '#72F2EB',
        quinary: '#747E7E',
      }
    },
  },
  plugins: [],
}

