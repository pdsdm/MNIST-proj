import numpy as np
import time
from model import CNN_decay


def train_model(training_dataset, testing_dataset, neuron1, nueron2, epochs, lr, decay):
    dnn = CNN_decay(sizes = [784, neuron1, nueron2, 10], epochs = epochs, lr = lr, decay = decay)
    dnn.train(training_dataset, testing_dataset)

    return dnn