import { useState } from "react";
import Alert from "./Alert";
import LoadingSpinner from "./LoadingSpinner";

function downloadAsFile(data) {
  const element = document.createElement("a");
  const file = new Blob([data], { type: "text/xml" });
  element.href = URL.createObjectURL(file);
  element.download = "output.xml";
  document.body.appendChild(element);
  element.click();
}

export default function Dissertation() {
  const [batchID, setBatchID] = useState("");
  const [depname, setDepname] = useState("");
  const [depemail, setDepemail] = useState("");
  const [registrant, setRegistrant] = useState("");
  const [uploadedFile, setUploadedFile] = useState();
  const [fileIsUploaded, setFileIsUploaded] = useState(false);
  const [errorHappened, setErrorHappened] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [fetchInProgress, setFetchInProgress] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setErrorHappened(false);

    const fileUpload = new FormData();
    fileUpload.append("file", uploadedFile);

    let uploadRes;
    let metadataRes;

    setFetchInProgress(true);

    try {
      uploadRes = await fetch("http://130.18.123.77:443/upload", {
        method: "POST",
        mode: "cors",
        body: fileUpload,
      });
    } catch (error) {
      setErrorMessage("Error during file upload");
      setErrorHappened(true);
      setFetchInProgress(false);
    }

    let uploadJson = await uploadRes.json();

    try {
      metadataRes = await fetch("http://130.18.123.77:443/dissertation", {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          batchid: batchID,
          depname: depname,
          depemail: depemail,
          registrant: registrant,
          fileID: uploadJson.fileID,
        }),
      });
    } catch (error) {
      setErrorMessage("Error during conversion");
      setErrorHappened(true);
      setFetchInProgress(false);
    }

    let xmlJson = await metadataRes.json();

    if (xmlJson.response === "bad headers") {
      setErrorMessage(
        "The headers in your CSV file do not match the expected values"
      );
      setErrorHappened(true);
      setFetchInProgress(false);
    } else {
      downloadAsFile(xmlJson.response);
      setFetchInProgress(false);
    }

    setFileIsUploaded(false);
  };

  const changeHandler = (event) => {
    setUploadedFile(event.target.files[0]);
    setFileIsUploaded(true);
  };

  return (
    <div className="App">
      <div>
        <div className="bg-gray-100 w-full px-4">
          <div className="mt-5 md:mt-0 md:col-span-2">
            <form onSubmit={handleSubmit}>
              <div className="shadow sm:rounded-md sm:overflow-hidden">
                <div className="px-4 py-5 bg-white space-y-6 sm:p-6">
                  {errorHappened && <Alert message={errorMessage} />}
                  <div className="grid grid-cols-3 gap-6">
                    <div className="col-span-3 sm:col-span-2">
                      <label className="block text-sm font-medium text-gray-700">
                        DOI Batch ID
                      </label>
                      <div className="mt-1 flex rounded-md shadow-sm">
                        <input
                          required
                          minLength={4}
                          maxLength={100}
                          type="text"
                          value={batchID}
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                          placeholder="my_batch_id"
                          onChange={(e) => setBatchID(e.target.value)}
                        />
                      </div>
                    </div>
                  </div>
                  <div className="grid grid-cols-3 gap-6">
                    <div className="col-span-3 sm:col-span-2">
                      <label className="block text-sm font-medium text-gray-700">
                        Depositor Name
                      </label>
                      <div className="mt-1 flex rounded-md shadow-sm">
                        <input
                          required
                          type="text"
                          value={depname}
                          placeholder="John Smith"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                          onChange={(e) => setDepname(e.target.value)}
                        />
                      </div>
                    </div>
                  </div>
                  <div className="grid grid-cols-3 gap-6">
                    <div className="col-span-3 sm:col-span-2">
                      <label className="block text-sm font-medium text-gray-700">
                        Depositor Email
                      </label>
                      <div className="mt-1 flex rounded-md shadow-sm">
                        <input
                          required
                          type="email"
                          value={depemail}
                          placeholder="someone@msstate.edu"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                          onChange={(e) => setDepemail(e.target.value)}
                        />
                      </div>
                    </div>
                  </div>
                  <div className="grid grid-cols-3 gap-6">
                    <div className="col-span-3 sm:col-span-2">
                      <label className="block text-sm font-medium text-gray-700">
                        Registrant
                      </label>
                      <div className="mt-1 flex rounded-md shadow-sm">
                        <input
                          required
                          type="text"
                          value={registrant}
                          placeholder="Mississippi State University"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                          onChange={(e) => setRegistrant(e.target.value)}
                        />
                      </div>
                    </div>
                  </div>

                  {!fileIsUploaded ? (
                    <>
                      <div>
                        <label className="block text-sm font-medium text-gray-700">
                          File Upload
                        </label>
                        <div>
                          <label
                            htmlFor="file-upload"
                            className="relative cursor-pointer rounded-md font-medium text-white"
                          >
                            <div className="mt-1 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                              <span className="text-lg">Upload a CSV file</span>
                              <input
                                required
                                id="file-upload"
                                name="file-upload"
                                type="file"
                                accept=".csv"
                                className="sr-only"
                                onChange={changeHandler}
                              />
                            </div>
                          </label>
                        </div>
                      </div>
                    </>
                  ) : (
                    <>
                      <p>File uploaded: {uploadedFile.name}</p>
                      <button
                        className="px-3 py-2 bg-red-500 text-white rounded-md font-medium hover:bg-red-700"
                        type="button"
                        onClick={() => setFileIsUploaded(false)}
                      >
                        Change File
                      </button>
                    </>
                  )}
                </div>
                <div className="bg-gray-200 h-0.5" />
                <div className="px-4 py-3 bg-white sm:px-6 rounded-md">
                  <button
                    type="submit"
                    className="text-lg inline-flex justify-center py-2 px-4 border border-transparent shadow-sm  font-medium rounded-md text-white bg-msugreen hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                    disabled={fetchInProgress}
                  >
                    {fetchInProgress ? (
                      <LoadingSpinner />
                    ) : (
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-7 w-7 pr-2"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fillRule="evenodd"
                          d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
                          clipRule="evenodd"
                        />
                      </svg>
                    )}
                    Convert to XML
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
