MSU_ROR = "https://ror.org/0432jq872"
MSU_WIKIDATA = "https://www.wikidata.org/wiki/Q1939211"

def cleanString(string):
    cleaned = ""

    for char in string:
        if ord(char) > 127:
            cleaned += f"&#{ord(char)};"
        else:
            cleaned += char
    
    return cleaned