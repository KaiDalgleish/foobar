def answer(x, y, z):
    """Determines whether a given set of numbers is a specific date"""

    # month/day/year
    # month 1-12
    # day: 1-28/30/31
        # 28: 2
        # 30: 4, 6, 9, 11
        # 31: 1, 3, 5, 7, 8, 10, 12
    # year: any (including single digit)

    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    date_count = 0
    arg_list = [x, y, z]
    possible_months = {num for num in arg_list if num in range(1, 13)}

    # print possible_months

    if len(possible_months) > 1:
        return "Ambiguous"
    else:
        month = possible_months.pop()
        arg_list.remove(month)

    possible_days = {num for num in arg_list if num in range(1, (days_in_month[month] + 1))}

    # print possible_days
    if len(possible_days) > 1:
        return "Ambiguous"
    else:
        day = possible_days.pop()
        arg_list.remove(day)

    year = arg_list[0]

    month = str(month).zfill(2)
    day = str(day).zfill(2)
    year = str(year).zfill(2) 

    return "%s/%s/%s" % (month, day, year)



print answer(2, 31, 28)
print answer(2, 30, 3)
print answer(1, 1, 99)