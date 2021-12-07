def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1, n):
            if lst[j-1] > lst[j]:
                # t = lst[j-1]
                # lst[j-1] = lst[j]
                # lst[j] = t

                lst[j-1], lst[j] = lst[j], lst[j-1]


lst = [5, 2, 68, 43, 232, 34, 55, 43, 21, 23, 44, 32, 78]
bubblesort(lst)
print(lst)
