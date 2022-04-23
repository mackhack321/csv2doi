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

        <select
          className="w-fit rounded-md shadow-sm"
          onChange={(e) => setRadio(e.target.value)}
        >
          <option value="dissertation">Dissertation</option>
          <option value="dataset">Dataset</option>
          <option value="journal">Journal</option>
          <option value="refUpdate">Reference Update</option>
        </select>
      </form>
      {radio === "dataset" && <Dataset />}
      {radio === "dissertation" && <Dissertation />}
      {radio === "refUpdate" && <RefUpdate />}
      {radio === "journal" && <Journal />}
    </div>
  );
}
