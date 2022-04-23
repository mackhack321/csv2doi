import React, { useState } from "react";
import Dataset from "./Dataset";
import Dissertation from "./Dissertation";
import RefUpdate from "./RefUpdate";
import Journal from "./Journal";

export default function Radio() {
  const [radio, setRadio] = useState("dissertation");
  return (
    <div className="py-4 rounded-md">
      <form className="flex flex-col py-8 px-6 text-xl ">
        <label className="block font-medium text-gray-700 pb-2">
          Select Datatype:
        </label>

<<<<<<< HEAD
        <select
          className="w-fit rounded-md shadow-sm"
          onChange={(e) => setRadio(e.target.value)}
        >
          <option value="dissertation">Dissertation</option>
          <option value="dataset">Dataset</option>
          <option value="journal">Journal</option>
          <option value="refUpdate">Reference Update</option>
        </select>
=======
        <div className="justify-center ">
          {/* <h1>Radio value is : {radio}</h1> */}
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
          <br />
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
            checked={radio === "journal"}
            value="journal"
            onChange={(e) => {
              setRadio(e.target.value);
            }}
          />
          <label className="pl-2 font-medium text-gray-700">Journal</label>
          <br />
          <input
            className="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
            type="radio"
            checked={radio === "refUpdate"}
            value="refUpdate"
            onChange={(e) => {
              setRadio(e.target.value);
            }}
          />
          <label className="pl-2 font-medium text-gray-700">
            Reference Update
          </label>
        </div>
>>>>>>> origin/main
      </form>
      {radio === "dataset" && <Dataset />}
      {radio === "dissertation" && <Dissertation />}
      {radio === "journal" && <Journal />}
      {radio === "refUpdate" && <RefUpdate />}
      {radio === "journal" && <Journal />}
    </div>
  );
}
