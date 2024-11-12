# https://leetcode.com/problems/find-k-closest-elements/description/

from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = 0
        hi = len(arr) - k

        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                hi = mid
            else:
                lo = mid + 1
        return arr[lo:lo + k]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        MAX = abs(arr[-1]) + abs(arr[0])
        # print(len(arr))
        x_index = bisect_left(arr, x)
        # print(x_index, arr[x_index])
        left = x_index - 1
        right = x_index
        # print(left, right)

        result = []

        while k > 0:
            if left >= 0:
                dl = abs(x - arr[left])
            else:
                dl = MAX

            if right < len(arr):
                dr = abs(x - arr[right])
            else:
                dr = MAX

            if dr == MAX and dl == MAX:
                break

            if dr == MAX or dl <= dr:
                result.insert(0, arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            k -= 1

        return result
