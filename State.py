# this class only for the first time setup init state for problem and is given to every search
import copy
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string
    def h_n(self):
        h = 0
        for pipe in self.pipes:
            stack = copy.deepcopy(pipe.stack)
            for i in range(0,len(stack)-1):
                up = stack.pop()
                if up != stack[0]:
                    h += 1
            stack = copy.deepcopy(pipe.stack)
            for i in range(0,len(stack)-1):
                down = stack.pop(0)
                if down != stack[0]:
                    h += 1
        return h
