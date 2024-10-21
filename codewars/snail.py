# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python


# First move is measurement of length of square
# Then, every 2 moves length is decreased by 1
def snail(snail_map):
    res = []
    lim = len(snail_map[0])
    x, y = -1, 0
    dir = 1

    for _ in range(lim):
        x += dir
        res.append(snail_map[y][x])
    lim -= 1

    while lim > 0:
        for _ in range(lim):
            y += dir
            res.append(snail_map[y][x])
        dir *= -1
        for _ in range(lim):
            x += dir
            res.append(snail_map[y][x])
        lim -= 1

    return res


# TESTS

tests = (
    [[1,2,3],
     [4,5,6],
     [7,8,9]],
    [[1,2,3],
     [8,9,4],
     [7,6,5]]
)
expected = (
    [1,2,3,6,9,8,7,4,5],
    [1,2,3,4,5,6,7,8,9]
)

for test, expect in zip(tests, expected):
    res = snail(test)
    print("expect:", expect)
    print("result:", res)
    print("PASSED") if res == expect else print("FAILED")
    print()
