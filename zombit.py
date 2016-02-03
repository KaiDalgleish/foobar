def answer(intervals):
    """Given a list of intervals, return the total number of supervised hours"""
    
    merged_intervals = []
    supervised_hours = 0

    # sort intervals and use first interval as current range
    sorted_intervals = sorted(intervals)
    low, high = sorted_intervals[0]

    # iterate through the rest of the ranges
    for interval in sorted_intervals[1:]:
        # if they overlap the current range, extend the current range
        if interval[0] <= high:
            high = max(high, interval[1])
        else:
            # save the current range, and start a new current range
            merged_intervals.append([low, high])
            low, high = interval

    merged_intervals.append([low, high])

    # add up the ranges
    for interval in merged_intervals:
        supervised_hours += interval[1] - interval[0]

    return supervised_hours

# print answer([[1, 3], [2, 7], [3, 6], [10, 15], [11, 12]])

# print answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]])
