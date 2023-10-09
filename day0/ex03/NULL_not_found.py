
def printNull(str, value):
    print("{}: {} {}".format(str, value, type(value)))

def NULL_not_found(value):
    if value and value == value:
        print("Type not found")
        return 1
    if type(value) == type(None):
        printNull("Nothing", value)
    if value != value:
        printNull("Cheese", value)
    if value == 0 and type(value) != type(False):
        printNull("Zero", value)
    if value == "":
        printNull("Empty", value)
    if type(value) == type(False) and not value:
        printNull("Fake", value)
    return 0