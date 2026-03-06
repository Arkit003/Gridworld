from Gridworld.enviroment.action import Action

class State:
    def __init__(self,row,cols,n_rows,n_cols,v):
        self.row = row
        self.col = cols
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.v = v
        

    def possible_actions(self,action:Action):
        actions = action.get_actions()
        return actions
    
