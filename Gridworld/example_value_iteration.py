from Gridworld.enviroment.gridworld import GridWorld
from Gridworld.enviroment.action import Action
from Gridworld.algorithm.value_iteration import ValueIteration

if __name__ == "__main__":
    rows = 5
    cols = 5
    reward = -1
    action  = Action()
    env = GridWorld(rows,cols,action,1,(2,2),-1)
    algo = ValueIteration(env)
    V = algo.updating_state_values()
    algo.print_v()