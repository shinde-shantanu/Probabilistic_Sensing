def dist(i, j, ti, tj): #function to measure heuristic values
    return abs(ti-i)+abs(tj-j) #Manhattan distance

def insert_fringe(i, j, fringe, f): #insertion into priority queue (Fringe)
    #print(fringe)
    if len(fringe)==0:
        fringe.append((i,j))
    else:
        for x in range(len(fringe)):
            (I,J)=fringe[x]
            if f[I][J]>f[i][j]:
                fringe.insert(x, (i,j))
                return
        fringe.append((i,j))

def a_star(dim, P, grid, si, sj, ti, tj):
    
    result=False
    
    g=[[-1 for i in range(dim)] for j in range(dim)] #data structure to store g(n) (list of lists). initialized with -1 for now
    g[si][sj]=0
    
    h=[[dist(i,j,ti,tj) for i in range(dim)] for j in range(dim)] #data structure to store h(n) (list of lists).
    
    f=[[-1 for i in range(dim)] for j in range(dim)] #data structure to store f(n) (list of lists). initialized with -1 for now
    f[si][sj]=g[si][sj]+h[si][sj]
    p=[[-1 for i in range(dim)] for j in range(dim)] #data structure to store pointers to parent (list of lists). initialized with -1 for now
    p[si][sj]=0
    
    fringe=[(si,sj)] #pushing the start node into the fringe
    
    while len(fringe)!=0:
        (i,j)=fringe.pop(0)
        if (i,j) == (ti,tj): #true if goal node is reached
            result=True
            break
        #print((i,j))
        if i-1 >= 0 and grid[i-1][j] != 4 and p[i-1][j]==-1 and p[i][j] != (i-1,j): #checking the chilren of each node popped from fringe
            p[i-1][j]=(i,j)
            g[i-1][j]=g[i][j]+1
            f[i-1][j]=g[i-1][j]+h[i-1][j]
            insert_fringe(i-1,j,fringe,f)
            
        if j+1 < dim and grid[i][j+1] != 4 and p[i][j+1]==-1 and p[i][j] != (i,j+1):
            p[i][j+1]=(i,j)
            g[i][j+1]=g[i][j]+1
            f[i][j+1]=g[i][j+1]+h[i][j+1]
            insert_fringe(i,j+1,fringe,f)
            
        if i+1 < dim and grid[i+1][j] != 4 and p[i+1][j]==-1 and p[i][j] != (i+1,j):
            p[i+1][j]=(i,j)
            g[i+1][j]=g[i][j]+1
            f[i+1][j]=g[i+1][j]+h[i+1][j]
            insert_fringe(i+1,j,fringe,f)
            
        if j-1 >= 0 and grid[i][j-1] != 4 and p[i][j-1]==-1 and p[i][j] != (i,j-1):
            p[i][j-1]=(i,j)
            g[i][j-1]=g[i][j]+1
            f[i][j-1]=g[i][j-1]+h[i][j-1]
            insert_fringe(i,j-1,fringe,f)
    
    return(result, p)
