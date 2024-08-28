"""
https://leetcode.com/problems/corporate-flight-bookings/description/

There are n flights that are labeled from 1 to n.

You are given an array of flight bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.



Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]
Example 2:

Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]
"""

from itertools import accumulate


def calculate_seats(bookings, n):
    changes = [0] * (n + 2)  # We use n+2 to handle the case where end+1 == n+1
    for start, end, value in bookings:
        changes[start] += value
        # changes[end + 1] -= value
        changes

    return list(accumulate(changes[1:n + 1]))  # We slice to get the correct range


print(calculate_seats([[1, 1, 20]], 1))

print(calculate_seats([[1, 2, 20]], 2))

print(
    calculate_seats(
        [[1, 2, 20], [1, 3, 10], [2, 4, 30]], 4)
)

print(calculate_seats([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 10))

