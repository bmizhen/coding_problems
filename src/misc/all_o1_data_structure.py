# https://leetcode.com/problems/all-oone-data-structure/

class ListItem:
    def __init__(self, val, before=None, after=None):
        self.val = val
        self.before = before
        self.after = after

    def __repr__(self):
        return str(['LI', self.val])


class LL:
    def __init__(self):
        self.first = None
        self.last = None

    def __repr__(self):
        res = []
        li = self.first
        while li:
            res.append(li)
            li = li.after
        return str(res)

    def remove(self, li):
        if self.first == li:
            self.first = li.after
        if self.last == li:
            self.last = li.before

        if li.after:
            li.after.before = li.before
        if li.before:
            li.before.after = li.after

    def insert_after(self, li, val):
        new_li = ListItem(val, li, li.after)
        li.after = new_li
        if new_li.after:
            new_li.after.before = new_li
        if self.last == li:
            self.last = new_li
        return new_li

    def insert_before(self, li, val):
        if not self.first:
            new_li = ListItem(val)
            self.first = new_li
            self.last = new_li
            return new_li
        else:
            new_li = ListItem(val, li.before, li)
            li.before = new_li

            if new_li.before:
                new_li.before.after = new_li

            if self.first == li:
                self.first = new_li

            return new_li


class AllOne:

    def __init__(self):
        self.ll = LL()
        self.li_map = {}

    def inc(self, key: str) -> None:
        if key not in self.li_map:
            if self.ll.first and self.ll.first.val[0] == 1:
                self.li_map[key] = self.ll.first
                self.ll.first.val[1].add(key)
            else:
                new_li = self.ll.insert_before(self.ll.first, (1, {key}))
                self.li_map[key] = new_li
            # print(self.li_map, self.ll)
            return

        li = self.li_map[key]
        count, key_set = li.val
        key_set.remove(key)

        if li.after and li.after.val[0] == count + 1:
            li.after.val[1].add(key)
            self.li_map[key] = li.after
        else:
            new_li = self.ll.insert_after(li, (count + 1, {key}))
            self.li_map[key] = new_li

        if not key_set:
            self.ll.remove(li)

        # print(self.li_map, self.ll)

    def dec(self, key: str) -> None:
        li = self.li_map[key]
        count, key_set = li.val
        key_set.remove(key)

        if count == 1:
            del self.li_map[key]
            if not key_set:
                self.ll.remove(li)

            # print(self.li_map, self.ll)
            return

        if li.before and li.before.val[0] == count - 1:
            li.before.val[1].add(key)
            self.li_map[key] = li.before
        else:
            new_li = self.ll.insert_before(li, (count - 1, {key}))
            self.li_map[key] = new_li

        if not key_set:
            self.ll.remove(li)

        # print(self.li_map, self.ll)

    def getMaxKey(self) -> str:
        if not self.ll.last:
            return ''
        else:
            for e in self.ll.last.val[1]:
                return e

    def getMinKey(self) -> str:
        if not self.ll.first:
            return ''
        else:
            for e in self.ll.first.val[1]:
                return e

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
