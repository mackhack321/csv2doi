module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        maroon: "#5D1725",
        msublue: "#007FA3",
        msugreen: "#198754",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
