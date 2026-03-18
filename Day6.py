"""
6

l = [4,7,1,9,3]
m = 0
for i in l:
    if i > m:
        m = i
print(m)

7

l = list(map(int,input("Enter the List: ").split()))
i = 0
j = len(l) - 1
while i <= j:
    if l[i] != l[j]:
        print("False")
        exit()
    else:
        i += 1
        j -= 1
print("True")

8

s = "leetcode"
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for n,m in d.items():
    if m == 1:
        print(n)
        break

9

l1 = [1,3,5]
l2 = [2,4,6]
l = l1+l2
l.sort()
print(l)

10

n = 9875
while len(str(n)) > 1:
    m = 0
    for i in str(n):
        m += int(i)
    n = m
print(n)

"""
