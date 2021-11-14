from Grid import examine
from Grid import gen_grid
from A_Star import a_star
import random
from Agent_6 import agent_6
from Agent_7 import agent_7
from Agent_8 import agent_8

dim = 50
grid,target = gen_grid(dim)
for x in grid:
    print(x)
print(target)
result, parent = a_star(dim,0.3,grid,0,0,target[0],target[1])
if result==False:
    print("Unsolvable grid")
else:
    print("Agent 8")
    result, i, j, move, exam, time = agent_8(grid, target, dim)
    print(i,j)
    print("Move: ", move)
    print("Exam: ", exam)
    print("Time: ", time)
    
    print("Agent 7")
    result, i, j, move, exam, time = agent_7(grid, target, dim)
    print(i,j)
    print("Move: ", move)
    print("Exam: ", exam)
    print("Time: ", time)
    
    print("Agent 6")
    result, i, j, move, exam, time = agent_6(grid, target, dim)
    print(i,j)
    print("Move: ", move)
    print("Exam: ", exam)
    print("Time: ", time)
