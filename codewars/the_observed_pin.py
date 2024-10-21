# https://www.codewars.com/kata/5263c6999e0f40dee200059d/python


options = {
    '1': ('1', '2', '4'),
    '2': ('2', '1', '3', '5'),
    '3': ('3', '2', '6'),
    '4': ('4', '1', '5', '7'),
    '5': ('5', '2', '4', '6', '8'),
    '6': ('6', '3', '5', '9'),
    '7': ('7', '4', '8'),
    '8': ('8', '5', '7', '9', '0'),
    '9': ('9', '6', '8'),
    '0': ('0', '8')
}


# The solution has to be by going into one direction of the string, and at every position trying all possibilities of the characters behind.
# Like counting numbers, it produces all options of the rightmost character first.
def get_pins(observed):
    def all_options_at_index(s, i):
        res = []

        if i == len(s) - 1:
            for o in options[s[i]]:
                res.append(f"{s[:i]}{o}")
        else:
            for o in options[s[i]]:
                res.extend(all_options_at_index(f"{s[:i]}{o}{s[i+1:]}", i + 1))

        return res

    return all_options_at_index(observed, 0)


# TESTS

tests = ("111111111111",)
expected = (["11", "22", "44", "12", "21", "14", "41", "24", "42"],)

for test, expect in zip(tests, expected):
    res = get_pins(test)
    print("expect:", expect)
    print("result:", res)
    print("PASSED") if res == expect else print("FAILED")
    print()
