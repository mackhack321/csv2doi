import datetime  # to get the current time because crossref wants a timestamp
import csv  # to read the input data into a form the program can use
from os import remove  # to delete the input csv file when done
import io # for StringIO, reading csv data from a string
from shared import cleanString, MSU_ROR, MSU_WIKIDATA
# CSV_FILENAME = "dataset.csv"  # csv dataset to use
# XML_FILENAME = "dataset.xml"  # where to store the generated XML

# # information used in making the head
# DOI_BATCH_ID = "my_doi_batch"
# DEPOSITOR_NAME = "Mary Ann Jones"
# DEPOSITOR_EMAIL = "maw324@msstate.edu"
# REGISTRANT = "Mississippi State University"

# # information for the database itself
# DATABASE_TITLE = "Scholars Junction"

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
        authors += "          <person_name contributor_role=\"author\" sequence=\"first\">\n"
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


def makeBody(rows, dbname):
    numDone = 0
    numEntries = len(rows)
    print(f"Generating XML for {numEntries} entries...")

    body = ""

    body += "    <database>\n"
    body += "      <database_metadata language=\"en\">\n"
    body += f"        <titles><title>{dbname}</title></titles>\n"
    body += f"        <institution>\n"
    body += f"          <institution_id type=\"ror\">{MSU_ROR}</institution_id>\n"
    body += f"          <institution_id type=\"wikidata\">{MSU_WIKIDATA}</institution_id>\n"
    body += f"          <institution_department>{row[f'institutionDept']}</institution_department>\n"
    body += f"        </institution>\n"
    # body += "        <institution>\n"
    # body += f"          <institution_id type=\"ror\">{DATABASE_ROR}</institution_id>\n"
    # body += f"          <institution_id type=\"isni\">{DATABASE_ISNI}</institution_id>\n"
    # body += f"          <institution_id type=\"wikidata\">{DATABASE_WIKIDATA}</institution_id>\n"
    # body += f"          <institution_department>{DATABASE_DEPT}</institution_department>\n"
    # body += "        </institution>\n"
    # body += "        <institution>\n"
    # body += f"          <institution_name>{DATABASE_INST_NAME}</institution_name>\n"
    # body += "        </institution>\n"
    # body += "        <doi_data>\n"
    # body += f"          <doi>{DATABASE_DOI}</doi>\n"
    # body += f"          <resource>{DATABASE_RESOURCE}</resource>\n"
    # body += "        </doi_data>\n"
    body += "      </database_metadata>\n"

    for row in rows:

        body += "      <dataset dataset_type=\"collection\">\n"
        body += "        <contributors>\n"
        
        body += makeAuthors(row)

        body += "        </contributors>\n"
        body += f"        <titles><title>{row['title']}</title></titles>\n"
        body += "        <database_date>\n"
        body += "          <creation_date>\n"
        body += f"            <month>{row['creation date month']}</month>\n"
        body += f"            <day>{row['creation date day']}</day>\n"
        body += f"            <year>{row['creation date year']}</year>\n"
        body += "          </creation_date>\n"
        body += "          <publication_date>\n"
        body += f"            <month>{row['publication date month']}</month>\n"
        body += f"            <day>{row['publication date day']}</day>\n"
        body += f"            <year>{row['publication date year']}</year>\n"
        body += "          </publication_date>\n"
        # body += "          <update_date>\n"
        # body += f"            <month>{'{:02d}'.format(int(row['update date'].split('/')[0]))}</month>\n"
        # body += f"            <day>{'{:02d}'.format(int(row['update date'].split('/')[1]))}</day>\n"
        # body += f"            <year>{row['update date'].split('/')[2]}</year>\n"
        # body += "          </update_date>\n"
        body += "        </database_date>\n"
        body += "        <publisher_item>\n"
        body += f"          <item_number item_number_type=\"veryimportant\">{row['item number']}</item_number>\n"
        body += "        </publisher_item>\n"
        body += f"        <description language=\"en\">{row['description']}</description>\n"
        body += "        <format mime_type=\"text/html\"/>\n"

        body += "        <doi_data>\n"
        body += f"          <doi>{row['doi']}</doi>\n"
        body += f"          <resource>{row['resource']}</resource>\n"
        body += "        </doi_data>\n"

        body += "      </dataset>\n"

        numDone += 1

        print(f"  Finished processing entry {numDone} out of {numEntries}")

    body += "    </database>\n"

    return body


def rowsToXML(rows, batchID, depname, depemail, registrant, dbname):
    xml = ""
    xml += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += """<doi_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.crossref.org/schema/5.3.0 https://www.crossref.org/schemas/crossref5.3.0.xsd"
    xmlns="http://www.crossref.org/schema/5.3.0" version="5.3.0">\n"""

    xml += "  <head>\n"
    xml += makeHead(batchID, depname, depemail, registrant)
    xml += "  </head>\n"

    xml += "  <body>\n"
    xml += makeBody(rows, dbname)
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


def go(batchID, depname, depemail, registrant, dbname, fileID):
    rows = []
    with open(f"temp/{fileID}", 'r') as file:
        cleanedContent = cleanString(file.read())
        reader = csv.DictReader(io.StringIO(cleanedContent))
        for row in reader:
            rows.append(row)
        file.close()

    remove(f"temp/{fileID}")

    # headersAreValid = validateHeaders(reader.fieldnames)
    # if not headersAreValid:
    #     return "bad headers"

    xml = rowsToXML(rows, batchID, depname, depemail, registrant, dbname)
    # writeXMLToFile(xml)

    return xml
