def spellcheck(document, valid_words):
    if document == "":
        return set()
    woorden = document.replace("\n", " ")
    woorden = woorden.split(" ")
    valid_words = set(valid_words)
    result = set()
    for woord in woorden:
        if woord.lower() not in valid_words:
            result.add(woord.lower())
    return result

#print(spellcheck("the cat sat on the mat", [ 'cat', 'mat', 'sat', 'the' ]))
#print(spellcheck("", []))
print(spellcheck("the cat\nsat on\nthe mat",
            ['cat', 'sat', 'mat']))