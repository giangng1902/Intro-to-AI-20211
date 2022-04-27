import base

class Idastar(base.ProblemSolver):
    def __init__(self):
        super().__init__()
        self.name = 'IDA*'

    def heuristic(self, current_state):
        if 'Sheperd' in current_state:
            h_value = (len(current_state) // 2) * 2 - 1
        else:
            h_value = ((len(current_state) + 1) // 2) * 2
        return int(h_value)

    def dfs(self, bound):
        self.ctime = 0
        self.cspace = 0
        self.cresult = None
        def search(node, parent, g, bound, space):
            self.trace[(node, g)] = parent
            self.ctime += 1
            self.cspace = max(self.cspace, space)
            f = g + self.heuristic(node)
            if f > bound:
                return f
            if node == base.goal:
                self.cresult = g
                return
            new_bound = float('inf')
            state_list = base.find_next_states(node)
            state_list.sort(key=lambda x : self.heuristic(x))
            for next_node in state_list:
                if next_node != parent and base.valid_state(next_node):
                    t = search(next_node, node, g + 1, bound, space + len(state_list) + 1)
                    if self.cresult != None:
                        return
                    new_bound = min(new_bound, t)
            return new_bound
        return search(base.initial_state, None, 0, bound, 1)

    def run(self):
        time = space = 0
        bound = self.heuristic(base.initial_state)
        while True:
            self.trace = {}
            t = self.dfs(bound)
            time += self.ctime
            space = max(space, self.cspace)
            if self.cresult != None:
                break
            bound = t
        self.time.append(time)
        self.space.append(space)
        self.result.append(self.cresult)

    def trace_back(self):
        l = []
        def find_pre_state(state):
            pre_state = self.trace.get(state, None)
            if pre_state != None:
                find_pre_state((pre_state, state[1] - 1))
            l.append(state[0])
        find_pre_state((base.goal, self.result[0]))
        return l