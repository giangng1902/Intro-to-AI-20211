import random
from sys import argv
import base, bfs, ids, astar, idastar

def read_file():
    states = []
    with open('all.txt', 'r') as f:
        for line in f:
            states.append(eval(line.strip()))
    return states

def analysis(test_count, algorithms: list, trace = False):
    table = [['Algorithm', 'Max time', 'Min time', 'Avg time', 'Max space', 'Min space', 'Avg space']]
    for algo in algorithms:
        column = [algo.name, \
            algo.get_max_time(), algo.get_min_time(), algo.get_avg_time(), \
            algo.get_max_space(), algo.get_min_space(), algo.get_avg_space()]
        table.append(column)
    rows = ['|'] * 7
    for col in table:
        maxLen = 0
        for value in col:
            maxLen = max(maxLen, len(str(value)))
        for i in range(7):
            label = str(col[i])
            rows[i] += ' ' + label + ' ' * (maxLen - len(label)) + ' |'
    print('Number of tests:', test_count)
    for row in rows:
        print(row)
    if trace:
        print()
        for algo in algorithms:
            print('* Algorithm: ' + algo.name + ' - Number of steps:', algo.result[0])
            print()
            j = 0
            for state in algo.trace_back():
                print(str(j) + '. ', end='')
                sideA, sideB = '', ''
                for i in base.objects:
                    if i in state:
                        sideA += i + ' '
                    else:
                        sideB += i + ' '
                print('-' * 42)
                print('   ' + '| {:38} |'.format(sideA.strip()))
                print('   ' + '-' * 42)
                print('   ' + '| {:38} |'.format(sideB.strip()))
                print('   ' + '-' * 42)
                j += 1
            print()

if __name__ == "__main__":
    test_count = 50
    all_algo = {'bfstree': bfs.BfsTree(), 'bfs': bfs.Bfs(), 'ids': ids.Ids(), \
                'astartree': astar.AstarTree(), 'astar': astar.Astar(), 'idastar': idastar.Idastar()}
    algorithms = []
    initial_states = read_file()
    trace_back = False
    i = 1
    while i < len(argv):
        if argv[i] == '-test-count':
            test_count = int(argv[i + 1])
            i += 2
        elif argv[i] == '-algo':
            for algo in argv[i + 1].split(','):
                algorithms.append(all_algo[algo])
            i += 2
        elif argv[i] == '-trace-back':
            trace_back = True
            initial_states = [('Cabbage', 'Goat', 'Shepherd', 'Stick', 'Torch', 'Wolf')]
            i += 1
        else:
            print('Invalid argument')
            exit(1)
    if len(algorithms) < 1:
        algorithms = [value for value in all_algo.values()]
    if trace_back:
        test_count = 1
    for test in range(test_count):
        base.next_states.clear()
        base.shuffle_states = False
        base.random_all_next_states(())
        base.shuffle_states = True
        base.initial_state = initial_states[random.randrange(0, len(initial_states))]
        for algo in algorithms:
            algo.solve()
    analysis(test_count, algorithms, trace_back)