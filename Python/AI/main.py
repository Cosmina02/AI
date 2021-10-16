# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
# global variables
# mal_l = []
# mal_r = []
import copy

nr_couples = 0


def initialization():
    # pentru verif la 3 cupluri
    print(nr_couples)
    mal_l = []
    mal_r = []
    if nr_couples > 0:
        for i in range(1, nr_couples + 1):
            mal_l.append([i, i])  # sotul va fi pe pozitia 0 din tuplu, iar sotia pe pozitia 1
            mal_r.append([0, 0])
        return [mal_l, mal_r, 0, 0]


def is_final(current_state):
    # print("in is final",current_state)
    if current_state[2] == nr_couples:
        if current_state[3] == 1:
            return True
    return False


def transition(transition_state, index_p1, gender1, index_p2=-1, gender2=-1):
    new_state = transition_state
    if transition_state[3] == 0:
        new_state[1][index_p1][gender1] = index_p1 + 1
        new_state[0][index_p1][gender1] = 0
        if index_p2 != -1:
            new_state[1][index_p2][gender2] = index_p2 + 1
            new_state[0][index_p2][gender2] = 0

    else:
        new_state[0][index_p1][gender1] = index_p1 + 1
        new_state[1][index_p1][gender1] = 0
        if index_p2 != -1:
            new_state[0][index_p2][gender2] = index_p2 + 1
            new_state[1][index_p2][gender2] = 0
    k = 0
    mal_mal = new_state[1]
    for i in mal_mal:
        if i[0] == i[1] & i[0] != 0:
            k = k + 1
    new_state[2] = k
    new_state[3] = (new_state[3] + 1) % 2
    return new_state


def is_valid(to_validate_state, index_p1, gender1, index_p2=-1, gender2=-1):
    if index_p1 == -1:
        return False
    new_state = transition(to_validate_state, index_p1, gender1, index_p2, gender2)
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
    elif rightW < rightH & rightW != 0:
        return False
    elif rightW + leftW != nr_couples:
        return False
    elif rightH + leftH != nr_couples:
        return False
    else:
        return True


def bkt_strategy(current_state, current_state_list):
    copy_state = copy.deepcopy(current_state)
    copy_state_list = copy.deepcopy(current_state_list)
    current_state_list = []
    if is_final(current_state):
        print("am gasit starea finala")
        return True
    else:
        #        if current_state[3] == 0: # daca barca se va duce de la stanga la dreapta
        if current_state[3] == 0:
            mal = current_state[0]
        else:
            mal = current_state[1]

        for couple in mal:  # mergem prin fiecare cuplu
            for i in range(0, 2):  # mergem prin fiecare membru al cuplului
                if couple[i] != 0:  # daca exista pe acest mal
                    # if i == 0: # daca este sot
                    for couple2 in mal:  # mergem prin fiecare cuplu
                        for j in range(0, 2):  # mergem prin fiecare membru al cuplului
                            # if couple[i] == couple2[j] and i == j:
                            #     if isValid(copy_state, couple[i] - 1, i) is True:
                            #         new_state = transition(current_state, couple[i] - 1, i)
                            #         print(new_state)
                            #         if bkt_strategy(new_state) is False:
                            #             continue
                            #     else:
                            #         return False
                            # else:
                            # if couple2[j] != 0:
                            if is_valid(copy_state, couple[i] - 1, i, couple2[j] - 1, j) is True:
                                print("persoana ",couple[i],"persoana ", couple2[j],"merg pe malul ", current_state[3]+1%2)
                                new_state = transition(current_state, couple[i] - 1, i, couple2[j] - 1, j)
                                print(i + 1, j + 1)
                                if [couple[i] - 1, i, couple2[j] - 1, j, new_state[3]] not in copy_state_list:
                                    print(new_state)
                                    copy_state_list.append([couple[i] - 1, i, couple2[j] - 1, j, new_state[3]])
                                    current_state_list = copy_state_list
                                    if bkt_strategy(new_state, current_state_list) is True:
                                        return True
                                else:
                                    continue
        return False


if __name__ == '__main__':
    # sys.setrecursionlimit(10000)
    nr_couples = int(input("Number of couples:"))
    state = initialization()  # primeste [situatia de pe malul stang, situatia de pe malul drept, cupluri mal drept
    # pozitia barcii]
    print(state)
    state_list = copy.deepcopy(state)
    bkt_strategy(state, [])
