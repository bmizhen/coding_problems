# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
           return 2147483647

        negate_result = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if divisor > dividend:
            return 0

        divisor_doubles = [(divisor, 1)]
        while divisor_doubles[-1][0] < dividend:
            div, count = divisor_doubles[-1]
            divisor_doubles.append((div + div, count + count))

        result = 0
        while divisor_doubles:
            # print(divisor_doubles, dividend)
            div, count = divisor_doubles[-1]
            if div > dividend:
                divisor_doubles.pop()
            else:
                dividend -= div
                result += count

        return -result if negate_result else result
