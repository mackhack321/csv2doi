import datetime  # to get the current time because crossref wants a timestamp
import csv  # to read the input data into a form the program can use
from os import remove  # to delete the input csv file when done
import io # for StringIO, reading csv data from a string
from shared import cleanString, MSU_ROR
# CSV_FILENAME = "dissertation.csv"  # csv dataset to use
# XML_FILENAME = "dissertation.xml"  # where to store the generated XML

# # information used in making the head
# DOI_BATCH_ID = "my_doi_batch"
# DEPOSITOR_NAME = "Mack Stanley"
# DEPOSITOR_EMAIL = "jms2099@msstate.edu"
# REGISTRANT = "Mississippi State University"

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
        body += "    <dissertation publication_type=\"full_text\" language=\"en\">\n"

        body += "      <contributors>\n"
        
        body += makeAuthors(row)

        body += "      </contributors>\n"

        body += "      <titles>\n"
        body += f"        <title>{row['title']}</title>\n"
        body += "      </titles>\n"

        body += "      <approval_date>\n"
        body += f"        <month>{'{:02d}'.format(int(row['approval date'].split('/')[0]))}</month>\n"
        body += f"        <day>{'{:02d}'.format(int(row['approval date'].split('/')[1]))}</day>\n"
        body += f"        <year>{row['approval date'].split('/')[2]}</year>\n"
        body += "      </approval_date>\n"

        body += f"      <institution>\n"
        body += f"        <institution_id type=\"ror\">{MSU_ROR}</institution_id>\n"
        body += f"        <institution_department>{row[f'institutionDept']}</institution_department>\n"
        body += f"      </institution>\n"

        body += f"      <degree>{row['degree']}</degree>\n"

        body += "      <doi_data>\n"
        body += f"        <doi>{row['doi']}</doi>\n"
        body += f"        <resource>{row['resource']}</resource>\n"
        body += "      </doi_data>\n"

        body += "      <citation_list>\n"
        
        body += makeCitations(row)

        body += "      </citation_list>\n"
            

        body += "    </dissertation>\n"

        numDone += 1

        print(f"  Finished processing entry {numDone} out of {numEntries}")

    return body


def rowsToXML(rows, batchID, depname, depemail, registrant):
    xml = ""
    xml += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += """<doi_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.crossref.org/schema/5.3.0 https://www.crossref.org/schemas/crossref5.3.0.xsd"
    xmlns="http://www.crossref.org/schema/5.3.0" version="5.3.0">\n"""

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
