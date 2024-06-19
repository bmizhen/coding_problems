# Hi, and welcome to the Ally's Corner Deli!
#
# We are building a system to tell us how valuable our goods are!
# We hope this will allow us to add more items for sale.
#
# First, an introduction to our system:
#
# - All items have a Shelf Life attr which denotes the number of days
# we have to sell the item
# - All items have a Value attr which denotes how valuable the item is
# - At the end of each day our system lowers both values for every item
#
#
#
# ## Items
#
#
# Item Name     |     Value         |     Shelf Life
# --------------|-------------------|----------------
# Apple         |     10            |     5
# Candy         |     20            |     50
# Fancy Pants   |     100           |     100
# Salmon        |     80            |     10
#
#
# ## Directions
#
# We'd love to know how the Value of our wares changes over time!
#
# Write a function `value_after(item, days)` that takes an item and a
# number of days and outputs the Value of the item after that many days.
# You can assume all items are "fresh" and start with maximum Value.
#
# Remember, there's no "correct" answer to this and we're not interested
# in any particular solution. We're more intrigued by how you deal with
# evolving and often competing requirements.
#
# Here we go!


## Initial Requirements
# 1. All items start with their maximum Value
# 2. For all items, Value decays by 1 after each Day
# 3. Can obtain Value for Apple after 1 day
# 4. Can obtain Value for Apple after 10 days
# 5. Can obtain the Value for a second item (Candy) after 10 days

class Item:
    MAX_VALUE = 200

    def __init__(self, name: str, value: int, shelf_life: int, decay_rate=1):
        self.name = name
        self.value = value
        self.shelf_life = shelf_life
        self.decay_rate = decay_rate

    def value_after(self, days):
        if self.shelf_life < days:
            value = self.value - self.shelf_life * self.decay_rate
            value -= (days - self.shelf_life) * self.decay_rate * 2
        else:
            value = self.value - days * self.decay_rate

        return min(max(0, value), Item.MAX_VALUE)


class DurableItem(Item):
    def __init__(self, name, value, decay_rate=0):
        super().__init__(name, value, 10 ** 10, decay_rate)


class Inventory:
    def __init__(self, items: list[Item]):
        self.items = {item.name: item for item in items}

    def value_after(self, item_name: str, days):
        if item_name not in self.items:
            return None
        item = self.items[item_name]
        return item.value_after(days)


# Item Name     |     Value         |     Shelf Life
# --------------|-------------------|----------------
# Apple         |     10            |     5
# Candy         |     20            |     50
inventory = Inventory(
    [Item('Apple', 10, 5),
     Item('Candy', 20, 50),
     Item('Salmon', 80, 10, decay_rate=2),
     Item('Cheese', 30, 10, decay_rate=-1),
     DurableItem('Diamond', 150)])

assert inventory.value_after('Diamond', 900) == 150

assert inventory.value_after('foo', 9) == None
assert inventory.value_after('Apple', 1) == 9
assert inventory.value_after('Apple', 5) == 5
assert inventory.value_after('Apple', 6) == 3

assert inventory.value_after('Apple', 10) == 0
assert inventory.value_after('Apple', 9) == 0

assert inventory.value_after('Candy', 10) == 10

assert inventory.value_after('Salmon', 1) == 78
assert inventory.value_after('Salmon', 11) == 56

assert inventory.value_after('Cheese', 1) == 31
assert inventory.value_after('Cheese', 11) == 42
assert inventory.value_after('Cheese', 1111) == 200
