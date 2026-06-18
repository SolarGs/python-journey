def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                year = True
            else:
                year = False
        else:   
            year = True
    else:
        year = False
    return year

print(leap_year(2400))