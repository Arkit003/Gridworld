from Gridworld.algorithm.policy_evaluation import PolicyEvalutaion
from Gridworld.enviroment.action import Action
from Gridworld.enviroment.gridworld import GridWorld

if __name__=="__main__":

    rows = 4
    cols =4
    gamma = 1
    terminal_state=(0,0)
    reward = -1
    policy =0.25
    threshold = 1
    action = Action()
    env= GridWorld(rows,cols,action,gamma,terminal_state,reward)

    evaluation = PolicyEvalutaion(policy,action,env,threshold)
    evaluation.updating_state_values()