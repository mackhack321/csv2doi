import { Link } from "@reach/router";
import React from "react";
// import logo from "./horz_maroon.svg";
import logo from "./csv2doi.png";

export default function Navbar() {
  return (
    <div>
      <div className="inline-flex">
        <img src={logo} alt="logo" className="h-24" />
        <div className="flex space-x-4 px-5 py-9 text-xl">
          <Link to="/">
            <button
              className="text-maroon rounded-md font-medium hover:text-msublue"
              type="button"
            >
              Home
            </button>
          </Link>
          <Link to="help">
            <button
              className="text-maroon rounded-md font-medium hover:text-msublue"
              type="button"
            >
              Help
            </button>
          </Link>
        </div>
      </div>
      <div className="bg-maroon h-1"></div>
    </div>
  );
}
