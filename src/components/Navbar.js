import { Link } from "@reach/router";
import React from "react";
// import logo from "./horz_maroon.svg";
import logo from "./csv2doi.png";

export default function Navbar() {
  return (
    <div>
      <img src={logo} alt="logo" className="h-24" />
      <div className="flex space-x-4 px-5 pb-3">
        <Link to="/">
          <button
            className="px-3 py-2 bg-msugreen text-white rounded-md font-medium hover:bg-green-800"
            type="button"
          >
            Home
          </button>
        </Link>

        <Link to="about">
          <button
            className="px-3 py-2 bg-msugreen text-white rounded-md font-medium hover:bg-green-800"
            type="button"
          >
            About
          </button>
        </Link>
      </div>
      <div className="bg-maroon h-1"></div>
    </div>
  );
}
