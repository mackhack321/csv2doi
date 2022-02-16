import React, { useState } from "react";
import Dataset from "./Dataset";
import Dissertation from "./Dissertation";

export default function Radio() {
  const [radio, setRadio] = useState("dataset");
  return (
    <div className="py-4 rounded-md">
      <form className="flex flex-col py-8 px-6 text-xl ">
        <label className="block font-medium text-gray-700 pb-2">
          Select Datatype:
        </label>

        <div className="justify-center ">
          {/* <h1>Radio value is : {radio}</h1> */}
          <input
            className="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
            type="radio"
            checked={radio === "dataset"}
            value="dataset"
            onChange={(e) => {
              setRadio(e.target.value);
            }}
          />
          <label className="pl-2 font-medium text-gray-700">Dataset</label>
          <br />
          <input
            className="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
            type="radio"
            checked={radio === "dissertation"}
            value="dissertation"
            onChange={(e) => {
              setRadio(e.target.value);
            }}
          />
          <label className="pl-2 font-medium text-gray-700">Dissertation</label>
        </div>
      </form>
      {radio === "dataset" && <Dataset />}
      {radio === "dissertation" && <Dissertation />}
    </div>
  );
}
