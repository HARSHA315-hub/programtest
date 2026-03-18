l1 = [1,3,5]
l2 = [2,4,6]
l3 = []
i = len(l1)-1
j = len(l2)-1
while i>-1 and j>-1:
    if l1[i] > l2[j]:
        l3.insert(0,l1[i])