from Gridworld.enviroment.action import Action
from Gridworld.enviroment.gridworld import GridWorld

class PolicyEvalutaion:
    def __init__(self,policy:float,action:Action,env:GridWorld,threshold:float):
        self.policy=policy
        self.actions = action
        self.env = env
        self.threshold = threshold
        self.V = [[0 for _ in range(env.cols)] for _ in range(env.rows)]

    def updating_state_values(self):
        
        grid = [[0 for _ in range(self.env.cols)] for _ in range(self.env.rows)]
        while True:
            delta = 0
            for i in range(self.env.rows):
                for j in range(self.env.cols):

                    if self.env.is_terminal(i,j):
                        continue
                    
                    value=0
                    for action in self.actions.get_actions():
                        next_state,reward = self.env.step((i,j),action)
                        value += self.policy*(reward +(self.env.discount_factor*self.V[next_state[0]][next_state[1]]))
                        
                    delta=max(delta,abs(self.V[i][j]-value))
                    grid[i][j]=value
            self.V = grid
            #visualization
            for row in self.V:
                print(f"{row}")
            print("\n")   
            # no_iter+=1 #no of iteration taken to converges

            if delta<self.threshold:
                break
        return self.V

                
    def print_v(self):
        print("Converged State Value:\n")
        for i in range(self.env.rows):
            for j in range(self.env.cols):
                print(self.V[i][j],end=" ")
            print("\n")
    