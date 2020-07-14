# Biggie Size
def biggie_size(list):
    for i in range (len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

# Count Positives
def count_positives(list):
    count = 0
    for i in range (len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list

# Sum Total
def sum_total(list):
    sum = 0
    for i in list:
        sum += i
    return sum

# Average
def average(list):
    return sum_total(list)/len(list)

# Length
def length(list):
    return len(list)

# Minimum
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for i in list:
            if min > i:
                min = i
        return min 
        
# Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for i in list:
            if max < i:
                max = i
        return max 

# Ultimate Analysis
def ult_analysis(list):
    obj = {
        "sumTotal" : sum_total(list),
        "average" : average(list),
        "minimum" : minimum(list),
        "maximum" : maximum(list)
    }
    return obj

# Reverse List
def reverse_list(list):
    for i in range (0, int(len(list)/2)):
        temp = list[i]
        list[i] =list[len(list)-i-1]
        list[len(list)-i-1] = temp
    return list

# print(biggie_size([-1,3,5,-5]))
# print(count_positives([-1,1,1,1]))
# print(count_positives([1,6,-4,-2,-7,-2]))
# print (sum_total([1,2,3,4]))
# print (sum_total([6,3,-2]))
# print (average([1,2,3,4]))
# print(length([37,2,1,-9]))
# print(length([]))
# print(minimum([37,2,1,-9]))
# print(minimum([]))
# print(maximum([37,2,1,-9]))
# print(maximum([]))
# print(ult_analysis([37,2,1,-9]))
# print(reverse_list([37,2,1,-9,10]))