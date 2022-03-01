import copy


class State:
    mal_drept = None  # array cu pozitia persoanelor w1,w2,...,h1,h2...(0->stang,1->drept)
    barca = 0  # initial pe malul stang
    drum = None  # array cu state-uri
    adancime = 0 # costul drumului

    def __init__(self, s=None, b=0):
        if s is None:
            s = []
        self.mal_drept = s
        self.barca = b
        self.adancime = 0
        self.drum = []

    def f(self):
        return self.adancime+h(self)


def h(current_state):
    result = len(current_state.mal_drept)
    for i in current_state.mal_drept:
        result = result-i
    return result

def is_valid(current_state):
    for i in range(0, noCouples):
        if current_state.mal_drept[i] != current_state.mal_drept[noCouples + i]:
            for j in range(noCouples, noCouples * 2):
                if current_state.mal_drept[j] == current_state.mal_drept[i]:
                    return True
    return False


def move_person(a):
    return abs(a - 1)


def check_side(current_state):  # verifica ce oamenii sunt pe aceeasi parte cu barca
    good_people = copy.deepcopy(current_state.mal_drept)
    for i in range(0, len(current_state.mal_drept)):
        if current_state.mal_drept[i] == current_state.barca:
            good_people[i] = 1
    return good_people


def is_final(current_state):
    result = 0
    for i in current_state.mal_drept:
        result += i
    if result == noCouples * 2:
        return True
    return False


def visited_state(current_state, searched):
    for k in range(0, len(searched)):
        if current_state.mal_drept == searched[k].mal_drept and current_state.barca == searched[k].barca:
            return True
    return False


def possible_moves(capacity, current_state, movement, result, start):
    for i in range(start, len(current_state.mal_drept)):
        if check_side(current_state)[i] == 1:
            movement.append(i)
            if capacity > 1:
                possible_moves(capacity-1, current_state, movement, result, i)
            if capacity == 1:
                 result.append(copy.deepcopy(movement))
            movement.pop()
    return result


def check_states(state):
    current_state = copy.deepcopy(state)
    result = []
    all_moves = possible_moves(2, state, [], result, 0)
    for i in all_moves:
        current_state = copy.deepcopy(state)
        for j in i:
            current_state.mal_drept[j] = move_person(state.mal_drept[j])
        current_state.barca = move_person(state.barca)
        if visited_state(current_state, searched):
            True
        elif is_valid(current_state):
            searched.append(current_state)
        elif True:
            current_state.adancime = current_state.adancime+1
            current_state.drum.append(state)
            frontier.append(current_state)



def check_hc_state(state):
    current_state = copy.deepcopy(state)
    result = []
    all_moves = possible_moves(2, state, [], result, 0)
    for i in all_moves:
        current_state = copy.deepcopy(state)
        for j in i:
            current_state.mal_drept[j] = move_person(state.mal_drept[j])
        current_state.barca = move_person(state.barca)
        if visited_state(current_state, searched):
            True
        elif is_valid(current_state) and state.f() > current_state.f():
            searched.append(current_state)
        elif True:
            # print(f'f(current_state)={current_state.f()} \n f(state)={state.f()}')
            # if current_state.f() < state.f():
            current_state.adancime = current_state.adancime+1
            current_state.drum.append(state)
            frontier.append(current_state)


def bfs():
    noStates = 0
    while True:
        noStates = noStates + 1
        current = frontier.pop(0)

        if is_final(current) is True:
            return current

        check_states(current)
        searched.append(current)


def hillclimbing():
    noStates = 0
    while True:
        noStates = noStates + 1

        # print(f'size of frontier {len(frontier)}')
        current = frontier.pop(0)

        if is_final(current) is True:
            return current

        check_hc_state(current)
        searched.append(current)


def a_star():
    noStates=0
    while True:
        noStates = noStates + 1
        frontier.sort(key=lambda state: state.f())

        current = frontier.pop(0)

        if is_final(current) is True:
            return current

        check_states(current)
        searched.append(current)


if __name__ == '__main__':
    noCouples = int(input("Enter the number of couples: "))

    couple = [0, 0]
    initial = State([], 0)
    goal = State([], 0)
    drum = []
    frontier = []
    searched = []

    for i in range(0, noCouples):
        initial.mal_drept.extend(couple)

    frontier.append(initial)
    print("\nsearch strategies:")
    print("\t(1) Breadth-First-Search")
    print("\t(2)Hill Climbing Algorithm")
    print("\t(3) A*-Search-Algorithm")
    selection = int(input("Select the search strategy you would like to use: "))

    if (selection == 1):
        goal = bfs()  # search with Breadth-First-Search
    elif (selection == 2):
        goal = hillclimbing()
    elif (selection == 3):
        goal = a_star()  # search with A*-Search-Algorithm

    print("\nSuccess: ", goal.mal_drept, " reached")
    for i in goal.drum:
        drum.append(i.mal_drept)
    print("Path: ", drum)

