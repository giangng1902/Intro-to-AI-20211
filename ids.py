import base

class Ids(base.ProblemSolver):
    def __init__(self):
        super().__init__()
        self.name = 'IDS'

    def dls(self, limit):
        self.ctime = 0
        self.cspace = 0
        def limited_depth(current, parent, cost, limit, space):
            self.trace[(current, cost)] = parent
            self.ctime += 1
            self.cspace = max(self.cspace, space)
            if cost > limit:
                return None
            if current == base.goal:
                return cost
            state_list = base.find_next_states(current)
            for next in base.find_next_states(current):
                if next != parent and base.valid_state(next):
                    result = limited_depth(next, current, cost + 1, limit, space + len(state_list) + 1)
                    if result != None:
                        return result
        return limited_depth(base.initial_state, None, 0, limit, 1)

    def run(self):
        time = space = 0
        result = 0
        while True:
            self.trace = {}
            stop = self.dls(result)
            time += self.ctime
            space = max(space, self.cspace)
            if stop != None:
                break
            result += 1
        self.time.append(time)
        self.space.append(space)
        self.result.append(result)
    
    def trace_back(self):
        l = []
        def find_pre_state(state):
            pre_state = self.trace.get(state, None)
            if pre_state != None:
                find_pre_state((pre_state, state[1] - 1))
            l.append(state[0])
        find_pre_state((base.goal, self.result[0]))
        return l