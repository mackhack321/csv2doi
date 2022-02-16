import React, { useState } from "react";
import Dataset from "./Dataset";
import Dissertation from "./Dissertation";

export default function Radio() {
  const [radio, setRadio] = useState("dataset");
  return (
    <div className="">
      <form className="flex flex-col py-8 px-6 text-xl">
        <label className="block font-medium text-gray-700">
          Select Datatype
        </label>
        <div className="justify-center">
          {/* <h1>Radio value is : {radio}</h1> */}
          <input
            type="radio"
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
