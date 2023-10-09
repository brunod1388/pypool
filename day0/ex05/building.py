import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    try:
        assert len(args) == 1, "wrong number of arguments"
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(1)

    dic = {"upper letters": 0, "lower letters": 0, "digits": 0, "spaces": 0, "punctuation marks": 0 }
    n = 0
    for c in args[0]:
        if c.isupper():
            dic["upper letters"] += 1
        elif c.islower():
            dic["lower letters"] += 1
        elif c.isdigit():
            dic["digits"] += 1
        elif c.isspace():
            dic["spaces"] += 1
        elif c in ".,;:!?-+*/=":
            dic["punctuation marks"] += 1
        n += 1
    print("The text contains {} characters:".format(n))
    for key, value in dic.items():
        print("{} {}".format(value, key))