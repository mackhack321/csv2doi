import React, { useState } from "react";
import {
  makeDissertationHeaders,
  makeDatasetHeaders,
  makeRefUpdateHeaders,
  makeJournalHeaders,
} from "../utils/Templates";

export default function Help() {
  const [numCitations, setNumCitations] = useState(1);
  const [numAuthors, setNumAuthors] = useState(1);

  function downloadTemplate(data, name) {
    const element = document.createElement("a");
    const file = new Blob([data], { type: "text/csv;charset=UTF-8" });
    element.href = URL.createObjectURL(file);
    element.download = `${name}.csv`;
    document.body.appendChild(element);
    element.click();
  }

  return (
    <div className="w-screen px-4 py-5 bg-gray-100">
      <div className="rounded-md px-4 py-3 bg-white">
        <div className="text-4xl pb-4 text-maroon font-bold text-center">
          How to Use CSV2DOI
        </div>
        <div className="pb-4 space-y-2">
          <p className="text-2xl">Creating your Spreadsheet</p>
          {/* <p className="pb-2">
            CSV2DOI requires a CSV file to read data from. This is equivalent to
            a spreadsheet and can be created using Microsoft Excel or any other
            spreadsheet editor. However, the file must be saved as a .CSV file
            rather than the traditional .XLSX file. To do this in Excel, follow
            these instructions:
          </p>
          <p>
            Click the File button near the top left corner. Then, in the side
            bar, select Save As. After that, select Browse under Other
            Locations. After navigating to where you want to save the file, open
            the "Save as type" dropdown. Find and select "CSV (Comma delimited)
            (*csv)." Finally, click Save. The file you have just saved is the
            file you will upload into CSV2DOI.
          </p> */}
          <p>
            Download a blank CSV file for your data type using the buttons below
            and fill with your data.
          </p>
          <div className="flex space-x-5">
            <div>
              <p>Enter the number of citations</p>
              <input
                type="number"
                placeholder="1"
                onChange={(e) => setNumCitations(parseInt(e.target.value))}
              />
            </div>
            <div>
              <p>Enter the number of authors (Journal datatype)</p>
              <input
                type="number"
                placeholder="1"
                onChange={(e) => setNumAuthors(parseInt(e.target.value))}
              />
            </div>
          </div>
          <div className="space-x-3">
            <button
              className="bg-msugreen text-white rounded-md p-3"
              onClick={() =>
                downloadTemplate(
                  makeDissertationHeaders(numCitations),
                  "dissertation"
                )
              }
            >
              Download dissertation template
            </button>
            <button
              className="bg-msugreen text-white rounded-md p-3"
              onClick={() => downloadTemplate(makeDatasetHeaders(), "dataset")}
            >
              Download dataset template
            </button>
            <button
              className="bg-msugreen text-white rounded-md p-3"
              onClick={() =>
                downloadTemplate(
                  makeRefUpdateHeaders(numCitations),
                  "refUpdate"
                )
              }
            >
              Download reference update template
            </button>
            <button
              className="bg-msugreen text-white rounded-md p-3"
              onClick={() =>
                downloadTemplate(
                  makeJournalHeaders(numCitations, numAuthors),
                  "journal"
                )
              }
            >
              Download journal template
            </button>
          </div>
        </div>
        <div className="space-y-2">
          <p className="text-2xl">
            A note on using multiple citations and authors
          </p>
          <p>
            In the data type templates, you will find that some columns have a
            suffix of 1 (e.g. firstname1, unstructCitation1 for first author's
            first name and first unstructured citation, respectively). This is
            to enable the use of multiple authors or citations. To add more than
            one of these fields, simply insert the columns you need and give
            them the same header just with an incremented suffix. For example,
            to add another author, one would insert the columns firstname2,
            lastname2, and orcid2 and fill in the data. Take care to not skip a
            number, as this will lead to unexpected results.
          </p>
        </div>
      </div>
    </div>
  );
}
