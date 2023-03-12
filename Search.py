from Solution import Solution
from Problem import Problem
from datetime import datetime
from periorityQueue import PriorityQueue

class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    def ucs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = PriorityQueue()
        explored = {}
        state = prb.initState
        queue.enqueue_with_priority(-(state.g_n), state)
        explored[state.__hash__()] = 'true'
        while queue.size > 0:
            state = queue.dequeue()
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for c in neighbors:
                
                if not c.__hash__() in explored:
                    explored[c.__hash__()] = 'true'
                    queue.enqueue_with_priority(-(c.g_n), c)

        
        return None

    def dfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        stack = []
        explored = {}
        state = prb.initState
        stack.append(state)
        explored[state.__hash__()] = 'true'
        while len(stack) > 0:
            state = stack.pop()
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if not c.__hash__() in explored:
                    explored[c.__hash__()] = 'true'
                    stack.append(c)
        return None

    @staticmethod
    def ids(prb: Problem) -> Solution:
        d = 0
        while True:
            dfsSearch = Search.dfs1(prb, d)
            if dfsSearch != None:
                return dfsSearch
            d += 1
        return
    @staticmethod
    def dfs1(prb: Problem, depth) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        stack = []
        explored = {}
        state = prb.initState
        stack.append(state)
        explored[state.__hash__()] = 'true'
        while len(stack) > 0:
            state = stack.pop()
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if not c.__hash__() in explored and c.g_n <= depth:
                    explored[c.__hash__()] = 'true'
                    stack.append(c)
        return None
    def gbfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        explored = {}
        state = prb.initState
        queue.append(state)
        explored[state.__hash__()] = 'true'
        while len(queue) > 0:
            state = min(queue, key=lambda x: x.g_n)
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for c in neighbors:
                if not c.__hash__() in explored:
                    explored[c.__hash__()] = 'true'
                    queue.append(c)
        return None

    @staticmethod
    def ida(prb: Problem)-> Solution:
        cutoff = prb.initState.g_n + prb.initState.h_n()
        while True:
            stack = []
            explored = {}
            state = prb.initState
            stack.append(state)
            explored[state.__hash__()] = 'true'
            min = float('inf')
            t = Search.search(prb,stack,explored,cutoff,min)
            if t != None:
                return t
            cutoff = min

    @staticmethod
    def search(prb: Problem, stack: list, explored: dict, cutoff, min) -> Solution:
        start_time = datetime.now()
        while len(stack) > 0:
            state = stack.pop()
            f_n = state.g_n + state.h_n()
            if f_n > cutoff:
                if f_n < min:
                    min = f_n
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for c in neighbors:
                f_n = c.g_n + c.h_n()
                if not c.__hash__() in explored and f_n <= cutoff:
                    explored[c.__hash__()] = 'true'
                    stack.append(c)
        return None

    @staticmethod
    def a (prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = PriorityQueue()
        explored = {}
        state = prb.initState
        queue.enqueue_with_priority(-(state.g_n + state.h_n()), state)
        explored[state.__hash__()] = 'true'
        while queue.size > 0 :
            state = queue.dequeue()
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for c in neighbors:
                if not c.__hash__() in explored:
                    explored[c.__hash__()] = 'true'
                    queue.enqueue_with_priority(-(c.g_n + c.h_n()), c)

        return None
