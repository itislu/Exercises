# https://www.codewars.com/kata/550f22f4d758534c1100025a/python


from collections import deque


def dir_reduc(arr):
    deq = deque()

    while arr:
        if len(deq) > 0:
            pair = sorted([arr[-1], deq[0]])
            if pair == ["NORTH", "SOUTH"] or pair == ["EAST", "WEST"]:
                arr.pop()
                deq.popleft()
                continue
        deq.appendleft(arr.pop())

    return list(deq)


# TESTS

tests: tuple = (
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
    ["NORTH", "WEST", "SOUTH", "EAST"],
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
    ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST", "EAST"],
    [],
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"],
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"],
    ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"],
    ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"],
    ["NORTH", "WEST", "SOUTH", "EAST"],
    ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
)

expected: tuple = (
    ['WEST'],
    ["NORTH", "WEST", "SOUTH", "EAST"],
    ['WEST'],
    ['NORTH', 'NORTH'],
    [],
    [],
    ["NORTH"],
    ["EAST", "NORTH"],
    ["NORTH", "EAST"],
    ["NORTH", "WEST", "SOUTH", "EAST"],
    ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']
)

for test, expect in zip(tests, expected):
    res = dir_reduc(test)
    print("expect:", expect)
    print("result:", res)
    print("PASSED") if res == expect else print("FAILED")
    print()
