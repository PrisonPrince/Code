def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
pos = 1
def search(list, n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid  = (l + u) // 2
        if  list[mid] == n:
            return True
        elif list[mid] > n:
            u = mid - 1
        else:
            l = mid + 1
        globals()['pos'] = pos + 1
            



list = []
n  = int(input("enter the no. of elements: "))
for i in range(n):
    element = int(input("Enter the element:".format(i+1)))
    list.append(element)

print(list)
sort(list)
print(list)

a = int(input("Enter the element to be found: "))
if search(list, a):
    print("Found at", pos+1)
else:
    print("Not Found")
