def answer(x, y, z):
    """Determines whether a given set of numbers can form a single date"""


    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    arg_list = [x, y, z]
    possible_months = {num for num in arg_list if num in range(1, 13)}

    if len(possible_months) > 1:
        return "Ambiguous"
    else:
        month = possible_months.pop()
        arg_list.remove(month)

    possible_days = {num for num in arg_list if num in range(1, (days_in_month[month] + 1))}

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