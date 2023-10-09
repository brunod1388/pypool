from ft_filter import ft_filter
import sys

if __name__ == "__main__":
    '''
    1st argument is a string of space-separated words
    2nd argument is an integer that will be the length of the words to keep
    '''
    args = sys.argv[1:]
    try:
        assert len(args) == 2, "the arguments are bad len"
        assert args[1].isdigit(), "the arguments are bad int"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    l = int (args[1])
    print(ft_filter(lambda x: (len(x) == l), args[0].split(' ')))
    print(ft_filter(None, args[0].split(' ')))
