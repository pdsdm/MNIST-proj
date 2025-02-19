import numpy as np


def forwarding_output(input_data, num, list, neural):
    
    actual_num = None 
    if num is not None:
        values = list[num].split(',')  
        inputs = (np.asarray(values[1:], dtype=np.float32) / 255.0 * 0.99) + 0.01
        actual_num = int(float(values[0]))  
    elif input_data is not None:
        inputs = (np.asarray(input_data, dtype=np.float32) / 255.0 * 0.99) + 0.01
          
    else:
        return None, None
    result = neural.forward_pass(inputs)
    np.set_printoptions(suppress=True, precision=4)
    print(result)
    predicted_label = int(np.argmax(result)) 
    return actual_num, predicted_label 