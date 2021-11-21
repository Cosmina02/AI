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
    def activate(self, input_values):
        for i in input_values:
            for j in i:
                self.sigmoid_function(j)
        return input_values

    def activate_derivative(self, y):
        return self.sigmoid_derivative(y)

    # transfer neuron activation using the sigmoid function
    def sigmoid_function(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self,output):
        return output * (1.0 - output)

    def forward(self, input_values):
        input_layer = input_values
        hidden_layer = self.activate(input_values)
        output_layer = self.activate(hidden_layer)
        # output_layer = self.sigmoid_function(output_layer)  # nu s sigura aici,am vazut undeva ceva de genu :))
        self.layers = [
            input_layer,
            hidden_layer,
            output_layer
        ]
        return output_layer

    def backward(self, target_output, actual_output):
        difference = []
        error = np.subtract(target_output,actual_output)
        # error = target_output - actual_output

        for backward in range(2, 0, -1):
            gradient = error * self.activate_derivative(self.layers[backward])
            self.weights[backward - 1] += self.learning_rate * np.dot(self.layers[backward - 1].T, gradient)
            error = np.dot(gradient, self.weights[backward - 1].T)



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

    # nr_iterations = input("Introduceti numarul maxim de epoci de antrenare: ")
    # learning_rate = input("Introduceti numarul ratei de invatare: ")
    nr_iterations="20"
    learning_rate="0.1"
    x = np.array(data,dtype=float)
    print(x)
    network = NeuralNetwork(float(learning_rate))
    # for i in range(int(nr_iterations)):
    #     network.train(data,output)
    #
    #     x = int(nr_iterations) // 10
    #     if i % x == 0:
    #         print(f'Epoch {i} MSE: {np.mean(np.square(output - network.output))}')