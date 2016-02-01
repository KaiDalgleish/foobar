def answer(intervals):
    """Given a list of intervals, return the total number of supervised hours"""

    # add first interval as seed
    supervised_hours = intervals[0]

    # for interval in intervals:
    #     for num in range(interval[0], interval[1]):
    #         if num not in supervised_hours:
    #             supervised_hours.append(num)

    # return len(supervised_hours)



    for interval in intervals[1:]:
        print "interval:", interval
        for hour_group in supervised_hours:
            print "hours:", hour_group
    #         if (interval[0] in range(hour_group[0], hour_group[1])) and (interval[1] > hour_group[1]):
    #             print "interval in range"
    #             hour_group[1] = interval[1]
    #         else:
    #             "adding interval"
    #             supervised_hours.append(interval)

    print "suped:", supervised_hours


# set gives memory errors, lists give time errors.

# intervals = [[1, 3], [3, 6]]
# > 5
print answer([[1, 3], [3, 6]])

# intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
# > 16
# print answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]])