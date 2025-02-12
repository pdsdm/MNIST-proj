import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import model
from script.convert_ubyt_to_csv import convert
from script.csv_to_list import csv_convert_list
from train import train_model
from predict import forwarding_output
from representations import Representations
from show_bad import show_imgs_bad


train_x = "dataset/ubyte/train-images.idx3-ubyte"
train_y = "dataset/ubyte/train-labels.idx1-ubyte"
test_x = "dataset/ubyte/t10k-images.idx3-ubyte"
test_y = "dataset/ubyte/t10k-labels.idx1-ubyte"

train_csv = "dataset/csv/train.csv"
test_csv = "dataset/csv/test.csv"


#IF THE CSV IS NOT DONE
#convert(train_x, train_y, train_csv, 60000) #generating the files
#convert(test_x, test_y, test_csv, 10000)

train_list, test_list = csv_convert_list(train_csv, test_csv)

import sys

script = int(sys.argv[0])  
layer1 = int(sys.argv[1])  
layer2 = int(sys.argv[2])  
epochs = int(sys.argv[3])  
lr = float(sys.argv[4])    
decay = float(sys.argv[5]) 
num = int(sys.argv[6])


dnn = train_model(train_list, test_list, layer1, layer2, epochs, lr, decay)
num = 12

#print(forwarding_output(None, num, train_list, dnn))
#Representations.rep_imag(train_list, num)

show_imgs_bad(train_list, dnn, 50)