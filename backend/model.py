import numpy as np
import time 

class CNN_decay:
    def __init__(self, sizes, epochs, lr, decay=0.0):
        self.sizes = sizes 
        self.epochs = epochs  
        self.lr = lr 
        self.decay = decay 

        input_layer = sizes[0]
        hidden_1 = sizes[1]
        hidden_2 = sizes[2]
        output_layer = sizes[3]

        self.params = {
            'W1': np.random.randn(hidden_1, input_layer) * np.sqrt(1. / hidden_1),
            'W2': np.random.randn(hidden_2, hidden_1) * np.sqrt(1. / hidden_2),
            'W3': np.random.randn(output_layer, hidden_2) * np.sqrt(1. / output_layer)
        }

    def sigmoid(self, x, derivative=False):
        sig = 1 / (1 + np.exp(-x))
        if derivative:
            return sig * (1 - sig)
        return sig
    
    def softmax(self, x, derivative=False):
        exps = np.exp(x - np.max(x))  
        softmax_vals = exps / np.sum(exps, axis=0)
        if derivative:
            return softmax_vals * (1 - softmax_vals)
        return softmax_vals

    def forward_pass(self, x_train):
        params = self.params
        params['A0'] = x_train

        params['Z1'] = np.dot(params['W1'], params['A0'])
        params['A1'] = self.sigmoid(params['Z1'])

        params['Z2'] = np.dot(params['W2'], params['A1'])
        params['A2'] = self.sigmoid(params['Z2'])

        params['Z3'] = np.dot(params['W3'], params['A2'])
        params['A3'] = self.softmax(params['Z3'])

        return params['A3']
    
    def backward_pass(self, y_train, output):
        params = self.params
        change_w = {}

        error = 2 * (output - y_train) / output.shape[0] * self.softmax(params['Z3'], derivative=True)
        change_w['W3'] = np.outer(error, params['A2'])

        error = np.dot(params['W3'].T, error) * self.sigmoid(params['Z2'], derivative=True)
        change_w['W2'] = np.outer(error, params['A1'])

        error = np.dot(params['W2'].T, error) * self.sigmoid(params['Z1'], derivative=True)
        change_w['W1'] = np.outer(error, params['A0'])

        return change_w
    
    def update_weights(self, change_w):
        for key, val in change_w.items():
            if self.params[key].shape == val.shape:
                self.params[key] -= self.lr * val

    def compute_accuracy(self, list):
        predictions = []
        for x in list:
            values = x.split(',')
            inputs = (np.asarray(values[1:], dtype=np.float32) / 255.0 * 0.99) + 0.01
            targets = np.zeros(10) + 0.01
            targets[int(values[0])] = 0.99
            output = self.forward_pass(inputs)
            pred = np.argmax(output)
            predictions.append(pred == np.argmax(targets))

        return np.mean(predictions)

    def train(self, train_list, test_list):
        start_time = time.time()

        for iter in range(self.epochs):
            for x in train_list:
                values = x.split(',')
                inputs = (np.asarray(values[1:], dtype=np.float32) / 255.0 * 0.99) + 0.01
                targets = np.zeros(10) + 0.01
                targets[int(values[0])] = 0.99
                output = self.forward_pass(inputs)
                change_w = self.backward_pass(targets, output)
                self.update_weights(change_w)
            
            self.lr *= (1. / (1. + self.decay * iter))
            
            accuracy = self.compute_accuracy(test_list)
            print(f'Epoch: {iter+1}, Time Spent: {time.time()-start_time:.02f}s, Accuracy: {accuracy*100:.2f}%, Learning Rate: {self.lr:.6f}')
