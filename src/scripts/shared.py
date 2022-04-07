def cleanString(string):
    cleaned = ""

    for char in string:
        if ord(char) > 127:
            cleaned += f"&#{ord(char)};"
        else:
            cleaned += char
    
    return cleaned