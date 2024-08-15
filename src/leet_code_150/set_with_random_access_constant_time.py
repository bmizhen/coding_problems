'''
https://leetcode.com/problems/insert-delete-getrandom-o1/description/

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


average O(1) time.

## Extension: Allow for duplicates, i.e. inserting the same element multiple times.
## But make sure random access still uniform taking into account number of duplicates.

'''


class RandomAccessSet:
    def __init__(self) -> None:
        self.element_map = {}
        self.random_access_array = []

    def insert(self, val):
        if val in self.element_map:
            return False
        self.random_access_array.append(val)
        self.element_map[val] = len(self.random_access_array) - 1
        return True

    def get_random(self):
        if not self.element_map:
            raise Exception('no elements in the array')

        from random import choice
        return choice(self.random_access_array)

    def remove(self, val):
        if val not in self.element_map:
            return False
        self._remove_from_access_array(val)
        del self.element_map[val]
        return True

    def _remove_from_access_array(self, val):
        location = self.element_map[val]

        if location == len(self.random_access_array) - 1:
            self.random_access_array.pop()
        else:
            self.random_access_array[location] = self.random_access_array.pop()
            self.element_map[self.random_access_array[location]] = location
