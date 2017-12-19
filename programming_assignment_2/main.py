import time


def quick_sort(lst, l, r, method):
    # method 1 => first element as a pivot
    # method 2 => last element as a pivot
    # method 3 => median as a pivot
    if l >= r:
        return

    pivot_index = partition(lst, l, r, method)
    quick_sort(lst, l, pivot_index, method)
    quick_sort(lst, pivot_index+1, r, method)
    return lst


def partition(lst, l, r, method):
    global comparasions

    comparasions += r - l - 1

    if method == 1:
        pivot_index = l
    elif method == 2:
        pivot_index = r-1
        swap(lst, pivot_index, l)
    else:
        pivot_index = median(lst, l, r)
        swap(lst, pivot_index, l)

    pivot = lst[l]
    i = l+1

    for j in range(l+1, r):
        if lst[j] < pivot:
            swap(lst, j, i)
            i += 1
    swap(lst, l, i-1)
    return i-1


def median(lst, l, r):
    a = lst[l]
    b = lst[r-1]
    c = lst[(l + r - 1) // 2]
    if c>a and c>b:
        if a>b:
            return l
        else:
            return r-1
    elif (c>a and c<b) or (c<a and c>b):
        return (l+r-1)//2
    else:
        if a>b:
            return r-1
        else:
            return l
    print(a,b,c)


def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]


with open("QuickSort.txt") as file:
    data = [int(i) for i in file.readlines()]


for i in range(1,4):
    comparasions = 0
    start_time = time.time()
    quick_sort(data.copy(), 0, len(data), i)
    print(f"Finished in {time.time() - start_time}s")
    print(comparasions)


