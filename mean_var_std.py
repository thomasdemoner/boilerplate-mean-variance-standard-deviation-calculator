import numpy as np

def calculate(list):

  # print(len(list))
  try:
    len(list) == 9
  except:
    print("List must contain nine numbers.")

  num_arr= np.asarray(list)
  num_arr = np.reshape(num_arr, (3, 3))

  ret_dict = {
    'mean': [np.mean(num_arr, axis= 0).tolist(), np.mean(num_arr, axis= 1).tolist(), np.mean(num_arr)],
    'variance': [np.var(num_arr, axis= 0).tolist(), np.var(num_arr, axis= 1).tolist(), np.var(num_arr)],
    'standard deviation': [np.std(num_arr, axis= 0).tolist(), np.std(num_arr, axis= 1).tolist(), np.std(num_arr)],
    'max': [np.max(num_arr, axis= 0).tolist(), np.max(num_arr, axis= 1).tolist(), np.max(num_arr)],
    'min': [np.min(num_arr, axis= 0).tolist(), np.min(num_arr, axis= 1).tolist(), np.min(num_arr)],
    'sum': [np.sum(num_arr, axis= 0).tolist(), np.sum(num_arr, axis= 1).tolist(), np.sum(num_arr)],
  }

  return ret_dict