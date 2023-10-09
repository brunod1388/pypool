import sys
morse = {
    ' ': "/ ",
    'A': ".- ",
    'B': "-... ",
    'C': "-.-. ",
    'D': "-.. ",
    'E': ". ",
    'F': "..-. ",
    'G': "--. ",
    'H': ".... ",
    'I': ".. ",
    'J': ".--- ",
    'K': "-.- ",
    'L': ".-.. ",
    'M': "-- ",
    'N': "-. ",
    'O': "--- ",
    'P': ".--. ",
    'Q': "--.- ",
    'R': ".-. ",
    'S': "... ",
    'T': "- ",
    'U': "..- ",
    'V': "...- ",
    'W': ".-- ",
    'X': "-..- ",
    'Y': "-.-- ",
    'Z': "--.. ",
    '0': "----- ",
    '1': ".---- ",
    '2': "..--- ",
    '3': "...-- ",
    '4': "....- ",
    '5': "..... ",
    '6': "-.... ",
    '7': "--... ",
    '8': "---.. ",
    '9': "----. ",
}

def isMorse(msg):
    for c in msg:
        if c.upper() not in morse:
            return False
    return True

def toMorse(msg):
    morsMsg = ""
    for c in msg:
        if c.upper() not in morse.keys():
            raise AssertionError("the arguments are bad morse")
        morsMsg += morse[c.upper()]
    return morsMsg[:-1]

if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)
    if argc == 0:
        exit()
    try:
        assert argc == 1, "the arguments are bad len"
        print(toMorse(args[0]))
    except AssertionError as e:
        print("AssertionError:" + str(e))
        sys.exit(1)