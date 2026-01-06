#condition do not alter the list given the list is already sorted 
def removeduplicate1(lis1):
    lis2=lis1.copy()
    j=-1
    t=0
    k=-1
    for m in range(len(lis1)):
        i=lis1[m]
        if j==i:
            lis2.pop(m)
            lis2.append(i)
        else:
            j=i
            continue
    print(lis2)
a=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
removeduplicate1(a)
