from random import randint


def quick_merge_middle_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        main_el = len(list_) // 2
        pivot = list_[main_el]
        less = [i for i in list_[:main_el] if i <= pivot] + [i for i in list_[main_el + 1:] if i <= pivot]
        greater = [i for i in list_[:main_el] if i > pivot] + [i for i in list_[main_el + 1:] if i > pivot]
        return quick_merge_middle_sort(less) + [pivot] + quick_merge_middle_sort(greater)


def quick_merge_random_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        main_el = randint(0, len(list_) - 1)
        pivot = list_[main_el]
        less = [i for i in list_[:main_el] if i <= pivot] + [i for i in list_[main_el + 1:] if i <= pivot]
        greater = [i for i in list_[:main_el] if i > pivot] + [i for i in list_[main_el + 1:] if i > pivot]
        return quick_merge_random_sort(less) + [pivot] + quick_merge_random_sort(greater)


def quick_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        pivot = list_[0]
        less = [i for i in list_[1:] if i <= pivot]
        greater = [i for i in list_[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_smart_random_sort(list_):
    if len(list_) < 2:
        return list_
    main_el = randint(0, len(list_) - 1)
    pivot = list_[main_el]
    less = list(filter(lambda x: x < pivot, list_))
    greater = list(filter(lambda x: x > pivot, list_))
    return quick_smart_random_sort(less) + [pivot] + quick_smart_random_sort(greater)


mas = [10, 9, 8, 7, 6]
print(quick_merge_middle_sort(mas))
