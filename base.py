import random
from math import inf
from statistics import mean

objects = ['Shepherd', 'Wolf', 'Goat', 'Cabbage', 'Stick', 'Torch']
conflicts = [('Wolf', 'Goat'), ('Goat', 'Cabbage'), ('Wolf', 'Stick'), ('Stick', 'Torch')]

initial_state = ('Cabbage', 'Goat', 'Shepherd', 'Stick', 'Torch', 'Wolf')
goal = ()

shuffle_states = False
next_states = {}

def find_next_states(x : tuple):
    if shuffle_states:
        return next_states[x]
    x = list(x)
    states = []
    if 'Shepherd' in x:
        x.remove('Shepherd')
        states.append(tuple(x))
        for i in range(len(x)):
            tmp = x[:]; tmp.pop(i)
            states.append(tuple(tmp))
            for j in range(i, len(tmp)):
                tmp2 = tmp[:]; tmp2.pop(j)
                states.append(tuple(tmp2))
    else:
        x.append('Shepherd'); x.sort()
        states.append(tuple(x))
        for i in range(len(objects)):
            if objects[i] not in x:
                tmp = x[:]; tmp.append(objects[i]); tmp.sort()
                states.append(tuple(tmp))
                for j in range(i + 1, len(objects)):
                    if objects[j] not in x:
                        tmp2 = tmp[:]; tmp2.append(objects[j]); tmp2.sort()
                        states.append(tuple(tmp2))
    return states

def valid_state(x : tuple):
    for conflict in conflicts:
        if (conflict[0] in x and conflict[1] in x and 'Shepherd' not in x) or (conflict[0] not in x and conflict[1] not in x and 'Shepherd' in x):
            return False
    return True

def random_all_next_states(state):
    l = find_next_states(state)
    random.shuffle(l)
    next_states[state] = l
    for next_state in l:
        if next_state not in next_states:
            random_all_next_states(next_state)

class ProblemSolver:
    def __init__(self):
        self.name = ''
        self.maxTime = self.maxSpace = 0
        self.minTime = self.minSpace = inf
        self.time = []
        self.space = []
        self.result = []
        self.trace = {}
    
    def run(self):
        pass

    def solve(self):
        self.run()
        self.maxTime = max(self.maxTime, self.time[-1])
        self.maxSpace = max(self.maxSpace, self.space[-1])
        self.minTime = min(self.minTime, self.time[-1])
        self.minSpace = min(self.minSpace, self.space[-1])

    def trace_back(self):
        l = []
        def find_pre_state(state):
            pre_state = self.trace.get(state, None)
            if pre_state != None:
                find_pre_state(pre_state)
            l.append(state)
        find_pre_state(goal)
        return l
    
    def get_max_time(self):
        return self.maxTime
    
    def get_min_time(self):
        return self.minTime
    
    def get_max_space(self):
        return self.maxSpace

    def get_min_space(self):
        return self.minSpace
    
    def get_avg_time(self):
        return mean(self.time)
    
    def get_avg_space(self):
        return mean(self.space)