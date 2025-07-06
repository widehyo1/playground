from typing import NamedTuple
from functools import reduce

class Item(NamedTuple):
    weight: int
    value: int

class Knapsack(NamedTuple):
    inventory: list[Item]
    capacity: int

# def find_recursion(ks: Knapsack):
#     results = []
#     bag = []
#     index = 0
#     acc_value = 0
# 
#     inventory = ks.inventory
# 
#     def backtrack(index: int, bag: list[Item]):
#         nonlocal acc_value
#         print(f"{acc_value=}, {index=}, {bag=}")
#         bag_weight = reduce(lambda acc, cur: acc + cur.weight, bag, 0)
#         # base condition
#         if bag_weight > ks.capacity:
#             return
#         print(f"flag1")
#         bag_value = reduce(lambda acc, cur: acc + cur.value, bag, 0)
#         if bag_value > acc_value:
#             acc_value = bag_value
#             results.clear()
#             results.append(bag[:])
#             return
#         print(f"flag2")
#         if bag_value == acc_value:
#             results.append(bag[:])
#         print(f"flag3")
# 
#         for idx in range(index, len(inventory)):
#             cur_item = inventory[idx]
#             print(f"{cur_item=}")
#             backtrack(idx + 1, [*bag, cur_item])
#             backtrack(idx + 1, bag)
# 
#     backtrack(0, [])
#     return results

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
                    reduce(lambda acc, cur: acc + cur.value, bag, 0),
                    reduce(lambda acc ,cur: acc + cur.weight,bag, 0))]
            elif cur_value == max_value: # append solution
                results.append(bag[:])
                results.append(bag[:],
                    reduce(lambda acc, cur: acc + cur.value, bag, 0),
                    reduce(lambda acc ,cur: acc + cur.weight, bag, 0))
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
    # res_recursion = find_recursion(ks)
    # print(res_recursion)
    res_iter = find_iter(ks)
    print(res_iter)
