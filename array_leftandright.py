def left1(n,list1):
    list2=list1.copy()
    for i in range(n):
        list2.append(list2[0])
        list2.remove(list2[0])
    print(list2)
def right1(n,list1):
    list2=list1.copy()
    for i in range(n):
        list2.insert(0,list2[-1])
        list2.pop(-1)
    print(list2)
number = 2
lis1=[1,2,3,4,5]
left1(number,lis1)
right1(number,lis1)