# write your code here
def decode1(word):
    decoded = ""
    for char in word:
        if char == "A":
            decoded += "o"
        else:
            decoded += char
    return decoded

print(decode1("SchAAl"))

def decode2(word):
    decoded = ""
    random = False
    for char in word:
        if not random:
            decoded += char
        random = not random
    return decoded
            
print(decode2("hqovtzdpozgm"))

def decode3(word):
    decoded = ""
    zin = word.split(" ")
    zin[0] = zin[0][::-1]
    for woord in zin:
        decoded += woord + " "
    return decoded

print(decode3("sepocseleT are too expensive."))

def decode4(word):
    decoded = ""
    for i in range(2, 2 + (len(word) // 2)):
        decoded += word[i]
    return decoded

print(decode4("oddolfijnnjiflK"))

def decode5(sentence):

    return (decode2(decode1(sentence)))

sentence = "MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu" 

print(decode5(sentence))
