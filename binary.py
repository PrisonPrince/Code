pos = 1
def search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            return True
        elif list[mid] > n:
            u = mid - 1
        else:
            l = mid + 1
        globals()['pos'] = pos + 1



list = []
n  = int(input("Enter no. of elements to be added in list: "))
for i in range(n):
    element = int(input("Enter the element to be added: ".format(i+1)))
    list.append(element)
print(list)
a = int(input("Enter the element  to be searched: " ))
if search(list,  a):
    print("Found at", pos + 1)
else:
    print("Not Found")
