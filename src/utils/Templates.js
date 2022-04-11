function dissertationHeaders(numCitations) {
  if (!numCitations) numCitations = 1;
  let dissertationHeaders =
    "firstname1,lastname1,orcid1,institutionDept,title,approval date,institution,degree,doi,resource,";
  for (let i = 1; i <= numCitations; i++) {
    dissertationHeaders += `unstructCitation${i},unstructDOI${i},`;
  }
  return dissertationHeaders;
}

function datasetHeaders() {
  return "firstname1,lastname1,orcid1,institutionDept,title,creation date month,creation date day,creation date year,publication date month,publication date day,publication date year,item number,description,doi,resource";
}

export { dissertationHeaders, datasetHeaders };
