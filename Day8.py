"""
6

l = [4,7,1,9,3]
s = 0
m = l[0]
for i in range(len(l)):
    if l[i] > m:
        m = l[i]
        s = i
print(s)

7

s = "I Love Coding"
s = s.split()
print(" ".join(s[::-1]))

8

n = int(input())
for i in range(2,n//2 + 1):
    if n%i == 0:
        print("False")
        exit()
print("True")

9

l = [2,3,5,3,2]
x = 0
for i in l:
    x = x^i
print(x)

10


s = "I Enjoy Solving Coding Problems"
l = 0
m = 0
for i in s:
    if i != " ":
        l += 1
    else:
    
        if m < l:
            m = l
        l = 0
print(m)

"""