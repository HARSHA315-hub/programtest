def unique1(lis1):
    for i in lis1:
        temp=lis1.count(i)
        if temp == 1:
            print(i)
            break
a=[1,3,4,5,5,5,3,3,1,1,1,2]
unique1(a)