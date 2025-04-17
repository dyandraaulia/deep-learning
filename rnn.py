import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_train = pd.read_csv('datasets/Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values

print(training_set)
