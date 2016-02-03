def answer(intervals):
    """Given a list of intervals, return the total number of supervised hours"""

    # sort list of intervals, so first item in list is in order
    sorted_intervals = sorted(intervals)
    merged_intervals = []

    low, high = sorted_intervals[0]
    # print "low:", low
    # print "high:", high

    # iterate through rest of sorted list
    for interval in sorted_intervals[1:]:
        # if start is less than high, make it the new high
        if interval[0] <= high:
            high = interval[1]
        else:
        # else save old range, start new range
            merged_intervals.append([low, high])
            low, high = interval

    merged_intervals.append([low, high])

    return merged_intervals


# set gives memory errors, lists give time errors.

# intervals = [[1, 3], [3, 6]]
# > 5
# answer([[1, 3], [2, 7], [3, 6]])

# intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
# > 16
# [[4, 20]]
print answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]])