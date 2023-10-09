dict = {type([]): "list", type(()): "tuple", type({0}): "set", type({}): "dict"}

def all_thing_is_obj(obj) -> 42:
    s = type(obj)

    if s in dict:
        print("{} : {}".format( dict[s], s))
    elif s == type(""):
        print(obj + " is in the kitchen : ", s)
    else:
        print("Type not found")
    return 42
