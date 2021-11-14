from Grid import examine
from A_Star import a_star
import random
import timeit

def update_probability(p, pxy, fnr, dim): #Function to update probability for all Pi,j
    d = (1-pxy) + (pxy * fnr)
    for x in range(dim):
        for y in range(dim):
            p[x][y] = p[x][y] / d

def update_find_probability(pc, pf, dis, f, h, t, ud, dim):
    fnr = [0,0.8,0.5,0.2]
    if ud != 0:
        fnr[0] = ((f * 0.8) + (h * 0.5) + (t * 0.2)) / ud
    for x in range(dim):
        for y in range(dim):
            if dis[x][y] == 4:
                pf[x][y] = 0
            else:
                pf[x][y] = pc[x][y] * fnr[dis[x][y]]

def update_probability_block(p, pxy, b):
    for x in range(dim):
        for y in range(dim):
            p[x][y] = p[x][y] / (1-pxy)

def dist(i, j, ti, tj): #Finds Manhattan distance for (i,j) with respect to (ti,tj)
    return abs(ti-i)+abs(tj-j)

def find_path(parent, ti, tj, si, sj): #Return list of tuples ass path
    i,j = ti, tj
    path = [(ti, tj)]
    while (i, j) != (si, sj):
        path.insert(0, parent[i][j])
        (i, j) = parent[i][j]
    return(path)

def agent_7(grid, target, dim):
    
    start = timeit.default_timer() #recording time stamp to measure run time
    
    nb = int(0.3 * ((dim * dim)-1))
    nf = int(((dim*dim)-nb)/3)
    nh = nf
    nt = (dim*dim) - nb - nf - nh
    ndis = 0
    cdis = [dim*dim, 0, 0, 0, 0]
    
    dis = [[0 for i in range(dim)] for j in range(dim)] #Discovered gridworld initialized to 0
    pi = 1/(dim*dim)
    pc = [[pi for i in range(dim)] for j in range(dim)] #Pi,j initilized to a constant value for all
    pf = [[0 for i in range(dim)] for j in range(dim)]
    update_find_probability(pc, pf, dis, nf-cdis[1], nh-cdis[2], nt-cdis[3], cdis[0], dim)
    
    i,j = 0,0 #i,j represents current position of agent. Starts at 0,0
    dis[0][0] = grid[0][0]
    cdis[dis[0][0]] = cdis[dis[0][0]] + 1
    cdis[0] = cdis[0] - 1
    ndis = 1
    update_find_probability(pc, pf, dis, nf-cdis[1], nh-cdis[2], nt-cdis[3], cdis[0], dim)
    
    move = 0
    exam = 0
    
    while True:

        flag = 0
        while flag==0: #Finding the cell having the maximum probability of finding the target
            
            flag = 1
            mp = max([max(x) for x in pf]) #Finding value of maximum probaility
            max_con = []
            for x in range(dim):
                for y in range(dim):
                    if pf[x][y] == mp:
                        max_con.append((x,y)) #List of cells having Pi,j equal to maximum probability
            if len(max_con)>1: #If there are more than 1 cells with maximum probability
                h = [[dist(x,y,i,j) for y in range(dim)] for x in range(dim)] #Finding Manhattan distances
                (ni,nj) = max_con[0]
                ndist = h[ni][nj]
                for (x,y) in max_con:
                    if h[x][y]<ndist:
                        (ni,nj) = (x,y)
                        ndist = h[x][y] #Finding the cells with minimum distance
                min_dist=[]
                for (x,y) in max_con:
                    if h[x][y]==ndist:
                        min_dist.append((x,y)) #List of cells with minimum distance
                
                if len(min_dist)>1:
                    (ni,nj) = random.sample(min_dist,1)[0] #randomly picking
                else:
                    (ni,nj) = min_dist[0]
            else:
                (ni,nj) = max_con[0]
            
            while True: #Planning path and traversing to next node
                
                result, parent = a_star(dim, 0.3, grid, i, j, ni, nj) #Finding path to maximum probability cell
                if result == False: #No path to maximum probaility cell
                    pc[ni][nj]=0 #Make probability 0
                    update_find_probability(pc, pf, dis, nf-cdis[1], nh-cdis[2], nt-cdis[3], cdis[0], dim)
                    flag = 0
                    break #Maximum probability node not reachable. Need to find next most feasible node.
                
                path = find_path(parent, ni, nj, i, j) #Finding path to maximum probabilty cell
                for (x,y) in path: #Traversing the found path
                    dis[x][y]=grid[x][y] #Updating the discovered matrix
                    cdis[dis[x][y]] = cdis[dis[x][y]] + 1
                    cdis[0] = cdis[0] - 1
                    ndis = ndis + 1
                    if dis[x][y]==4: #Planned path has a blocked node
                        b = b + 1
                        update_probability_block(pc, pc[x][y], b)
                        pc[x][y] = 0
                        update_find_probability(pc, pf, dis, nf-cdis[1], nh-cdis[2], nt-cdis[3], cdis[0], dim)
                        break
                    update_find_probability(pc, pf, dis, nf-cdis[1], nh-cdis[2], nt-cdis[3], cdis[0], dim)
                    move = move + 1 #Updating count of movements
                    (i,j)=(x,y)
                if (x,y)==(ni,nj): #Agent reached to maximum probability node
                    break
        
        #print(i,j)
        dis[i][j] = grid[i][j] #updating the discovered matrix
        
        if target == (i,j):
            t = 1
        else:
            t = 0
        exam = exam + 1 #Updating count of examinations
        if examine(grid[i][j],t) == 1: #Examining the current cell
            return(True, i, j, move, exam, timeit.default_timer() - start) #Termination
        
        if dis[i][j] == 1:
            fnr = 0.2
        elif dis[i][j] == 2:
            fnr = 0.5
        else:
            fnr = 0.8
        update_probability(pc, pc[i][j], fnr, dim)
        pc[i][j] = pc[i][j] * fnr
        update_find_probability(pc, pf, dis, nf-cdis[1], nh-cdis[2], nt-cdis[3], cdis[0], dim)
        
        

##grid,target = gen_grid(3)
##for x in grid:
##    print(x)
##print(target)
##result, parent = a_star(3,0.3,grid,0,0,target[0],target[1])
##if result!=Fsssalse:
##    result, i, j, move, exam = agent_7(grid, target, 3)
##    print(target)
##print(i,j)
##for x in grid:
##    print(x)
##print("Move: ", move)
##print("Exam: ", exam)
