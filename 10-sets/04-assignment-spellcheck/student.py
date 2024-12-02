def spellcheck(document, valid_words):
    found_words  = set()
    document = document.replace("\n", " ").split()
    print(document)
    valid_words = set(valid_words)
    for word in document:
        if not(word.lower() in valid_words):
            found_words.add(word.lower())
            
    return found_words



print(spellcheck("the cat\nsat on\nthe mat",
        ['cat', 'sat', 'mat']))

print(spellcheck('WORT', ['word']))