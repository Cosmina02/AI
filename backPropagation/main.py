from NNetwork import *

if __name__ == '__main__':
    data = []
    output = []
    f = open("input.txt", "r")
    for line in f:
        line.split("\n")
        line_content = []
        for nr in line:
            if nr >= '0' and nr <= '9':
                line_content.append(int(nr))
        output.append(line_content.pop(len(line_content) - 1))
        data.append(line_content)
    # print(data, output)

    nr_iterations = input("Introduceti numarul maxim de epoci de antrenare: ")
    learning_rate = input("Introduceti numarul ratei de invatare: ")
    # nr_iterations = "1000"
    # learning_rate = "0.1"
    x = np.array(data, dtype=np.longdouble)
    y = np.array(output, dtype=np.longdouble)
    # print(x, "\n", y)
    network = NeuralNetwork(float(learning_rate))
    for i in range(int(nr_iterations)):
        network.train(x, y)

        # nr = int(nr_iterations) // 10
        # if i % nr == 0:
        print(f'Epoch {i} MSE: {np.mean(np.square(y - network.output))}')