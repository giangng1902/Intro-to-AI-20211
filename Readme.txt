*** Quick start

To test all available algorithms, you can invoke the following command:
(By default, this will print a table summarizing all
  algorithms' performance in 50 random test cases)

        python main.py


To specify the number of test case, try:
(This will run 99 test cases)

        python main.py -test-count 99


To specify which algorithm(s) to run, use:
(Possible values are: bfstree bfs ids astar astartree idastar)

        python main.py -algo astar           # This will run only A*
        python main.py -algo bfs,astar,ids   # This will run BFS, A* and IDS


To trace back solution's path, you can try:
(Passed this argument, the program will run only 1 test case to
  make the output observable.
  And all objects will be at side A of the river initially)
(The following example runs BFS, A* and prints the path)

        python main.py -algo bfs,astar -trace-back


*** Project structure

The following table summarise our project structure:

| File name  | Description                                                                              | Requirement                       |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| main.py    | Program entry point, functions for formatting result and output it to console            | bfs.py ids.py astar.py idastar.py |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| base.py    | Provide base class for problem solver                                                    |                                   |
|            | Provide helper functions to calculate average time/space, record all test results, etc.. |                                   |
|            | Provide interface for querying possible next states, checking if a state is valid        |                                   |
|            | Random initial state and graph tree                                                      |                                   |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| bfs.py     | Breadth first search implementation                                                      | base.py                           |
|            | - 'BfsTree'     class for tree search                                                    |                                   |
|            | - 'Bfs'         class for graph search                                                   |                                   |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| ids.py     | Iterative deepening search implementation                                                | base.py                           |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| astar.py   | A star search implementation                                                             | base.py                           |
|            | - 'AstarTree'   class for tree search                                                    |                                   |
|            | - 'Astar'       class for graph search                                                   |                                   |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| idastar.py | Iterative deepening A star search implementation                                         | base.py                           |
|------------+------------------------------------------------------------------------------------------+-----------------------------------|
| all.txt    | Provide list of all valid states for randomizing initial state                           | base.py                           |
