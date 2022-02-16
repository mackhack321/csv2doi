import { useState } from "react";

function downloadAsFile(data) {
  const element = document.createElement("a");
  const file = new Blob([data], { type: "text/xml" });
  element.href = URL.createObjectURL(file);
  element.download = "output.xml";
  document.body.appendChild(element);
  element.click();
}

export default function Dataset() {
  const [batchID, setBatchID] = useState("");
  const [depname, setDepname] = useState("");
  const [depemail, setDepemail] = useState("");
  const [registrant, setRegistrant] = useState("");
  const [dbname, setDbname] = useState("");
  const [uploadedFile, setUploadedFile] = useState();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const fileUpload = new FormData();
    fileUpload.append("file", uploadedFile);

    let uploadRes = await fetch("http://localhost:5003/upload", {
      method: "POST",
      mode: "cors",
      body: fileUpload,
    });

    let uploadJson = await uploadRes.json();

    let metadataRes = await fetch("http://localhost:5003/dataset", {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        batchid: batchID,
        depname: depname,
        depemail: depemail,
        registrant: registrant,
        dbname: dbname,
        fileID: uploadJson.fileID,
      }),
    });

    let json = await metadataRes.json();

    downloadAsFile(json.response);
  };

  const changeHandler = (event) => {
    setUploadedFile(event.target.files[0]);
  };

  return (
    <div className="App">
      <div>
        <div className="bg-white w-screen px-4 bg-gray-100">
          <div className="mt-5 md:mt-0 md:col-span-2">
            <form onSubmit={handleSubmit}>
              <div className="shadow sm:rounded-md sm:overflow-hidden">
                <div className="px-4 py-5 bg-white space-y-6 sm:p-6">
                  <div className="grid grid-cols-3 gap-6">
                    <div className="col-span-3 sm:col-span-2">
                      <label className="block text-sm font-medium text-gray-700">
                        DOI Batch ID
                      </label>
                      <div className="mt-1 flex rounded-md shadow-sm">
                        <input
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
                          type="text"
                          value={depname}
                          placeholder="Bluto Blutarsky"
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
                          type="text"
                          value={depemail}
                          placeholder="bblutarsky@faber.edu"
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
                          type="text"
                          value={registrant}
                          placeholder="Faber College"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                          onChange={(e) => setRegistrant(e.target.value)}
                        />
                      </div>
                    </div>
                  </div>
                  <div className="grid grid-cols-3 gap-6">
                    <div className="col-span-3 sm:col-span-2">
                      <label className="block text-sm font-medium text-gray-700">
                        Database Name
                      </label>
                      <div className="mt-1 flex rounded-md shadow-sm">
                        <input
                          type="text"
                          value={dbname}
                          placeholder="Faber Institutional Respository"
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                          onChange={(e) => setDbname(e.target.value)}
                        />
                      </div>
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      File Upload
                    </label>
                    <div className="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
                      <div className="space-y-1 text-center">
                        <div className="flex text-sm text-gray-600">
                          <label
                            htmlFor="file-upload"
                            className="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
                          >
                            <span>Upload a file</span>
                            <input
                              id="file-upload"
                              name="file-upload"
                              type="file"
                              accept=".csv"
                              className="sr-only"
                              onChange={changeHandler}
                            />
                          </label>
                          <p className="pl-1">or drag and drop</p>
                        </div>
                        <p className="text-xs text-gray-500">CSV Files Only</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="px-4 py-3 bg-white text-right sm:px-6">
                  <button
                    type="submit"
                    className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Convert to XML
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      {/* start old form */}
      {/* <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={batchID}
          placeholder="Batch ID"
          onChange={(e) => setBatchID(e.target.value)}
        />
        <input
          type="text"
          value={depname}
          placeholder="Depositor Name"
          onChange={(e) => setDepname(e.target.value)}
        />
        <input
          type="text"
          value={depemail}
          placeholder="Depositor Email"
          onChange={(e) => setDepemail(e.target.value)}
        />
        <input
          type="text"
          value={registrant}
          placeholder="Registrant"
          onChange={(e) => setRegistrant(e.target.value)}
        />
        <input
          type="text"
          value={dbname}
          placeholder="Database Name"
          onChange={(e) => setDbname(e.target.value)}
        />

        <button type="submit">Greet me</button>

        <p>{response}</p>
      </form> */}
    </div>
  );
}

// batchID = request.json["batchid"]
// depname = request.json["depname"]
// depemail = request.json["depemail"]
// registrant = request.json["registrant"]
// dbname = request.json["dbname"]
