import numpy as np

from Gridworld.enviroment.action import Action

class GridWorld:
    def __init__(self,rows:int,cols:int,action:Action,discount_factor:float=1,terminal_state:tuple=(0,0),reward:int=-1) -> None:
        self.rows =rows
        self.cols = cols
        self.terminal_state_start=terminal_state
        self.reward = reward
        self.discount_factor = discount_factor
        self.actions = action.get_actions()
        self.grid = []
        


    def is_terminal(self,row,col)->bool:
        return  self.terminal_state_start == (row,col)

    def step(self,state:tuple,action:str):
        row,col = state
        if self.is_terminal(row,col):
            self.reward=0
            return state,self.reward

        direction = self.actions[action]
        next_row = row+direction[0] if row + direction[0]>=0 and row + direction[0]<self.rows else row
        next_col = col+direction[1] if col + direction[1]>=0 and col + direction[1]<self.cols else col

        next_state = next_row,next_col
        return next_state,self.reward

    def get_states(self):
        grid=[]
        for i in range(self.rows):
            m=[]
            for j in range(self.cols):
                m.append((i,j))
                print((i,j),end=" ")
            grid.append(m)
            print("\n")
        return grid
            
    
# if __name__ == "__main__":
#     row = 4
#     col=4
#     action = Action()
#     grid = GridWorld(row,col,action,1)
#     print(grid.step((1,1),"up"))
#     # grid.get_states()
#     print(grid.step((0,0),"up"))
#     print(grid.step((0,0),"left"))
#     print(grid.step((3,3),"down"))






