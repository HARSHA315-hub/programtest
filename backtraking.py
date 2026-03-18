"""n = 3
l = [1,2,3]
r = []
def back(start,current):
    r.append(current[:])
    for i in range(start,n):
        current.append(l[i])
        back(i+1,current)
        current.pop()
back(0,[])
print(r)
maze = [[0,0,0,1],
        [0,1,0,1],
        [0,1,0,1],
        [0,1,0,0]]
n = len(maze)
m = len(maze[0])
sol = [[0 for _ in range(m)] for _ in range(n)]
def safe(x,y):
    if x < 0 or x > n-1 or y < 0 or y > m-1 or maze[x][y] == 1 or sol[x][y] == 1:
        return False
    return True
def back(x,y):
    if x == n-1 and y == m-1 and sol[x][y] == 0:
        sol[x][y] = 1
        return True
    if safe(x,y):
        sol[x][y] = 1
        if back(x+1,y):
            return True
        if back(x,y+1):
            return True
        if back(x-1,y):
            return True
        if back(x,y-1):
            return True
        sol[x][y] = 0
    return False
back(0,0)
for i in sol:   
    print(*i)"""
