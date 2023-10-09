
def ft_tqdm(lst: range) -> None:
    num = 0
    full = len(lst)
    BAR_LEN = 70
    while num in range(full+1):
        yield num
        percent = num / full
        print("{0:3.0f}%|{1:{2}}| {3}/{4}".format(percent * 100, u"\u2588" * int(percent * BAR_LEN), BAR_LEN, num, full), end="\r")
        num += 1