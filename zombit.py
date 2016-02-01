def answer(intervals):
    """Given a list of intervals, return the total number of supervised hours"""

    supervised_hours = set()

    for interval in intervals:
        # [1, 3]
        for num in range(interval[0], interval[1]):
            supervised_hours.add(num)

    return len(supervised_hours)




# intervals = [[1, 3], [3, 6]]
# > 5
print answer([[1, 3], [3, 6]])

# intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
# > 16
print answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]])