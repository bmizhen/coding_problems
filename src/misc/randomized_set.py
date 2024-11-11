# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import choice


class RandomizedSet:

    def __init__(self):
        print()
        self.map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.array)
        self.array.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        self.array[index] = self.array[-1]
        self.map[self.array[index]] = index

        del self.map[val]
        self.array.pop()

        return True

    def getRandom(self) -> int:
        return choice(self.array)
