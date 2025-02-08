import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

train_x = "dataset/train-images.idx3-ubyte"
train_y = "dataset/train-labels.idx1-ubyte"
test_x = "dataset/t10k-images.idx3-ubyte"
test_y = "dataset/t10k-labels.idx1-ubyte"

train_csv = "./csv_files/train.csv"
test_csv = "./csv_files/test.csv"

def convert (imgs, labels, outline, n):
    imgf = open(imgs, 'rb') #this function opens the ubyte file.
    labelf = open(labels, 'rb')
    csvf = open(outline, 'w')

    imgf.read(16) #Jumping few bytes due to metadata
    labelf.read(8)
    images = []

    for i in range(n):
        image = [ord(labelf.read(1))] #The reason is 1 is because you want to read just 1 byte. When readed, it automatically jumps to next byte.
        for j in range(28*28):
            image.append(ord(imgf.read(1))) #When appending single num, we added to the list we are in.
        images.append(image)  #Finally adding the existing list to another one.
    
    for image in images:
        csvf.write(",".join(str(plx) for plx in image)+ "\n") #The conversion into csv file.

    imgf.close()
    labelf.close()
    csvf.close()

#IF THE CSV IS NOT DONE
#convert(train_x, train_y, train_csv, 60000) #generating the files
#convert(test_x, test_y, test_csv, 10000)

train_file = open(train_csv, 'r')  
train_list = train_file.readlines()
train_file.close()
num = 7

class Representations:
    def rep_imag(list = train_list, num=0):
        values = list[num].split(",")
        images_array = np.asarray(values[1:], dtype=float).reshape((28,28))
        plt.imshow(images_array, cmap = "Grays", interpolation = "None")
        plt.grid(True, "major")

    def rep_matrix (list = train_list, num=0):
        values = list[num].split(",")
        images_array = np.asarray(values[1:], dtype=float).reshape((28,28))
        image_matrix = images_array.astype(int)
        print(pd.DataFrame(image_matrix).to_string(index=False, header=False))


Representations.rep_matrix(train_list, 234)
