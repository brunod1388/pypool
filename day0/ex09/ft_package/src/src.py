from typing import TypeVar, Generic


T = TypeVar('T')

def count_in_list(lst:list[T], value:T) -> int:
    return lst.count(value)
