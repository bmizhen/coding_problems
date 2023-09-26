"""
# Implement a Unit Conversion calculator.

Given a list of  unit conversion facts in the tuple form
[(amount, from unit, to unit), ] you should be able to answer
queries (amount, from unit, to unit).

Print "Can't convert" if unable to convert.

Example Facts:
10 mm -> 1 cm
100 cm -> 1 m
1000 m -> 1 km
39.3701 in -> 1 m
12 in -> 1 f

60 sec in 1 min
3600 sec in 1 hour
24 hour in 1 day
365 day in 1 year
12 month -> 1 year

Example Queries:
 10 f -> km
 1 month -> sec
 1 hr -> in
"""
import math


class UnitNode:
    def __init__(self, unit: str):
        self.unit = unit
        self.conversions: dict[UnitNode, float] = dict()

    def add_conversion(self, unit, multiplier):
        self.conversions[unit] = multiplier

    def __repr__(self):
        conversions = [
            (node.unit, multiplier)
            for node, multiplier in self.conversions.items()]

        return f'{self.unit} -> {conversions}'


def create_conversion_graph(
        facts: list[tuple[float, str, str]]
) -> dict[str, UnitNode]:
    nodes: dict[str, UnitNode] = dict()

    for amount, from_unit, to_unit in facts:
        if from_unit not in nodes:
            nodes[from_unit] = UnitNode(from_unit)

        if to_unit not in nodes:
            nodes[to_unit] = UnitNode(to_unit)

        nodes[from_unit].add_conversion(
            nodes[to_unit], 1 / amount)

        nodes[to_unit].add_conversion(
            nodes[from_unit], amount)

    return nodes


def convert(facts_map, query):
    amount, from_unit, to_unit = query

    if ((from_unit not in facts_map) or
            (to_unit not in facts_map)):
        return "Can't Convert"

    answer = amount * convert_rec(
        facts_map[from_unit],
        facts_map[to_unit],
        set())

    if math.isnan(answer):
        return "Can't Convert"
    else:
        return answer


def convert_rec(from_unit: UnitNode, to_unit: UnitNode, visited: set):
    if from_unit.unit == to_unit.unit:
        return 1

    if from_unit in visited:
        return math.nan

    visited.add(from_unit)

    if to_unit in from_unit.conversions:
        return from_unit.conversions[to_unit]
    else:
        for next_from_unit in from_unit.conversions.keys():
            multiple = convert_rec(
                next_from_unit, to_unit, visited)
            if not math.isnan(multiple):
                return multiple * from_unit.conversions[next_from_unit]
    return math.nan


conversion_graph = create_conversion_graph([
    (10, 'mm', 'cm'), (100, 'cm', 'm'), (1000, 'm', 'km'),
    (39.3701, 'in', 'm'), (12, 'in', 'f'),
    (60, 'sec', 'min'), (3600, 'sec', 'hour'), (24, 'hour', 'day'),
    (365, 'day', 'year'), (12, 'month', 'year')
])

print(conversion_graph)

print(convert(conversion_graph, (10, 'month', 'year')))
print(convert(conversion_graph, (10, 'month', 'in')))
print(convert(conversion_graph, (10, 'f', 'mm')))
print(convert(conversion_graph, (10, 'year', 'sec')))
print(convert(conversion_graph, (10, 'year', 'in')))
print(convert(conversion_graph, (10, 'year', 'year')))
print(convert(conversion_graph, (10, 'year', 'bar')))
