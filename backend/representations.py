import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Representations:
    def rep_imag(list, num=0):
        values = list[num].split(",")
        images_array = np.asarray(values[1:], dtype=float).reshape((28,28))
        plt.imshow(images_array, cmap = "Grays", interpolation = "None")
        plt.grid(True, "major")
        plt.show()

    def rep_matrix (list, num=0):
        values = list[num].split(",")
        images_array = np.asarray(values[1:], dtype=float).reshape((28,28))
        image_matrix = images_array.astype(int)
        print(pd.DataFrame(image_matrix).to_string(index=False, header=False))
