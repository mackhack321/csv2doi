import csv  # to read the input data into a form the program can use
from os import remove  # to delete the input csv file when done
import io # for StringIO, reading csv data from a string
from shared import cleanString

def makeHead(batchID, depname, depemail):
    head = ""

    head += f"    <doi_batch_id>{batchID}</doi_batch_id>"

    head += f"""    <depositor>
      <depositor_name>{depname}</depositor_name>
      <email_address>{depemail}</email_address>
    </depositor>\n"""

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
        body += "    <doi_citations>\n"

        body += f"      <doi>{row['doi']}</doi>\n"

        body += "      <citation_list>\n"
        
        body += makeCitations(row)

        body += "      </citation_list>\n"
            

        body += "    </doi_citations>\n"

        numDone += 1

        print(f"  Finished processing entry {numDone} out of {numEntries}")

    return body


def rowsToXML(rows, batchID, depname, depemail):
    xml = ""
    xml += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += """<doi_batch version="4.4.2" xmlns="http://www.crossref.org/doi_resources_schema/4.4.2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.crossref.org/doi_resources_schema/4.4.2 http://www.crossref.org/schemas/doi_resources4.4.2.xsd">\n"""

    xml += "  <head>\n"
    xml += makeHead(batchID, depname, depemail)
    xml += "  </head>\n"

    xml += "  <body>\n"
    xml += makeBody(rows)
    xml += "  </body>\n"

    xml += "</doi_batch>"

    print("Successfully generated XML\n")

    return xml

def go(batchID, depname, depemail, fileID):
    rows = []
    with open(f"temp/{fileID}", 'r', encoding="utf-8-sig") as file:
        cleanedContent = cleanString(file.read())
        reader = csv.DictReader(io.StringIO(cleanedContent))
        for row in reader:
            rows.append(row)
        file.close()

    remove(f"temp/{fileID}")

    xml = rowsToXML(rows, batchID, depname, depemail)

    return xml
