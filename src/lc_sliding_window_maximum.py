"""
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

return the list of Maximum Element from each window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Input: nums = [1], k = 1
Output: [1]
"""


class MaxWindow:
    def __init__(self, k):
        self.k = k
        self.counter = 0
        self.buffer = []

    def add(self, n):
        self.counter += 1
        # remove out-of-window element
        if len(self.buffer) > 0:
            counter, _ = self.buffer[0]
            if counter + self.k == self.counter:
                self.buffer.pop(0)

        # Remove all in window elements that are smaller
        # than the new element n.
        # Remove from the end, so we don't fall into O(N*k)
        for i in range(len(self.buffer)):
            counter, element = self.buffer[-1]
            if element <= n:
                self.buffer.pop()
            else:
                break

        self.buffer.append((self.counter, n))

    def get_max(self):
        return self.buffer[0][1]


def max_elements_from_sliding_window(k, numbers):
    window = MaxWindow(k)
    results = []
    for n in numbers:
        window.add(n)
        results.append(window.get_max())
    return results[k - 1:]


# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
print(max_elements_from_sliding_window(
    3, [1, 3, -1, -3, 5, 3, 6, 7]))

print(max_elements_from_sliding_window(
    1, [1]))

print(max_elements_from_sliding_window(
    5, []))
