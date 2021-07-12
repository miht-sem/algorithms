import bisect


def bin_search(list_, item):

    low = 0
    high = len(list_) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = list_[middle]
        if guess == item:
            return middle
        if guess < item:
            low = middle + 1
        else:
            high = middle - 1

    return None


mas = [1, 2, 3, 4, 5]
print(bin_search(mas, 5))
print(bin_search(mas, -1))

result = bisect.bisect_left(mas, -3, lo=0, hi=len(mas))
print(result) if mas[result] == -3 else print(None)

result = bisect.bisect_left(mas, 1, lo=0, hi=len(mas))
print(result) if mas[result] == 1 else print(None)