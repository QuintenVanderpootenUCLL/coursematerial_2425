# write your code here
def matches_pattern(pattern, string):
    if len(pattern) != len(string):
        return False
    patstr = dict()
    strpat = dict()

    for i in range(len(pattern)):
        print(strpat)
        print("__________________")
        if string[i] in strpat and strpat[string[i]] != pattern[i]:
            return False
        if pattern[i] not in patstr:
            patstr[pattern[i]] = string[i]
            strpat[string[i]] = pattern[i]

        else:
            if patstr[pattern[i]] != string[i]:
                return False
    return True


#print(matches_pattern("PFR", "CAT"))
#print(matches_pattern("AA","XX"))
print(matches_pattern("AB", "XX"))
print(matches_pattern("ABCABC", "TOKTOK"))