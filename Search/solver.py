from Search.Algorithms import simple, bfs, dfs, ids, astar, branch_and_bound


class Solver:

    def __init__(self, start):
        self.start = start
        self.solution = []

    def solve(self, nr, method=None, optimized=False):

        """

        :param nr: number of rectangles
        :param method: search method
        :param optimized: optimized solution
        :return: list of guards
        """

        if method is None:

            self.solution = simple.guard_detect_simple(self.start, nr)

        # BFS Algorithm
        elif method == 1:

            self.solution = bfs.BFS(self.start, nr).solve(nr / 3)

        # DFS Algorithm
        elif method == 2:

            self.solution = dfs.DFS(self.start, nr).solve(nr / 3, optimized)

        # Iterative Deepening Search Algorithm
        elif method == 3:

            self.solution = ids.IDS(self.start, nr).solve(nr / 3)

        # A* Algorithm
        elif method == 4:

            self.solution = astar.AStar(self.start, nr).solve(nr / 3)

        # Branch-and-Bound
        elif method == 5:

            self.solution = branch_and_bound.BranchAndBround(self.start, nr).solve(nr / 3)

        else:

            return []

        return self.solution
