def arr1(arr):
 n=len(arr)
 i,j=0,0
 while i<n:
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=1
    else:
        i+=1
 print(arr)
arr=eval(input("Enter The Array:"))
arr1(arr)