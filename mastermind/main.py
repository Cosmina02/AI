import copy
import random

bile = list()
nr_of_color = 0


class State:
    bile_incercate = list()
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
            final = final + 1
    if final == len(winning_state.bile_alese):
        return True
    return False


def choose_random(nr_color, k):
    final_combination = list()
    i = 0
    while i < k - 1:
        nr = random.randint(1, nr_color)
        culoare = random.choice(bile)
        for j in range(0, nr):
            final_combination.append(culoare)
        i = i + nr
    return final_combination


def check_colors(bile_alese):
    correct = 0
    for i in range(0, len(winning_state.bile_alese)):
        if bile_alese[i] == winning_state.bile_alese[i]:
            correct = correct + 1
    return correct


def already_guess(player):
    for secv in player.bile_incercate:
        if secv == player.bile_alese:
            return True
    return False


def choose_balls(player_B, l):
    B_input = input('Your guess: ').upper()
    player_B.bile_alese = B_input.split()
    if already_guess(player_B) is False:
        if len(player_B.bile_alese) == l:
            player_B.bile_alese_corect = check_colors(player_B.bile_alese)
            print('You chose ' + str(player_B.bile_alese_corect) + ' correct balls')
            player_B.bile_incercate.append(player_B.bile_alese)
            return True
        else:
            print("Please enter " + str(l) + " guesses")
            return False
    else:
        print("Already guessed this sequence, try another one")
        return False


def play_game():
    l = len(winning_state.bile_alese)
    for i in range(0, nr_tries):
        while True:
            if choose_balls(player_B, l) is True:
                break

        if is_final(player_B) is True:
            return True
        elif i != nr_tries:
            print("Try again!")
    return False


if __name__ == '__main__':
    n = 8
    ceva = ['A', 'B', 'C']
    winning_state = State()
    intialize(ceva, 4, 8)
    print(winning_state.bile_alese)
    #     Interfata jucatorul B
    player_B = State()
    nr_tries = 2 * n

    win = play_game()
    if win is False:
        print("Player A wins!")
    else:
        print("Player B wins!")
