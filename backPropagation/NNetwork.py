import numpy as np


class NeuralNetwork:
    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.output = list()
        self.layers = list()
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
    def sigmoid_function(self, values):
        return 1/(1 + np.exp(-values))

    def sigmoid_derivative(self, output):
        return output * (1.0 - output)

    def forward(self, input_values):
        input_layer = input_values
        hidden_layer = self.activate(np.dot(input_values, self.weights[0]))
        output_layer = self.activate(np.dot(hidden_layer, self.weights[1]))

        self.layers = [
            input_layer,
            hidden_layer,
            output_layer
        ]
        return output_layer

    def backward(self, target_output, actual_output):
        error = target_output - actual_output

        for backward in range(2, 0, -1):
            gradient = error * self.activate_derivative(self.layers[backward])
            self.weights[backward-1] = self.weights[backward - 1] + self.learning_rate * np.dot(self.layers[backward - 1].T, gradient)
            error = np.dot(gradient, self.weights[backward - 1].T)


    def train(self, input_values, output_values):
        self.output = self.forward(input_values)
        self.backward(output_values, self.output)