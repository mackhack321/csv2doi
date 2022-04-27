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

function makeJournalHeaders(numCitations, numAuthors) {
  if (!numCitations) numCitations = 1; // check for NaN
  if (!numAuthors) numAuthors = 1; // check for NaN
  console.log(numAuthors);
  let journalHeaders = "";
  for (let i = 1; i <= numAuthors; i++) {
    journalHeaders += `firstname${i},lastname${i},instName${i},orcid${i},`;
  }
  journalHeaders +=
    "fullTitle,abbrevTitle,issn,journalDOI,journalResource,articleTitle,abstract,publicationDate,acceptanceDate,itemNumber,crossmarkVersion,crossmarkPolicy,crossmarkReceivedDate,crossmarkAcceptedDate,funderName,funderIdentifier,awardNumber,articleDOI,articleResource,";
  for (let i = 1; i <= numCitations; i++) {
    journalHeaders += `unstructCitation${i},unstructDOI${i},`;
  }
  return journalHeaders;
}

export {
  makeDissertationHeaders,
  makeDatasetHeaders,
  makeRefUpdateHeaders,
  makeJournalHeaders,
};
