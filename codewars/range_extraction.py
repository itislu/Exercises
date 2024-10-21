def solution(args):
    res = ""
    l, h = 0, 0
    while l < len(args):
        h += 1
        while h < len(args) and args[h] == args[h - 1] + 1:
            h += 1
        match h - l:
            case 1:
                res += f"{args[l]},"
            case 2:
                res += f"{args[l]},{args[h - 1]},"
            case _:
                res += f"{args[l]}-{args[h - 1]},"
        l = h
    return res.strip(",")


tests = (
    [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20],
    [-3,-2,-1,2,10,15,16,18,19,20]
)
expected = (
    '-6,-3-1,3-5,7-11,14,15,17-20',
    '-3--1,2,10,15,16,18-20'
)

for test, expect in zip(tests, expected):
    res = solution(test)
    print("result:", res)
    print("expect:", expect)
    print()
