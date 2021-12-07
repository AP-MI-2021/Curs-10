def pseudo_quick_sort(lst):
    if lst == []:
        return []

    pivot = lst[0]
    left = pseudo_quick_sort([x for x in lst if x < pivot])
    right = pseudo_quick_sort([x for x in lst if x > pivot])

    return left + [x for x in lst if x == pivot] + right


lst = [5, 2, 68, 43, 232, 34, 55, 43, 21, 23, 44, 32, 78]
sorted_lst = pseudo_quick_sort(lst)
print(sorted_lst)
