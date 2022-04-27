import base
import heapq

class PriorityQueue:
    def __init__(self):
        self.state = []

    def push(self, state, cost):
        heapq.heappush(self.state, (cost, state))

    def pop(self):
        return heapq.heappop(self.state)[1]

    def empty(self):
        return len(self.state) < 1
    
    def size(self):
        return len(self.state)
    
class Astar(base.ProblemSolver):
    def __init__(self):
        super().__init__()
        self.name = 'A*'

    def heuristic(self, current_state):
        if 'Shepherd' in current_state:
            h_value = (len(current_state) // 2) * 2 - 1
        else:
            h_value = ((len(current_state) + 1) // 2) * 2
        return int(h_value)

    def run(self):
        time = space = 0
        q = PriorityQueue()
        q.push(base.initial_state, self.heuristic(base.initial_state))
        depth = {base.initial_state: 0}
        self.trace = {base.initial_state: None}
        while not q.empty():
            time += 1
            space = max(space, q.size() + len(depth))
            current = q.pop()
            if current == base.goal:
                break
            for next in base.find_next_states(current):
                if next not in depth and base.valid_state(next):
                    self.trace[next] = current
                    depth[next] = depth[current] + 1
                    f_cost = depth[next] + self.heuristic(next)
                    q.push(next, f_cost)
        self.time.append(time)
        self.space.append(space)
        self.result.append(depth[base.goal])

class AstarTree(base.ProblemSolver):
    def __init__(self):
        super().__init__()
        self.name = 'A* tree'
        self.queue = []

    def heuristic(self, current_state):
        if 'Shepherd' in current_state:
            h_value = (len(current_state) // 2) * 2 - 1
        else:
            h_value = ((len(current_state) + 1) // 2) * 2
        return int(h_value)

    def run(self):
        time = space = 0
        result = None
        self.queue.clear()
        self.trace = {(base.initial_state, 0): None}
        heapq.heappush(self.queue, (self.heuristic(base.initial_state), 0, base.initial_state, None))
        while len(self.queue) > 0:
            time += 1
            space = max(space, len(self.queue))
            current = heapq.heappop(self.queue)
            if current[2] == base.goal:
                result = current[1]
                break
            for next in base.find_next_states(current[2]):
                if next != current[3] and base.valid_state(next):
                    self.trace[(next, current[1] + 1)] = current[2]
                    f_cost = current[1] + 1 + self.heuristic(next)
                    heapq.heappush(self.queue, (f_cost, current[1] + 1, next, current[2]))
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