import random

dim=5

def gen_grid(dim):

    s=[]
    for i in range(dim):
        for j in range(dim):
            if (i,j) == (0,0):
                continue
            else:
                s.append((i,j))
    
    k = int(0.3 * ((dim * dim)-1))
    blocked = random.sample(s,k)
    
    s = list(set(s) - set(blocked))
    s.append((0,0))

    target = random.sample(s,1)
    
    nf = int(len(s)/3)
    nh = nf
    
    flat = random.sample(s,nf)
    s = list(set(s) - set(flat))
    
    hilly = random.sample(s,nh)
    s = list(set(s) - set(hilly))
    
    thick = s
    
    grid = [[3 for i in range(dim)] for j in range(dim)]
    
    for x in blocked:
        grid[x[0]][x[1]] = 4
    
    for x in flat:
        grid[x[0]][x[1]] = 1
    
    for x in hilly:
        grid[x[0]][x[1]] = 2
    
    return(grid,target[0])

def examine(cell, target):
    if target == 0:
        return 0
    if cell == 1:
        s = [1,1,1,1,1,1,1,1,0,0]
        if random.sample(s,1)==[1]:
            return 1
    if cell == 2:
        s = [1,1,1,1,1,0,0,0,0,0]
        if random.sample(s,1)==[1]:
            return 1
    if cell == 3:
        s = [1,1,0,0,0,0,0,0,0,0]
        if random.sample(s,1)==[1]:
            return 1
    return 0
