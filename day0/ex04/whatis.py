import sys

if len(sys.argv) > 1:
    try:
        assert len(sys.argv) < 3, "more than one argument provided"
        tp = "odd" if int(sys.argv[1]) % 2 else "even"
        print("I'm {}".format(tp))
    except AssertionError as msg:
        print("Assertion Error:", msg)
    except ValueError:
        print("Assertion Error: argument is not an integer")