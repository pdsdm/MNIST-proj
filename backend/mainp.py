import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import model
from script.convert_ubyt_to_csv import convert
from script.csv_to_list import csv_convert_list


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

