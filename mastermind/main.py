import copy
import random

bile = list()
nr_of_color = 0


class State:
    bile_alese = None
    bile_alese_corect = 0

    def __init__(self, b=None, c=0):
        if b is None:
            b = []
        self.bile_alese = b
        self.bile_alese_corect = c


def intialize(n, m, k):
    for i in n:
        bile.append(i)  # facem lista cu bilele disponibile
    nr_of_color = m
    winning_combination = choose_random(nr_of_color, k)
    winning_state.bile_alese = winning_combination
    winning_state.bile_alese_corect = winning_combination
    initial_state = State(0, 0)
    return initial_state


def is_final(current_state):
    bile_a = copy.deepcopy(current_state.bile_alese)
    final = 0
    for i in range(0, len(winning_state.bile_alese)):
        if bile_a[i] == winning_state.bile_alese[i]:
            final = final+1
    if final == len(winning_state.bile_alese)+1:
        return True
    return False


def choose_random(nr_color, k):
    final_combination = list()
    i = 0
    while i < k-1:
        print(i)
        nr = random.randint(1, nr_color)
        culoare = random.choice(bile)
        for j in range(0, nr):
            final_combination.append(culoare)
        i = i+nr
    print(final_combination)
    return final_combination


def check_colors(bile_alese):
    correct = 0
    for i in range(0, len(winning_state.bile_alese)):
        if bile_alese[i] == winning_state.bile_alese[i]:
            correct = correct+1
    return correct




if __name__ == '__main__':
    ceva = ['A', 'B', 'C']
    winning_state = State()
    intialize(ceva, 4, 8)
    print(winning_state.bile_alese)

