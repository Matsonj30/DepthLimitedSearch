GoalState = (0,0,0,3,3,1) 
def DFS():
    InitialState = (3,3,1,0,0,0)
    return RecursiveDFS(Make-Node(InitialState))


def RecursiveDFS(node, limit):
    if node == GoalState:
        return action #path to goal
    elif limit == 0:
        return "cutoff reached"
    else:
        
