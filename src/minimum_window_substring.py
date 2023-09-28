"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t
(including duplicates) is included in the window.
If there is no such substring, return the empty string "".


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.

"""


class SlidingWindowTracker:
    def __init__(self, chars):
        # how many copies do we need of each character
        # this object will not change
        self.required_char_counts = {}

        for c in chars:
            self.required_char_counts[c] = (
                    self.required_char_counts.get(c, 0) + 1)

        # for each required char - how many copies do we have
        # inside the sliding window
        self.sliding_window_char_tracker = {}

        # how many entries in self.sliding_window_char_tracker do not have
        # enough copies of the required char.
        # Note, here we don't count every missing char.
        # We only count unique missing chars.
        #
        # When equal to 0 - no missing chars in the sliding window.
        self.incomplete_char_tracker_entries = len(self.required_char_counts)

        self.smallest_window = None

    def remove_char(self, char):
        if char not in self.required_char_counts:
            return

        if (self.sliding_window_char_tracker[char] ==
                self.required_char_counts[char]):
            self.incomplete_char_tracker_entries += 1

        self.sliding_window_char_tracker[char] -= 1

    def add_char(self, char):
        if char not in self.required_char_counts:
            return

        self.sliding_window_char_tracker[char] = (
                self.sliding_window_char_tracker.get(char, 0) + 1)

        if (self.sliding_window_char_tracker[char] ==
                self.required_char_counts[char]):
            self.incomplete_char_tracker_entries -= 1

    def update_smallest_window(self, start, end):
        if (not self.smallest_window or
                (end - start) <
                (self.smallest_window[1] - self.smallest_window[0])):
            self.smallest_window = (start, end)

    def slide(self, string):
        start = 0
        end = 0
        while start < len(string):
            # print(self.required_char_counts, self.sliding_window_char_tracker)
            if self.incomplete_char_tracker_entries == 0:
                # our sliding window has all required chars
                self.update_smallest_window(start, end)
                # remove a char from beginning
                self.remove_char(string[start])
                start += 1
            else:
                # our sliding window does not have all required chars
                if end == len(string):
                    # if we can't increase the window we are done
                    break
                else:
                    # add char to the end
                    self.add_char(string[end])
                    end += 1

        if not self.smallest_window:
            return None

        start, end = self.smallest_window
        return string[start:end]


print(SlidingWindowTracker("A").slide("A"))
print(SlidingWindowTracker("AA").slide("A"))
print(SlidingWindowTracker("ABC").slide("ADOBECODEBANC"))
print(SlidingWindowTracker("").slide(""))
print(SlidingWindowTracker("A").slide(""))
