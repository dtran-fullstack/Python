def selection_sort(list):
    for i in range (len(list)):
        min_index = i
        for j in range (i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i] , list[min_index] = list[min_index], list[i]        
    return(list)

print(selection_sort([2,4,5,1,6,7,3,4,5,8]))