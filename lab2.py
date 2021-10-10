class Node:
    def InitialState():
        return(3,3,1,0,0,0)
    def state():
        return Node

    

GoalState = (0,0,0,3,3,1) 
treeStack = []
def DLS():
    return RecursiveDLS(Node.InitialState(), 15)


def RecursiveDLS(node, limit): #Returns failure, or curoff reached 
    if node == GoalState:
        return action #path to goal
    elif limit == 0:
        return "cutoff"
    else:
        cutoffOCcurred = False
        for action in ACTIONS(node):
            child = node[action]
            result = RecursiveDLS(child, limit-1)
        if result == "cutoff":
            cutoffOCcurred = True
        if cutoffOCcurred == True: 
            return "cutoff"
        else:
            return "failure"
            

def ACTIONS(node):
    possibleActions = []
    #5 actions: 1C, 1M, 2C, 2M, 1C 1M
    if(node[2]) == 1: #boat is at A
        possibleActions.append((node[0], node[1]-1, 0, node[3], node[4]+1, 1)) #1C
        possibleActions.append((node[0]-1, node[1], 0, node[3]+1, node[4], 1)) #1M
        possibleActions.append((node[0], node[1]-2, 0, node[3], node[4]+2, 1)) #2C
        possibleActions.append((node[0]-2, node[1], 0, node[3]+2, node[4], 1)) #2M
        possibleActions.append((node[0]-1, node[1]-1, 0, node[3]+1, node[4]+1, 1)) #1C1M
    else: #boat is at B
        possibleActions.append((node[0], node[1]+1, 1, node[3], node[4]-1, 0)) #1C
        possibleActions.append((node[0]+1, node[1], 1, node[3]-1, node[4], 0)) #1M
        possibleActions.append((node[0], node[1]+2, 1, node[3], node[4]-2, 0)) #2C
        possibleActions.append((node[0]+2, node[1], 1, node[3]-2, node[4], 0)) #2M
        possibleActions.append((node[0]+1, node[1]+1, 1, node[3]-1, node[4]-1, 0)) #1C1M
    return(possibleActions)

print(ACTIONS((2,2,0,1,1,1)))