
def ft_filter(function_to_apply, list_of_inputs):
    if function_to_apply == None:
        return [x for x in list_of_inputs if x]
    return [x for x in list_of_inputs if function_to_apply(x)]