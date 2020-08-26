def is_leap(year):
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input())
print(is_leap(year))

# Created by me
def leap_year(year):
    if year % 4 == 0:
      return True
    else:
        return False
    if year % 100 == 0:
        return False
    else:
        return True
    if year % 400 == 0:
        return True
    else:
        return False
while(True):
    year = int(input("Enter a year:\n"))
    print(leap_year(year))


