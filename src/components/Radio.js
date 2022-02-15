import React, { useState } from "react";
import Dataset from "./Dataset";
import Dissertation from "./Dissertation";

export default function Radio() {
  const [radio, setRadio] = useState("dataset");
  return (
    <div className="">
      <form className="flex flex-col py-8 px-6 text-xl">
        <div className="justify-center">
          {/* <h1>Radio value is : {radio}</h1> */}
          <input
            type="radio"
            className=""
            checked={radio === "dataset"}
            value="dataset"
            onChange={(e) => {
              setRadio(e.target.value);
            }}
          />
          <label className="pl-2">Dataset</label>
          <br />
          <input
            type="radio"
            checked={radio === "dissertation"}
            value="dissertation"
            onChange={(e) => {
              setRadio(e.target.value);
            }}
          />
          <label className="pl-2">Dissertation</label>
        </div>
      </form>
      {radio === "dataset" && <Dataset />}
      {radio === "dissertation" && <Dissertation />}
    </div>
  );
}
