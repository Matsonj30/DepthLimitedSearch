class Node:
    def InitialState():
        return(3,3,1,0,0,0)
    def state():
        return Node

def DLS():
    return RecursiveDLS(Node.InitialState(), 15)


def RecursiveDLS(CurrentNode, limit): #Returns failure, or cutoff reached 
    #print(CurrentNode)
    if CurrentNode == (0,0,0,3,3,1):
        return "goal" #path to goal
    elif limit == 0:
        return "cutoff"
    else:
        cutoffOccurred = False
        for possibleNode in ACTIONS(CurrentNode):
            result = RecursiveDLS(possibleNode, limit-1) 
            if result == "cutoff":
                cutoffOccurred = True
            elif result != "failure":
                print("At the current " + str(CurrentNode) + " you take the action ", end='')
                actionString(CurrentNode, possibleNode)
                print("to get to " + str(possibleNode), end='')
                if(possibleNode == (0,0,0,3,3,1)):
                    print("(GOAL)")
                else:
                    print("")
                return result
        if cutoffOccurred == True: 
             return "cutoff"
        else:
            return "failure"
            

def actionString(currentNode, possibleNode):
    action = []
    for number in range(6):
       action.append(possibleNode[number] - currentNode[number])

    if (action[0] < 0 and action[1] < 0): # moving missionaries and cannibals
       print("<MOVE " + str(abs(action[0])) + " missionary and " + str(abs(action[1])) + " cannibals", end='')
    elif (action[3] < 0 and action[4] < 0): # moving missionaries and cannibals
        print("<MOVE " + str(abs(action[3])) + " missionary and " + str(abs(action[4])) + " cannibals", end='')
    else:     
        if(action[0] < 0): #missionaries being moved over
            print("<MOVE " + str(abs(action[0])) + " missionaries", end='')
        if(action[1] < 0):
            print("<MOVE " + str(abs(action[1])) + " cannibals", end='')
        if(action[3] < 0):
            print("<MOVE " + str(abs(action[0])) + " missionaries", end='')
        if(action[4] < 0):
            print("<MOVE " + str(abs(action[1])) + " cannibals", end='')
    if(action[2] < 0):
        print(" FROM sideA TO sideB> ", end='')
    else:
        print(" FROM sideB TO sideA> ", end='')
    

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

DLS()
