import random
policy1 = {
    'A': {1:1, 2:0},
    'B': {1:1, 2:0},
    'C': {1:1, 2:0},
    'D': {1:1, 2:0}
}

policy2 = {
    'A': {1:0, 2:1},
    'B': {1:0, 2:1},
    'C': {1:0, 2:1},
    'D': {1:0, 2:1}
}

policy3 = {
    'A': {1:0.4, 2:0.6},
    'B': {1:1, 2:0},
    'C': {1:0, 2:1},
    'D': {1:1, 2:0}

}

actions = [1,2]
states = ['A', 'B', 'C']
#r(s, a, s')
reward_model = {
    'A': {'B':-10, 'C':-10},
    'B': {'A':-10, 'D':-10},
    'C': {'A':-10, 'D':-10},
    'D': {'D':100}
}

transition_model = {
    'A':['B','C'],
    'B':['D','A'],
    'C':['A','D'],
    'D':['D','D']
}

state_val_table = {
    'A':0,
    'B':0,
    'C':0,
    'D':100
}
state_val_table_2 = {
    'A':0,
    'B':0,
    'C':0,
    'D':100,
}



def probSA(state, action, nextS):
    prob = 0
    if(state == 'A'):
        if(action == 1 and nextS == 'B'):
            prob = 0.9
        elif(action == 1 and nextS == 'C'):
            prob = 0.1
        if(action == 2 and nextS == 'C'):
            prob = 0.9
        elif(action == 2 and nextS == 'B'):
            prob = 0.1
    elif(state == 'B'):
            if(action == 2 and nextS == 'A'):
                prob = 0.9
            elif(action == 2 and nextS == 'D'):
                prob = 0.1
            if(action == 1 and nextS == 'D'):
                prob = 0.9
            elif(action == 1 and nextS == 'A'):
                prob = 0.1
    else: # state == C
            if(action == 1 and nextS == 'A'):
                prob = 0.9
            elif(action == 1 and nextS == 'D'):
                prob = 0.1
            if(action == 2 and nextS == 'D'):
                prob = 0.9
            elif(action == 2 and nextS == 'A'):
                prob = 0.1
    return prob



def rewardSA(state, nextS):
    reward = reward_model[state][nextS]
    return reward


def bellman_eq(policy, gamma):
    i = 0
    
    while i < 100:
        state_val_table['A'] = 0
        state_val_table['B'] = 0
        state_val_table['C'] = 0
        for s in states:
            for a in actions:
                for nextS in transition_model[s]:
                    state_val_table[s] += policy[s][a] * (probSA(s,a,nextS) * (rewardSA(s, nextS) + gamma * state_val_table_2[nextS]))
            
        for item in state_val_table:
            state_val_table_2[item] = state_val_table[item]
        i+=1

def solveStates(policy):
    bellman_eq(policy, 1)
    printStateVals()

def printStateVals():
    for i in state_val_table:
        print("Vpi(" + i + "): " + str(round(state_val_table[i], 2)))

print("==Policy 1== ")
solveStates(policy1)

print("\n==Policy 2== ")
solveStates(policy2)

print("\n==Policy 3== ")
solveStates(policy3)




