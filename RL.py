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
state_val_table_2= {
    'A':0,
    'B':0,
    'C':0,
    'D':100,
}

def probAction(state, action, policy):
    # probability of 
    return 3

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
    else:
            if(action == 1 and nextS == 'A'):
                prob = 0.9
            elif(action == 1 and nextS == 'D'):
                prob = 0.1
            if(action == 2 and nextS == 'D'):
                prob = 0.9
            elif(action == 2 and nextS == 'A'):
                prob = 0.1
    
    return prob

# reward_model[s][ transition_model[s][count] ]
def bellman_eq(policy, gamma):
    i = 0
    
    while i < 100:
        state_val_table['A'] = 0
        state_val_table['B'] = 0
        state_val_table['C'] = 0
        for s in states:
            count = 0
            for nextS in transition_model[s]:
                state_val_table[s] += policy[s][1] * (probSA(s,1,nextS) * (-10 + gamma * state_val_table_2[nextS]))
            count +=1
            for nextS in transition_model[s]:
                state_val_table[s] += policy[s][2] * (probSA(s,1,nextS) * (-10 + gamma * state_val_table_2[nextS]))
        for item in state_val_table:
            state_val_table_2[item] = state_val_table[item]
        i+=1
    

    
def next_state(state, action):
    probability = random.uniform(0,1)
    if(probability < 0.1): # 10% chance of going to opposite state of one chosen
        if (action == 1):
            action = 2
        else:
            action = 1

    return transition_model[state][action-1]
    


bellman_eq(policy1, 1)

print(state_val_table['A'])
print(state_val_table['B'])
print(state_val_table['C'])
print(state_val_table['D'])



