"""
6
l = [5,3,8,1,9]
m = l[0]
for i in l:
    if m > i:
        m = i
print(m)

7

o = 0
e = 0
l = [1,2,3,4,5,6]
for i in l:
    if i%2 == 0:
        e += 1
    else:
        o += 1
print("Even:",e)
print("Odd:",o)

8

s1 = "listen"
s2 = "silent"
if len(s1) != len(s2):
    print("False")
else:
    for i in s1:
        if s1.count(i) != s2.count(i):
            print("False")
            exit()
    print("True")

9

l = [1,2,3,2,4,2]
r = 2
i = 0
while i < len(l):
    if l[i] == r:
        l.pop(i)
    else:
        i += 1
print(l)

10

l = [7,2,5,1,9]
l.remove(min(l))
print(min(l))

(or)

l = [7,2,5,1,9]
l.sort()
print(l[1])

"""
