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

from collections import defaultdict


def calculate_seats(bookings, n):
    increase_map = defaultdict(int)
    decrease_map = defaultdict(int)

    for start, end, value in bookings:
        increase_map[start] += value
        decrease_map[end + 1] -= value

    flight_seats = []
    counter = 0
    for i in range(1, n + 1):
        counter += increase_map[i] + decrease_map[i]
        flight_seats.append(counter)
    return flight_seats


print(calculate_seats([[1, 1, 20]], 1))

print(calculate_seats([[1, 2, 20]], 2))

print(
    calculate_seats(
        [[1, 2, 20], [1, 3, 10], [2, 4, 30]], 4)
)

print(calculate_seats([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 10))

"""
class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res = new int[n];
        for (int[] v : bookings) {
            res[v[0] - 1] += v[2];
            if (v[1] < n)
                res[v[1]] -= v[2];
        }
        for (int i = 1; i < n; ++i)
            res[i] += res[i - 1];
        return res;
    }
}
"""
