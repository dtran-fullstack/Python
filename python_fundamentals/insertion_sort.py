def insertion_sort(list):
    for i in range (1,len(list)):
        index = i
        for j in range (i-1, -1, -1):
            if (list[index] < list[j]):
                list[index], list[j] = list[j], list[index]
                index = j
    return list

print(insertion_sort([9,3,78,12,76,0,-2]))