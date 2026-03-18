"""
6
l = [1,2,2,3,4,4,5]
s = []
for i in l:
    if i not in s:
        s.append(i)
print(s)

7

l = [1,2,3,4,5,6,7]
k = 3
m = l[:k][::-1] + l[k:][::-1]
print(m[::-1])

8

def gcd(a,b):
    while b != 0:
        a , b = b , a%b
    return a
print(gcd(5,15))

9

s = "programming"
val = "AEIOUaeiou"
v = 0 
c = 0
for i in s:
    if i.isalpha():
        if i in val:
            v += 1
        else:
            c += 1
print("Vowel:",v,"Consonants:",c)

10

l = ("I love solving algorithm problems").split()
m = ""
for i in l:
    if len(m) < len(i):
        m = i
print(m)

l = [1,2,3,4,5,6,7]
k = 3
for _ in range(k):
    l.insert(0,l[-1])
    l.pop()
print(l)

extra

l = [1,2,3,4,5]
k = 3
k = k % len(l)
l1 = l[k:]+l[:k]
l2 = l[-k:]+l[:-k]
print(l)
print(l1)
print(l2)
tar = 2
f = 0
le = 0
r = 0
for i in range(len(l)):
    if l[i] == tar:
        f = i
        break
for i in range(len(l)):
    if l1[i] == tar:
        le = i
        break
for i in range(len(l)):
    if l2[i] == tar:
        r = i
print(le,f,r)
"""