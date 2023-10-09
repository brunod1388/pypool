def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list."""
    shapeDim = (len(family), len(family[0]))
    newShape = family[start:end]
    new_shapeDim = (len(newShape), len(newShape[0]))
    print("My shape is: ", shapeDim)
    print("My new shape is: ", new_shapeDim)
    return newShape
