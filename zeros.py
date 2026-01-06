#def zero11(zero1):
'''    zero2=zero1.copy()
    first =0
    last=-1
    count1=0
    for i in zero2:
        if i>0:
            count1+=1
    while 1:
        if zero2[last] == 0:
            last-=1
        elif zero2[first] == 0 and zero2[last] !=0:
            zero2[first],zero2[last] = zero2[last],zero2[first]
            first+=1
            last-=1
        elif zero2[first] > 0:
            first+=1
        if count1 == first:
            break
    print(zero2)'''

def zero11(zero1):
    zero2=zero1.copy()
    i = 0
    j = 1
    for m in range(len(zero2)):
        if zero2[j] == 0:
            j+=1
        elif zero2[i] > 0:
            i += 1
        elif zero2[i] == 0 and zero2[j] !=0:
            zero2[i],zero2[j]=zero2[j],zero2[i]

    print(zero2)
        
a=[1,0,4,0,0,5,0,6,0,2]
zero11(a)