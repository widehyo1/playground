from typing import NamedTuple

class Item(NamedTuple):
    weight: int
    value: int

class Knapsack(NamedTuple):
    inventory: list[Item]
    capacity: int

class Walker(NamedTuple):
    index: int
    bag: list[Item]
    cur_weight: int
    cur_value: int

def find_iter(ks: Knapsack):
    results = []
    inventory = ks.inventory
    max_value = 0

    cur_weight = 0
    cur_value = 0
    index = 0
    bag = []

    stack = [Walker(index, bag, cur_weight, cur_value)]

    while stack:
        index, bag, cur_weight, cur_value = stack.pop()
        # base condition1: exceed capacity
        if ks.capacity < cur_weight:
            continue
        # base condition2: all items checked
        if index == len(inventory):
            if cur_value > max_value: # new value
                max_value = cur_value
                results = [(bag[:],
                    sum(item.value for item in bag),
                    sum(item.weight for item in bag))]
            elif cur_value == max_value: # append solution
                results.append((bag[:],
                    sum(item.value for item in bag),
                    sum(item.weight for item in bag)))
            continue

        # biz logic
        cur_item = inventory[index]
        stack.append(Walker(index + 1, bag, cur_weight, cur_value)) # backtrack
        stack.append(Walker(
            index + 1,
            [*bag, cur_item],
            cur_weight + cur_item.weight,
            cur_value + cur_item.value)
        ) # proceed

    return results


if __name__ == '__main__':
    weights = [12,1,4,1,2]
    values  = [4,2,10,1,2]
    inventory = [Item(w, v) for w, v in zip(weights, values)]
    capacity = 15
    ks = Knapsack(inventory, capacity)
    print(ks)
    res_iter = find_iter(ks)
    print(res_iter)
