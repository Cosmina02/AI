import numpy as np

def sigmoid_function(x):
    return 1/(1+np.exp(-x))



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
        output.append(line_content.pop(len(line_content)-1))
        data.append(line_content)
    print(data)

    nr_iterations = input("Introduceti numarul maxim de epoci de antrenare: ")
    learning_rate = input("Introduceti numarul ratei de invatare: ")

