# write your code here
def palindrome(string):
    reverse = string[::-1]
    return reverse == string
palindrome("RADAR")