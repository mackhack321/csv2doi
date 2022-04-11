function makeDissertationHeaders(numCitations) {
  if (!numCitations) numCitations = 1; // check for NaN
  let dissertationHeaders =
    "firstname1,lastname1,orcid1,institutionDept,title,approval date,institution,degree,doi,resource,";
  for (let i = 1; i <= numCitations; i++) {
    dissertationHeaders += `unstructCitation${i},unstructDOI${i},`;
  }
  return dissertationHeaders;
}

function makeDatasetHeaders() {
  return "firstname1,lastname1,orcid1,institutionDept,title,creation date month,creation date day,creation date year,publication date month,publication date day,publication date year,item number,description,doi,resource";
}

function makeRefUpdateHeaders(numCitations) {
  if (!numCitations) numCitations = 1; // check for NaN
  let refUpdateHeaders = "doi,";
  for (let i = 1; i <= numCitations; i++) {
    refUpdateHeaders += `unstructCitation${i},unstructDOI${i},`;
  }
  return refUpdateHeaders;
}

export { makeDissertationHeaders, makeDatasetHeaders, makeRefUpdateHeaders };
