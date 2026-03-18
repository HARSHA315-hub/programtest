"""
6

class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        n = x
        x = abs(x)
        c = 2**31
        while x > 0:
            r = r*10
            m = x%10
            x = x//10
            r += m
        if c < r or -c > r:
            return 0
        elif n >= 0:
            return r
        else:
            return -r

8

n = [1,3,5,4,7,8,9]
c = 1
m = 0
for i in range(1,len(n)):
    if n[i] > n[i-1]:
        c += 1
    else:
        c = 1
    m = max(c,m)
print(m)

9

l = [1,2,2,2,3,4]
tar = 2
def first(l,tar):
    low = 0
    high = len(l) - 1
    res = -1
    while low <= high:
        mid = (low + high)//2
        if l[mid] == tar:
            res = mid
            high = mid-1
        elif l[mid] > tar:
            high = mid - 1
        else:
            low = mid + 1
    return res


def last(l,tar):
    low = 0
    high = len(l) - 1
    res = -1
    while low <= high:
        mid = (low + high)//2
        if l[mid] == tar:
            res = mid
            low = mid+1
        elif l[mid] > tar:
            high = mid-1
        else:
            low = mid+1
    return res
print(abs(first(l,tar) - last(l,tar))+1)

10

n = int(input("Enter the number: "))
m = 1
f = 0
while n > 0:
    n -= m
    m += 2
    if n == 0:
        f += 1
if f > 0:
    print("Perfect Square")
else:
    print("Not A Perfect Square")

"""