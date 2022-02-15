module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        maroon: "#5D1725",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
