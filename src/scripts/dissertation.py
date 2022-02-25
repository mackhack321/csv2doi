import datetime  # to get the current time because crossref wants a timestamp
import csv  # to read the input data into a form the program can use
from os import remove  # to delete the input csv file when done
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


def makeBody(rows):
    numDone = 0
    numEntries = len(rows)
    print(f"Generating XML for {numEntries} entries...")

    body = ""
    for row in rows:
        body += "    <dissertation publication_type=\"full_text\" language=\"en\">\n"

        body += "      <contributors>\n"
        body += "        <person_name contributor_role=\"author\" sequence=\"first\">\n"
        body += f"          <given_name>{row['firstname']}</given_name>\n"
        body += f"          <surname>{row['lastname']}</surname>\n"
        body += f"          <affiliation>{row['affiliation']}</affiliation>\n"
        body += f"          <ORCID authenticated=\"true\">{row['orcid']}</ORCID>\n"
        body += "        </person_name>\n"
        body += "      </contributors>\n"

        body += "      <titles>\n"
        body += f"        <title>{row['title']}</title>\n"
        body += "      </titles>\n"

        body += "      <approval_date>\n"
        body += f"        <month>{'{:02d}'.format(int(row['approval date'].split('/')[0]))}</month>\n"
        body += f"        <day>{'{:02d}'.format(int(row['approval date'].split('/')[1]))}</day>\n"
        body += f"        <year>{row['approval date'].split('/')[2]}</year>\n"
        body += "      </approval_date>\n"

        body += "      <institution>\n"
        body += f"        <institution_name>{row['institution']}</institution_name>\n"
        body += "      </institution>\n"

        body += f"      <degree>{row['degree']}</degree>\n"

        body += "      <doi_data>\n"
        body += f"        <doi>{row['doi']}</doi>\n"
        body += f"        <resource>{row['resource']}</resource>\n"
        body += "      </doi_data>\n"

        body += "      <citation_list>\n"
        citationIndex = 0
        
        for unstructCitation in row['unstructCitation'].split(', '):
            # print(f"found unstruct citation: {unstructCitation}")
            body += f"        <citation key=\"ref{citationIndex + 1}\">\n"
            body += f"          <doi>{row['citationDOI'].split(', ')[citationIndex]}</doi>\n"
            body += f"          <unstructured_citation>{unstructCitation}</unstructured_citation>\n"
            body += "        </citation>\n"
            citationIndex += 1

        body += "      </citation_list>\n"
            

        body += "    </dissertation>\n"

        numDone += 1

        print(f"  Finished processing entry {numDone} out of {numEntries}")

    return body


def rowsToXML(rows, batchID, depname, depemail, registrant):
    xml = ""
    xml += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += """<doi_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.crossref.org/schema/4.8.0 https://www.crossref.org/schemas/crossref4.8.0.xsd"
    xmlns="http://www.crossref.org/schema/4.8.0" version="4.8.0">\n"""

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
    with open(f"temp/{fileID}", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
        file.close()

    remove(f"temp/{fileID}")

    xml = rowsToXML(rows, batchID, depname, depemail, registrant)
    # writeXMLToFile(xml)

    return xml
