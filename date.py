def answer(x, y, z):
    """Determines whether a given set of numbers is a specific date"""

    # month/day/year
    # month 1-12
    # day: 1-28/30/31
        # 28: 2
        # 30: 4, 6, 9, 11
        # 31: 1, 3, 5, 7, 8, 10, 12
    # year: any (including single digit)

    date_count = 0
    arg_list = [x, y, z]
    possible_months = {num for num in arg_list if num in range(1, 13)}

    # print possible_months

    if len(possible_months) > 1:
        return "Ambiguous"




    # if date_count > 1:
    #     return "Ambiguous"
    # elif date_count == 1:
    #     pass
    #     # return formatted date
    # else:
    #     "No dates possible :("


answer(1, 3, 5)
answer(99, 13, 2)
answer(1, 1, 99)