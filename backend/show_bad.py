import matplotlib.pyplot as plt
import numpy as np
from predict import forwarding_output


def show_imgs_bad (list, neural_model, num_images):
    wrong_indices = []
    for i in range(len(list)):
        actual, predicted = forwarding_output(None, i, list, neural_model)
        if actual is not predicted:
            wrong_indices.append(i)

    

    fig, axes = plt.subplots(20, 10, figsize=(12, 32))
    axes = axes.flatten()  

    selected_wrong_indices = wrong_indices[:num_images]  

    for i, idx in enumerate(selected_wrong_indices):
        actual_label, predicted_label = forwarding_output(None, idx, list, neural_model)
        
        values = list[idx].split(',')  # Se usa "listas" en lugar de "test_list"
        image = np.asarray(values[1:], dtype=np.float32).reshape(28, 28) 

        axes[i].imshow(image, cmap='Greys')
        axes[i].axis('on')  
        axes[i].set_title(f"Actual: {actual_label}\nPredicted: {predicted_label}\nPosition: {idx}", fontsize=10, color='red')

    plt.tight_layout()
    plt.show()