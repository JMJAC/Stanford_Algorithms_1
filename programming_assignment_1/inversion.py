def inversions(lst, count=0):
    if len(lst) == 1 or len(lst) == 0:
        return lst, 0
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[::-1], 1
        return lst, 0

    left_lst = lst[:len(lst) // 2]
    right_lst = lst[len(lst) // 2:]

    left_lst, count_l = inversions(left_lst, count)
    right_lst, count_r = inversions(right_lst, count)
    split_lst,count_s = inversions_split(left_lst, right_lst)
    count = count_l + count_r+count_s
    return split_lst, count


def inversions_split(left_lst, right_lst):
    i = 0
    j = 0
    count = 0
    split_lst = []
    while i<len(left_lst) and j<len(right_lst):
        if left_lst[i] < right_lst[j]:
            split_lst.append(left_lst[i])
            i += 1
        else:
            count += len(left_lst)-i
            split_lst.append(right_lst[j])
            j += 1
    split_lst.extend(left_lst[i:])
    split_lst.extend(right_lst[j:])
    return split_lst, count

data = []
with open("data.txt") as file:
    for i in file:
        data.append(int(i))

print(inversions(data)[1])
