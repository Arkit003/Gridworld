from Gridworld.enviroment.gridworld import GridWorld
from Gridworld.enviroment.action import Action


class ValueIteration:
    def __init__(self,env:GridWorld):
        self.env=env
        self.grid = env.get_states()
        self.reward = env.reward
        self.actions = env.actions
        self.discount_factor = env.discount_factor
        self.V = [[0 for _ in range(env.cols)] for  _ in range(env.rows)]
        self.threshold = 0.001


    def updating_state_values(self):
        rows=len(self.grid)
        cols=len(self.grid[0])
        no_iter=0
        while True:
            delta = 0
            for i in range(rows):
                for j in range(cols):
                    if self.env.is_terminal(i,j):
                        continue

                    action_values= []
                    old_value= self.V[i][j]
                    for action in self.actions:
                        next_state,reward = self.env.step((i,j),action)
                        value = reward + (self.discount_factor * self.V[next_state[0]][next_state[1]])
                        action_values.append(value)
                    self.V[i][j]=max(action_values)
                    new_value=self.V[i][j]
                    delta = max(delta,abs(old_value-new_value))
            #visualization
            for row in self.V:
                print(row)
            print("\n")   
            no_iter+=1 #no of iteration taken to converges

            #chcking if the values converges
            if delta<self.threshold:
                break
        return self.V,no_iter
            
    def print_v(self):
        print("Converged State Value:\n")
        for i in range(self.env.rows):
            for j in range(self.env.cols):
                print(self.V[i][j],end=" ")
            print("\n")
    
            
        