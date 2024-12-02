# write your code here
def decode1(word):
    decoded = ""
    for char in word:
        if char == "A":
            decoded += "o"
        else:
            decoded += char
    print(decoded)
    return decoded

#print(decode1("SchAAl"))

def decode2(word):
    decoded = ""
    random = False
    for char in word:
        if not random:
            decoded += char
        random = not random
    print(decoded)
    return decoded
            
#print(decode2("hqovtzdpozgm"))

def decode3(sentence):
    zin = sentence.split(" ")
    zin[0] = zin[0][::-1]
    return " ".join(zin)

print(decode3("sepocseleT are too expensive."))

def decode4(word):
    decoded = ""
    for i in range(2, 2 + (len(word) // 2)):
        decoded += word[i]
    print(decoded)
    return decoded

#print(decode4("oddolfijnnjiflK"))

def decode5(sentence):
    decoded = ""
    for word in sentence.split(" "):
        decoded += decode4(decode2(decode1(word)))
        decoded += ' '
    decoded = decode3(decoded)
    return decoded
sentence = "MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu" 

#print(decode5(sentence))