def groupby(iterable):
    group = []

    for item in iterable:
        if not group or group[-1] == item:
            group.append(item)
        else:
            yield group
            group = [item]

    yield group


print(list(groupby([1, 1, 2, 2, 3, 3, 3, 4, 5])))
