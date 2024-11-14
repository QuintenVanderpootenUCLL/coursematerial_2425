table_of_numbers = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40),("L", 50),("XC", 90),("C", 100),("CD",400),("D", 500),("M", 1000)]
def to_roman(n):
    roman = ""
    i = len(table_of_numbers) - 1
    while i > -1:
            if table_of_numbers[i][1] <= n:
                roman += table_of_numbers[i][0]
                n -= table_of_numbers[i][1]
            else:
                i -= 1
    print(n)
    return roman

print(to_roman(5))
print(to_roman(8))
print(to_roman(2020))

def from_roman(string):
     i = 0
     while i < len(string):
