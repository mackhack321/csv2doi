MSU_ROR = "https://ror.org/0432jq872"

def cleanString(string):
    cleaned = ""

    for char in string:
        if ord(char) > 127:
            cleaned += f"&#{ord(char)};"
        elif char == '&':
            cleaned += f"&#38;"
        elif char == '<':
            cleaned += f"&#60;"
        elif char == '>':
            cleaned += f"&#62;"
        else:
            cleaned += char
    
    return cleaned