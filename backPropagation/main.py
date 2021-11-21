import numpy as np


class NeuralNetwork:
    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.output = None
        self.layers = None
        # randomly generating the weights
        self.weights = [
            np.random.uniform(low=-0.2, high=0.2, size=(2, 2)),  # input layer
            np.random.uniform(low=-2, high=2, size=(2, 1))  # hidden layer
        ]

    # Calculate neuron activation for an input
    def activate(self, input_values, weights):
        activation = weights
        for i in range(len(input_values) - 1):
            activation += weights * input_values[i]
        return activation

    # transfer neuron activation using the sigmoid function
    def sigmoid_function(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, input_values):
        input_layer = input_values
        hidden_layer = self.activate(input_values, self.weights[0])
        output_layer = self.activate(hidden_layer, self.weights[1])
        output_layer = self.sigmoid_function(output_layer)  # nu s sigura aici,am vazut undeva ceva de genu :))
        self.layers = [
            input_layer,
            hidden_layer,
            output_layer
        ]
        return output_layer


    def train(self, input_values, output_values):
        self.output = self.forward(input_values)
        self.backward(output_values, self.output)  # TODO:functia backward



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
    print(data, output)

    nr_iterations = input("Introduceti numarul maxim de epoci de antrenare: ")
    learning_rate = input("Introduceti numarul ratei de invatare: ")
