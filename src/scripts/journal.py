import datetime  # to get the current time because crossref wants a timestamp
import csv  # to read the input data into a form the program can use
from os import remove  # to delete the input csv file when done
import io # for StringIO, reading csv data from a string
from shared import cleanString

def makeTimestamp():  # crossref wants YYYYMMDDhhmmss
    now = datetime.datetime.now()
    time = ""
    time += str(now.year)
    time += '{:02d}'.format(now.month)
    time += '{:02d}'.format(now.day)
    time += '{:02d}'.format(now.hour)
    time += '{:02d}'.format(now.minute)
    time += '{:02d}'.format(now.second)
    return time

def makeAuthors(row):
    authors = ""
    totalAuthorsPosition = 1

    while True:
        if f"firstname{totalAuthorsPosition}" not in row.keys() or not row[f'firstname{totalAuthorsPosition}']: break # stop if we run out of authors
        if totalAuthorsPosition == 1:
            authors += "          <person_name contributor_role=\"author\" sequence=\"first\">\n"
        else:
            authors += "          <person_name contributor_role=\"author\" sequence=\"additional\">\n"
        authors += f"            <given_name>{row[f'firstname{totalAuthorsPosition}']}</given_name>\n"
        authors += f"            <surname>{row[f'lastname{totalAuthorsPosition}']}</surname>\n"
        authors += "            <affiliations>\n"

        authors += "              <institution>\n"

        authors += f"                <institution_name>{row[f'instName{totalAuthorsPosition}']}</institution_name>\n"
        authors += f"                <institution_department>{row[f'instDept{totalAuthorsPosition}']}</institution_department>\n"

        authors += "              </institution>\n"

        authors += "            </affiliations>\n"
        if row[f'orcid{totalAuthorsPosition}']:
            authors += f"            <ORCID authenticated=\"true\">{row[f'orcid{totalAuthorsPosition}']}</ORCID>\n"
        authors += "          </person_name>\n"

        totalAuthorsPosition += 1
    
    return authors


def makeHead(batchID, depname, depemail, registrant):
    head = ""

    head += f"""    <doi_batch_id>{batchID}</doi_batch_id>
    <timestamp>{makeTimestamp()}</timestamp>\n"""

    head += f"""    <depositor>
      <depositor_name>{depname}</depositor_name>
      <email_address>{depemail}</email_address>
    </depositor>\n"""

    head += f"    <registrant>{registrant}</registrant>\n"

    return head

def makeCitations(row):
    cites = ""

    # handle unstructured citations
    unstructCitePosition = 1
    while True:
        if f"unstructCitation{unstructCitePosition}" not in row.keys() or not row[f"unstructCitation{unstructCitePosition}"]: break # stop if we run out of unstructured citations
        
        cites += f"        <citation key=\"ref{unstructCitePosition}\">\n"
        if row[f'unstructDOI{unstructCitePosition}']:
            cites += f"          <doi>{row[f'unstructDOI{unstructCitePosition}']}</doi>\n"
        cites += f"          <unstructured_citation>{row[f'unstructCitation{unstructCitePosition}']}</unstructured_citation>\n"
        cites += "        </citation>\n"
        unstructCitePosition += 1

    return cites

def makeBody(rows):
    numDone = 0
    numEntries = len(rows)
    print(f"Generating XML for {numEntries} entries...")

    body = ""
    for row in rows:
        body += "    <journal>\n"

        body += "      <journal_metadata language=\"en\" reference_distribution_opts=\"any\">\n"

        body += f"        <full_title>{row['fullTitle']}</full_title>\n"
        body += f"        <abbrev_title>{row['abbrevTitle']}</abbrev_title>\n"
        body += f"        <issn media_type=\"electronic\">{row['issn']}</issn>\n"

        body += "        <doi_data>\n"
        body += f"        <doi>{row['journalDOI']}</doi>\n"
        body += f"        <resource>{row['journalResource']}</resource>\n"
        body += "        </doi_data>\n"

        body += "      </journal_metadata>\n"

        body += "      <journal_article language=\"en\" publication_type=\"full_text\" reference_distribution_opts=\"any\">\n"

        body += "        <titles>\n"
        body += f"          <title>{row['articleTitle']}</title>\n"
        body += "        </titles>\n"

        body += "        <contributors>\n"
        body += makeAuthors(row)
        body += "        </contributors>\n"

        body += "        <jats:abstract>\n"
        body += f"          <jats:p xml:lang=\"en\">{row['abstract']}</jats:p>\n"
        body += "        </jats:abstract>\n"

        body += "        <publication_date media_type=\"online\">\n"
        body += f"          <month>{'{:02d}'.format(int(row['publicationDate'].split('/')[0]))}</month>\n"
        body += f"          <day>{'{:02d}'.format(int(row['publicationDate'].split('/')[1]))}</day>\n"
        body += f"          <year>{row['publicationDate'].split('/')[2]}</year>\n"
        body += "        </publication_date>\n"

        body += "        <acceptance_date media_type=\"online\">\n"
        body += f"          <month>{'{:02d}'.format(int(row['acceptanceDate'].split('/')[0]))}</month>\n"
        body += f"          <day>{'{:02d}'.format(int(row['acceptanceDate'].split('/')[1]))}</day>\n"
        body += f"          <year>{row['acceptanceDate'].split('/')[2]}</year>\n"
        body += "        </acceptance_date>\n"

        body += "        <publisher_item>\n"
        body += f"        <item_number item_number_type=\"article_number\">{row['itemNumber']}</item_number>\n"
        body += "        </publisher_item>\n"

        body += "        <crossmark>\n"
        body += f"          <crossmark_version>{row['crossmarkVersion']}</crossmark_version>\n"
        body += f"          <crossmark_policy>{row['crossmarkPolicy']}</crossmark_policy>\n"
        body += "          <custom_metadata>"

        body += f"            <assertion name=\"received\" label=\"Received\" group_name=\"publication_history\" group_label=\"Publication History\" order=\"0\">{row['crossmarkReceivedDate']}</assertion>\n"
        body += f"            <assertion name=\"accepted\" label=\"Accepted\" group_name=\"publication_history\" group_label=\"Publication History\" order=\"1\">{row['crossmarkAcceptedDate']}</assertion>\n"

        body += "            <fr:program name=\"fundref\">\n"
        body += "              <fr:assertion name=\"fundgroup\">\n"
        body += f"                <fr:assertion name=\"funder_name\">{row['funderName']}\n"
        body += f"                  <fr:assertion name=\"funder_identifier\">{row['funderIdentifier']}</fr:assertion>\n"
        body += "                </fr:assertion>\n"

        body += f"                <fr:assertion name=\"award_number\">{row['awardNumber']}</fr:assertion>\n"

        body += "              </fr:assertion>\n"
        body += "            </fr:program>\n"

        body += "            <program xmlns=\"http://www.crossref.org/AccessIndicators.xsd\">\n"
        body += "              <free_to_read/>\n"
        body += "              <license_ref applies_to=\"vor\" start_date=\"2008-08-13\">http://creativecommons.org/licenses/by/3.0/deed.en_US</license_ref>\n"
        body += "            </program>\n"

        body += "          </custom_metadata>"
        body += "        </crossmark>\n"

        body += "        <doi_data>\n"
        body += f"          <doi>{row['articleDOI']}</doi>\n"
        body += f"          <resource content_version=\"vor\" mime_type=\"text/html\">{row['articleResource']}</resource>\n"
        body += "        </doi_data>\n"

        body += "        <citation_list>\n"
        body += makeCitations(row)
        body += "        </citation_list>\n"

        body += "      </journal_article>\n"

        body += "    </journal>\n"

        numDone += 1

        print(f"  Finished processing entry {numDone} out of {numEntries}")

    return body


def rowsToXML(rows, batchID, depname, depemail, registrant):
    xml = ""
    xml += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += """<doi_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.crossref.org/schema/5.3.0 https://www.crossref.org/schemas/crossref5.3.0.xsd"
    xmlns="http://www.crossref.org/schema/5.3.0" xmlns:jats="http://www.ncbi.nlm.nih.gov/JATS1"  xmlns:fr="http://www.crossref.org/fundref.xsd" xmlns:mml="http://www.w3.org/1998/Math/MathML" version="5.3.0">\n"""

    xml += "  <head>\n"
    xml += makeHead(batchID, depname, depemail, registrant)
    xml += "  </head>\n"

    xml += "  <body>\n"
    xml += makeBody(rows)
    xml += "  </body>\n"

    xml += "</doi_batch>"

    print("Successfully generated XML\n")

    return xml


# def writeXMLToFile(xml):
#     print(f"Writing generated XML to {XML_FILENAME}...")
#     with open(XML_FILENAME, 'w') as file:
#         file.write(xml)
#         file.close()
#     print(f"Successfully wrote XML to {XML_FILENAME}")

def go(batchID, depname, depemail, registrant, fileID):
    rows = []
    with open(f"temp/{fileID}", 'r', encoding="utf-8-sig") as file:
        cleanedContent = cleanString(file.read())
        reader = csv.DictReader(io.StringIO(cleanedContent))
        for row in reader:
            rows.append(row)
        file.close()

    remove(f"temp/{fileID}")

    xml = rowsToXML(rows, batchID, depname, depemail, registrant)
    # writeXMLToFile(xml)

    return xml
