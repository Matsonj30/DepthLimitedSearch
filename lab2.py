class Node:
    def InitialState():
        return(3,3,1,0,0,0)
    def state():
        return Node

def DLS():
    return RecursiveDLS(Node.InitialState(), 11)


def RecursiveDLS(CurrentNode, limit): #Returns failure, or cutoff reached 
    #print(CurrentNode)
    if CurrentNode == (0,0,0,3,3,1):
        return "We did eet?" #path to goal
    elif limit == 0:
        return "cutoff"
    else:
        cutoffOccurred = False
        for possibleNode in ACTIONS(CurrentNode):
            result = RecursiveDLS(possibleNode, limit-1) ##understand recursive method HERE and waht it means to make result = recursive call
        if result == "cutoff":
            cutoffOccurred = True
        elif result != "failure":
            print("At the current " + str(CurrentNode) + " you take the action to get to " + str(possibleNode))
            return "gay"
        if cutoffOccurred == True: 
            return "cutoff"
        else:
            return "failure"
            

def ACTIONS(node):
    possibleActions = []
    #5 actions: 1C, 1M, 2C, 2M, 1C 1M
    if(node[2]) == 1: #boat is at A
        possibleActions.append((node[0], node[1]-1, 0, node[3], node[4]+1, 1)) #1C
        possibleActions.append((node[0]-1, node[1], 0, node[3]+1, node[4], 1)) #1M
        if(node[1] >= 2):  #make sure there are sufficient people to send over
            possibleActions.append((node[0], node[1]-2, 0, node[3], node[4]+2, 1)) #2C
        if(node[0] >= 2):
            possibleActions.append((node[0]-2, node[1], 0, node[3]+2, node[4], 1)) #2M
            possibleActions.append((node[0]-1, node[1]-1, 0, node[3]+1, node[4]+1, 1)) #1C1M

    else: #boat is at B
        possibleActions.append((node[0], node[1]+1, 1, node[3], node[4]-1, 0)) #1C
        possibleActions.append((node[0]+1, node[1], 1, node[3]-1, node[4], 0)) #1M
        if(node[4] >= 2): #make sure there are sufficient people to send over
            possibleActions.append((node[0], node[1]+2, 1, node[3], node[4]-2, 0)) #2C
        if(node[3] >= 2):
            possibleActions.append((node[0]+2, node[1], 1, node[3]-2, node[4], 0)) #2M
        possibleActions.append((node[0]+1, node[1]+1, 1, node[3]-1, node[4]-1, 0)) #1C1M
    return(findAcceptableStates(possibleActions))
    
## def findAcceptableStates(possibleActions)
#  determines which states given by ACTIONS() are acceptable
#  returns tuple of acceptable states
def findAcceptableStates(possibleActions):  
    acceptableStates = []
    for action in possibleActions:
        if(action[0] == 0 or action[0] >= action[1]): #checking for less cannibals at A
            if(action[3] == 0 or action[3] >= action[4]): #checking for less cannibals at B
                acceptableStates.append(action)
    return(acceptableStates)

#print(ACTIONS((3,1,1,0,2,1)))
DLS()