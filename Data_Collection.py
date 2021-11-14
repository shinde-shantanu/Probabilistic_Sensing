from Grid import gen_grid
from A_Star import a_star
from Agent_6 import agent_6
from Agent_7 import agent_7
from Agent_8 import agent_8
import pandas as pd

df = pd.DataFrame(columns=['Target Type',
                           'Moves 6',
                           'Moves 7',
                           'Moves 8',
                           'Examine 6',
                           'Examine 7',
                           'Examine 8',
                           'Run Time 6',
                           'Run Time 7',
                           'Run Time 8'])

c = 0
dim = 50

while c <= 100:
    grid,target = gen_grid(dim)
    result, parent = a_star(dim,0.3,grid,0,0,target[0],target[1])
    if result==False:
        continue
    else:
        result, i, j, move8, exam8, time8 = agent_8(grid, target, dim)
        result, i, j, move7, exam7, time7 = agent_7(grid, target, dim)
        result, i, j, move6, exam6, time6 = agent_6(grid, target, dim)
        if move8 < move7 and move8 < move6:
            df1 = pd.DataFrame([[grid[target[0]][target[1]],move6,move7,move8,exam6,exam7,exam8,time6,time7,time8]],columns=['Target Type','Moves 6','Moves 7','Moves 8','Examine 6','Examine 7','Examine 8','Run Time 6','Run Time 7','Run Time 8'])
            df = pd.concat([df,df1])
            c = c + 1
            df.to_csv('data.csv')
