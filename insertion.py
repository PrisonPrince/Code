def sort(list):
    for i in range(1,len(list)):
        j = i
        while list[j-1] > list[j] and j> 0:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1




list = [10,7,4,32,34,6]
sort(list)
print(list)
