from sos import toMorse
import sys

tests = {
    "sos": "... --- ...",
    "Il etait uen fois la vie": ".. .-.. / . - .- .. - / ..- . -. / ..-. --- .. ... / .-.. .- / ...- .. .",
    "ABCD EFGH IJKL MNOP QRST UVWX YZ 0123 4567 89": ".- -... -.-. -.. / . ..-. --. .... / .. .--- -.- .-.. / -- -. --- .--. / --.- .-. ... - / ..- ...- .-- -..- / -.-- --.. / ----- .---- ..--- ...-- / ....- ..... -.... --... / ---.. ----.",
}
if __name__ == "__main__":
    for test in tests:
        print("Testing: {:48} result: ".format(test), end=" ")
        try:
            assert toMorse(test) == tests[test]
            print(u'\u2713')
        except AssertionError as e:
            print(e)
            print(u'\u2717')
            print("Got     : {}$".format(toMorse(test)))
            print("Expected: {}$".format(tests[test]))