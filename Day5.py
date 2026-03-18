"""
6

l = [0,1,2,3]
n = len(l) + 1
s = 0
r = 0
for i in l:
    s += i
for i in range(n):
    r += i
print(abs(s-r))

7

l = [1,-2,3,-4,5]
i = 0
j = 0
n = len(l)-1
while j < n:
    if l[i] < 0:
        i += 1
        j = i+1
    elif l[j] > 0:
        j += 1
    else:
        l[i],l[j] = l[j],l[i]
        i = j
        j = i+1
print(l)

8

l = [7,1,5,3,6,4]
mn = l[0]
mx = 0
for i in l:
    if mn > i:
        mn = i
    p = i - mn
    if p > mx:
        mx = p
print(mx)

9

s = "sab"
t = "abs"
flag = 0
n = len(s)
if len(s) != len(t):
    print("False")
elif s == t:
    print("True")
else:
    for i in range(1,n+1):
        k = i%n
        if t == s[-k:] + s[:-k]:
            flag = 1
    if flag > 0:
        print("True")
    else:
        print("False")

10

n = 12345
c = 0
while n > 0:
    c += 1
    n //= 10
print(c)

"""