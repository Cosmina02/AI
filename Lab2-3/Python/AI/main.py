# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
# global variables
# mal_l = []
# mal_r = []
nr_couples = 0


def initialization():
    mal_l = []
    mal_r = []
    if nr_couples > 0:
        for i in range(1, nr_couples + 1):
            mal_l.append([i, i])  # sotul va fi pe pozitia 0 din tuplu, iar sotia pe pozitia 1
            mal_r.append([0, 0])
        return [mal_l, mal_r, 0, 0]


def isFinal(current_state):
    if current_state[2] == nr_couples & current_state[3] == 1:
        return True
    return False


def transition(current_state, index_p1, gender1, index_p2=0, gender2=0):
    new_state = current_state
    if current_state[3] == 0:
        new_state[1][index_p1 - 1][gender1] = index_p1
        new_state[0][index_p1 - 1][gender1] = 0
        if index_p2 != 0:
            new_state[1][index_p2 - 1][gender2] = index_p2
            new_state[0][index_p2 - 1][gender2] = 0

    else:
        new_state[0][index_p1 - 1][gender1] = index_p1
        new_state[1][index_p1 - 1][gender1] = 0
        if index_p2 != 0:
            new_state[1][index_p2 - 1][gender2] = index_p2
            new_state[0][index_p2 - 1][gender2] = 0
    k = 0
    mal_mal = new_state[1]
    for i in mal_mal:
        if i[0] == i[1] & i[0] != 0:
            k = k + 1
    new_state[2] = k
    new_state[3] = (new_state[3] + 1) % 2
    return new_state


def isValid(current_state, index_p1, gender1, index_p2=0, gender2=0):
    new_state = transition(current_state, index_p1, gender1, index_p2, gender2)
    rightW = 0
    rightH = 0

    mal_r = new_state[1]
    for i in mal_r:
        if i[0] != 0:
            rightH = rightH + 1
        if i[1] != 0:
            rightW = rightW + 1
    leftW = nr_couples - rightW
    leftH = nr_couples - rightH
    if leftH < 0 | leftW < 0 | rightH < 0 | rightW < 0:
        return False
    elif leftW < leftH & leftW != 0:
        return False
    elif rightW < rightH & rightW != 0 :
        return False
    else:
        return True


if __name__ == '__main__':
    nr_couples = int(input("Number of couples:"))
    state = initialization()  # primeste [situatia de pe malul stang, situatia de pe malul drept, cupluri mal drept
    # pozitia barcii]
    print(state)

    if isValid(state, 2, 0, 2, 1):
        state = transition(state, 2, 0, 2, 1)
        print(isValid(state, 2, 0, 2, 1))
        print(state)
    if isValid(state, 2, 0):
        state = transition(state, 2, 0)
        print(isValid(state, 2, 0))
        print(state)
    if isValid(state, 2, 0, 3, 0):
        state = transition(state, 2, 0, 3, 0)
        print(isValid(state, 2, 0, 3, 0))
        print(state)
