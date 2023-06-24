import numpy as np


class Fungal:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the mycelial network
        self.weights_input_to_hidden = np.random.normal(0.0, input_size ** -0.5,
                                                        (input_size, hidden_size))

        self.weights_hidden_to_output = np.random.normal(0.0, hidden_size ** -0.5,
                                                         (hidden_size, output_size))
        self.learning_rate = 0.1

    def sigmoid(self, x):
        # Activation function
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        # Sensing and Environmental Adaptation:
        # Input to hidden layer
        self.hidden_inputs = np.dot(inputs, self.weights_input_to_hidden)
        self.hidden_outputs = self.sigmoid(self.hidden_inputs)

        # Hidden layer to output layer
        self.final_inputs = np.dot(self.hidden_outputs, self.weights_hidden_to_output)
        self.final_outputs = self.final_inputs

        return self.final_outputs

    def backpropagation(self, final_outputs, hidden_outputs, X, y, delta_weights_i_h, delta_weights_h_o):
        ''' Implement backpropagation '''
        error = y - final_outputs
        hidden_error = np.dot(self.weights_hidden_to_output, error)
        output_error_term = error
        hidden_error_term = hidden_error * hidden_outputs * (1 - hidden_outputs)
        delta_weights_i_h += hidden_error_term * X[:, None]
        delta_weights_h_o += output_error_term * hidden_outputs[:, None]
        return delta_weights_i_h, delta_weights_h_o

    def update_weights(self, delta_weights_i_h, delta_weights_h_o, n_records):
        ''' Update weights on gradient descent step '''
        self.weights_hidden_to_output += self.learning_rate * delta_weights_h_o / n_records
        self.weights_input_to_hidden += self.learning_rate * delta_weights_i_h / n_records

    def train(self, features, targets):
        # Spore Dispersal and Exploration:
        # Learning and Information Exchange:
        n_records = features.shape[0]
        delta_weights_i_h = np.zeros(self.weights_input_to_hidden.shape)
        delta_weights_h_o = np.zeros(self.weights_hidden_to_output.shape)
        for X, y in zip(features, targets):
            final_outputs, hidden_outputs = self.forward(X)
            delta_weights_i_h, delta_weights_h_o = self.backpropagation(final_outputs, hidden_outputs, X, y,
                                                                        delta_weights_i_h, delta_weights_h_o)
        self.update_weights(delta_weights_i_h, delta_weights_h_o, n_records)

    def predict(self, X):
        ''' Make a forward pass through the network with input features '''
        hidden_inputs = np.dot(X, self.weights_input_to_hidden)
        hidden_outputs = self.sigmoid(hidden_inputs)
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_to_output)
        final_outputs = final_inputs
        return final_outputs


# Hypothetical data
X_train = np.random.rand(1000, 10)  # 1000 samples, 10 features each
y_train = np.random.randint(2, size=1000)  # 1000 binary labels
X_test = np.random.rand(200, 10)  # 200 samples, 10 features each

# Network architecture parameters
input_size = 10  # Number of features
hidden_size = 20  # Size of the hidden layer
output_size = 1  # Binary output

# Create and train the Fungal model
fungal = Fungal(input_size, hidden_size, output_size)
fungal.train(X_train, y_train)

# Make predictions
predictions = fungal.predict(X_test)

# Initialize the Fungal network
fungal = Fungal(input_size, hidden_size, output_size)

# Train the Fungal network
fungal.train(X_train, y_train)

# Use the trained Fungal network to make predictions
predictions = fungal.predict(X_test)
