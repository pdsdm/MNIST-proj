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
import pickle


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

script = str(sys.argv[1])

if script == "predict":
    num = int(sys.argv[2])
if script == "train":
    layer1 = int(sys.argv[2])  
    layer2 = int(sys.argv[3])  
    epochs = int(sys.argv[4])  
    lr = float(sys.argv[5])    
    decay = float(sys.argv[6]) 



if script == "train":
    dnn = train_model(train_list, test_list, layer1, layer2, epochs, lr, decay)
    with open("dnn.pkl", "wb") as f:
        pickle.dump(dnn, f)  

if script == "predict":
    if num >= train_list:
        print("Error, num out of index")
    else:
        import pickle
        try:
            with open("dnn.pkl", "rb") as f:
                dnn = pickle.load(f)  

            prediccion = forwarding_output(None, num, train_list, dnn)
            print(prediccion)

        except FileNotFoundError:
            print("Error: No se encontró el modelo entrenado. Ejecuta 'train' primero.")

#Representations.rep_imag(train_list, num)


