# write your code here
def increase_version(version, breaking_change, new_features):
    major , minor , patch = version
    if breaking_change:
        major += 1
        minor = 0
        patch = 0
    elif new_features:
        minor += 1
        patch = 0
    else:
        patch += 1
    return (major, minor, patch)

print(increase_version((2,1,2), False, False))
print(increase_version((2,1,2), True, False))
print(increase_version((2,1,2), False, True))

def is_more_recent(v1, v2):
    return v1 > v2

def is_older(v1, v2):
    return v1 < v2