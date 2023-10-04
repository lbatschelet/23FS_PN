def list_threshold(lst, threshold):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    check = sum < threshold
    return check


my_list = range(0, 11)

print(list_threshold(my_list, 3))
