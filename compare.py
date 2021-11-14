from Grid import examine
from Grid import gen_grid
from A_Star import a_star
import random
from Agent_6 import agent_6
from Agent_7 import agent_7

grid,target = gen_grid(10)
for x in grid:
    print(x)
print(target)
result, parent = a_star(10,0.3,grid,0,0,target[0],target[1])
if result!=False:
    result, i, j, move, exam = agent_6(grid, target, 10)
    print(target)
print(i,j)
for x in grid:
    print(x)
print("Move: ", move)
print("Exam: ", exam)


print("Agent 7")
result, i, j, move, exam = agent_7(grid, target, 10)
print(target)
print(i,j)
for x in grid:
    print(x)
print("Move: ", move)
print("Exam: ", exam)

