"""
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element that appears
strictly more than N/2 times in the array.

None if no such element.

Moore’s Voting Algorithm

"""


def find_majority_element(elements):
    majority_element = None
    majority_element_count = 0

    for e in elements:
        if e == majority_element:
            majority_element_count += 1
        else:
            majority_element_count -= 1
            if majority_element_count <= 0:
                majority_element_count = 1
                majority_element = e

    majority_element_count = sum(e == majority_element for e in elements)

    if majority_element_count > len(elements) / 2:
        return majority_element
    else:
        return None


print(find_majority_element([1, 2, 3, 1, 1]))
