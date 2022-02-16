import React from "react";
// import logo from "./horz_maroon.svg";
import logo from "./csv2doi.png";

export default function Navbar() {
  return (
    <div>
      <img src={logo} alt="logo" className="h-24" />
      <div className="bg-maroon h-1"></div>
    </div>
  );
}
