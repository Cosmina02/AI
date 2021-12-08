class Game:
    matrix = list()
    start = list()
    end = list()
    ice = list()
    position = list()

    def __init__(self, m):
        self.m = m
        for i in range(0, m):
            line = list()
            for j in range(0, m):
                line.append('0')
            self.matrix.append(line)

    def set_start_end(self, start, end):
        if len(start) == 2 and len(end) == 2:
            if (start[0] >= 0 and start[1] <= self.m - 1) and (end[0] >= 0 and end[1] <= self.m - 1):
                self.start = start
                self.end = end
                self.matrix[start[0]][start[1]] = 's'  # 1 va fi valoare de pe start
                self.matrix[end[0]][end[1]] = 'e'  # 2 va fi pvaloare de pe final
                self.position = start
                return True
        print("Enter valid start and end!")
        return False

    def set_ice(self, ice_list):
        for i in ice_list:
            if len(i) == 2 and (i[0] >= 0 and i[1] <= self.m - 1):
                self.ice.append(i)
                self.matrix[i[0]][i[1]] = 'i'  # va fi valoare de pe gheata

    def print_game(self):
        for line in self.matrix:
            print(line)
        print()


class Table:
    matrix = list()
    actions = ['up', 'down', 'left', 'right']
    actions_step = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def __init__(self, n, m):
        self.n = n
        self.m = m
        for i in range(0, n):
            line = list()
            for j in range(0, m):
                line.append(0)
            self.matrix.append(line)

    def print_table(self):
        for line in self.matrix:
            print(line)
        print()

    def perform_action(self, game, action):
        if action in self.actions:
            x = self.actions_step[self.actions.index(action)]
            if 0 <= game.position[0] + x[0] < game.m and 0 <= game.position[1] + x[1] < game.m:
                if game.matrix[game.position[0] + x[0]][game.position[1] + x[1]] == 'i':
                    return False
                else:
                    if game.matrix[game.position[0]][game.position[1]] == 's':
                        self.matrix[0][self.actions.index(action)] = 1
                    game.matrix[game.position[0]][game.position[1]] = 'v'
                    game.position[0] += x[0]
                    game.position[1] += x[1]
                    game.matrix[game.position[0]][game.position[1]] = 'p'
                    return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    q_table = Table(5, 4)
    q_table.print_table()

    game = Game(4)
    start = [0, 0]
    end = [3, 3]
    ice = [[1, 1], [1, 3], [2, 3], [3, 0]]
    game.set_start_end(start, end)
    game.set_ice(ice)
    game.print_game()

    q_table.perform_action(game, "down")
    game.print_game()
    q_table.print_table()


