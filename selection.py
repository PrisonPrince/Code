def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j


        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

list = [100,3435,23,43,42,13,34]
sort(list)
print(list)
