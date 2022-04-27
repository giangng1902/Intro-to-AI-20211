import base
import collections

class BfsTree(base.ProblemSolver):
    def __init__(self):
        super().__init__()
        self.name = 'BFS tree'

    def run(self):
        time = space = 0
        result = None
        queue = collections.deque()
        queue.append((base.initial_state, 0, None))
        self.trace = {(base.initial_state, 0): None}
        while len(queue) > 0:
            time += 1
            space = max(space, len(queue))
            current = queue.popleft()
            if current[0] == base.goal:
                result = current[1]
                break
            for state in base.find_next_states(current[0]):
                if not base.valid_state(state) or state == current[2]:
                    continue
                self.trace[(state, current[1] + 1)]= current[0]
                queue.append((state, current[1] + 1, current[0]))
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

class Bfs(base.ProblemSolver):
    def __init__(self):
        super().__init__()
        self.name = 'BFS'

    def run(self):
        time = space = 0
        visited = {base.initial_state}
        self.trace = {base.initial_state: None}
        result = None
        queue = collections.deque()
        queue.append((base.initial_state, 0))
        while len(queue) > 0:
            time += 1
            space = max(space, len(queue) + len(visited))
            current = queue.popleft()
            if current[0] == base.goal:
                result = current[1]
                break
            for state in base.find_next_states(current[0]):
                if (not base.valid_state(state)) or (state in visited):
                    continue
                visited.add(state)
                self.trace[state] = current[0]
                queue.append((state, current[1] + 1))
        self.time.append(time)
        self.space.append(space)
        self.result.append(result)