import numpy as np

from gridworld.gridworld.action import Action

class GridWorld:
    def __init__(self,rows,cols) -> None:
        self.rows =rows
        self.cols = cols
        self.terminal_state_start=(0,0)
        self.terminal_state_end = (-1,-1)
        self.reward = -1
        self.policy = 0.25

    def is_terminal(self,row,cols):
        out = self.terminal_state_start == (row,cols) or self.terminal_state_end=(rows,cols)
        return out 

    def initial_state(self)->np.array:
        arr=np.zeros((self.rows,self.cols))
        return arr
    
    def possible_actions(self,state):
        pass

    def next_state(self,state,action):
        state = 1/self.policy()

