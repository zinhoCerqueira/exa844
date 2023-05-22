/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    fontFamily: {
      roboto:['Roboto', 'sans-serif'],
      pacifico:['Pacifico', 'cursive'],
      Lato:['Lato', 'sans-serif'],
      Berkshire: ['Berkshire Swash', 'cursive'] 
    },
    extend: {
      colors:{
        primary: '#FF5F5D',
        secondary: '#F8F8FF',
        tertiary: '#D4145A',
        quaternary: '#FBB03B',
        quinary: '#FFB7B9',
      }
    },
  },
  plugins: [],
}

