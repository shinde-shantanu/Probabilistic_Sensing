from A_Star import a_star
from Grid import gen_grid

grid,target = gen_grid(10)
for x in grid:
    print(x)

print(target)

result, p = a_star(10, 0.3, grid, 0, 0, target[0], target[1])
print(result)
for x in p:
    print(x)

def find_path(parent, ti, tj, si, sj): #used to find the path from the parent data structure
    i,j = ti, tj
    path = [(ti, tj)]
    while (i, j) != (si, sj):
        #print(path)
        path.insert(0, parent[i][j])
        (i, j) = parent[i][j]
    return(path)

print(find_path(p, target[0], target[1], 0, 0))
