"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs
to integer directly.

"""


def reverse_str(s):
    return str(s)[::-1]


def pad_zeros(num1, num2):
    padding = '0' * abs(len(num1) - len(num2))

    if len(num1) > len(num2):
        num2 += padding
    else:
        num1 += padding
    return num1, num2


ADDITION_TABLE = {
    (str(i), str(j)): reverse_str(i + j) + '0'
    for i in range(10)
    for j in range(10)
}

MULTIPLICATION_TABLE = {
    (str(i), str(j)): reverse_str(i * j) + '0'
    for i in range(10)
    for j in range(10)
}


def add_rev(num1, num2):
    num1, num2 = pad_zeros(num1, num2)

    carry = '0'
    result = []

    for i in range(len(num1)):
        # may overflow into tens
        units, tens, *_ = ADDITION_TABLE[num1[i], num2[i]]
        units_and_carry, new_carry, *_ = ADDITION_TABLE[units, carry]
        carry, *_ = ADDITION_TABLE[tens, new_carry]

        result.append(units_and_carry)

    if carry != '0':
        result.append(carry)

    return result


def multiply_rev(num1, num2):
    result = '0'

    for power, digit in enumerate(num1):
        intermediate_sum = ['0'] * power
        carry = '0'
        for digit2 in num2:
            units, tens, *_ = MULTIPLICATION_TABLE[digit, digit2]
            units_and_carry, new_carry, *_ = ADDITION_TABLE[units, carry]
            carry, *_ = ADDITION_TABLE[tens, new_carry]

            intermediate_sum.append(units_and_carry)

        if carry != '0':
            intermediate_sum.append(carry)

        result = add_rev(result, ''.join(intermediate_sum))

    if result == ['0'] * len(result):
        return '0'

    return result


def multiply_symbolic(num1, num2):
    return ''.join(reversed(
        multiply_rev(reverse_str(num1), reverse_str(num2))))


def add_symbolic(n1, n2):
    return ''.join(reversed(
        add_rev(reverse_str(n1), reverse_str(n2))))


print(add_symbolic('5', '5'))
print(add_symbolic('0', '0'))
print(add_symbolic('999', '1'))
print(add_symbolic('998', '1'))
print(add_symbolic('998', '0'))
print(add_symbolic('998', '1000'))

print(multiply_symbolic("1", "1"))
print(multiply_symbolic("1", "0"))
print(multiply_symbolic("0", "0"))
print(multiply_symbolic("9", "9"))
print(multiply_symbolic("5", "5"))
print(multiply_symbolic("9", "1000"))
print(multiply_symbolic("999", "99"))
print(multiply_symbolic("23", "123"))

for i in range(100):
    for j in range(100):
        # print(i, j, multiply_symbolic(str(i), str(j)))
        assert str(i * j) == multiply_symbolic(str(i), str(j))
