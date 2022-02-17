import React from "react";

export default function Alert(props) {
  return (
    <div className="animate-pulse bg-red-500 rounded-md w-fit px-2 py-4 text-white font-medium">
      <p>There was a problem executing your request:</p>
      <p>{props.message}</p>
    </div>
  );
}
