import React from "react";

export default function Alert(props) {
  return (
    <div className="animate-pulse bg-red-500 rounded-md w-fit px-2 py-4 text-white font-medium">
      <div className="flex flex-inline">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-12 w-12"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
            clip-rule="evenodd"
          />
        </svg>
        <div className="px-3">
          <p>There was a problem executing your request:</p>
          <p>{props.message}</p>
        </div>
      </div>
    </div>
  );
}
