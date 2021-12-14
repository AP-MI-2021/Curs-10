def bubblesort_with_key(lst, key):
    n = len(lst)
    for i in range(n):
        for j in range(1, n):
            if key(lst[j-1]) > key(lst[j]):
                # t = lst[j-1]
                # lst[j-1] = lst[j]
                # lst[j] = t

                lst[j-1], lst[j] = lst[j], lst[j-1]

    return lst

def bubblesort_with_cmp(lst, cmp):
    n = len(lst)
    for i in range(n):
        for j in range(1, n):
            if cmp(lst[j-1], lst[j]):
                # t = lst[j-1]
                # lst[j-1] = lst[j]
                # lst[j] = t

                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


lst = [5, 2, 68, 43, 232, 34, 55, 43, 21, 23, 44, 32, 78]
print(bubblesort_with_key(lst, key=lambda x: -x))
lst = [5, 2, 68, 43, 232, 34, 55, 43, 21, 23, 44, 32, 78]
print(bubblesort_with_cmp(lst, cmp=lambda x, y: x > y))
