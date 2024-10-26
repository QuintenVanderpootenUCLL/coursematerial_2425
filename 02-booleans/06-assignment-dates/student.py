# write your code here
def is_valid_month(month):
    return month <= 12 and month >= 1

def is_leap_year(year):
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

def has_30_days(month):
    return (month % 2 == 0 and month <= 6 or month == 9 or month == 11) and month != 2

def has_31_days(month):
    return month != 2 and not(has_30_days(month))

def has_28_days(month, year):
    return not is_leap_year(year) and month == 2

def has_29_days(month, year):
    return not(has_28_days(month, year)) and month == 2

def is_valid_date(day, month, year):
    return(
        (day <= 28
        or
        day == 29 and has_29_days(month, year)
        or
        day == 29 and has_30_days(month)
        or
        day == 29 and has_31_days(month)
        or
        day == 30 and has_31_days(month)
        or
        day == 30 and has_30_days(month)
        or
        day == 31 and has_31_days(month))
        and
        day > 0
        and 
        day < 32
    )

    