from itertools import permutations
l = ["A","B","C"]
for i in permutations(l):
    print("".join(i))