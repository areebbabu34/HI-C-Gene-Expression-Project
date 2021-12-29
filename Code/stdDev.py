import numpy as np
import math

dataFile = open("0-100DataSetGenetoAll.txt", 'r')

storage = []

for line in dataFile:
    if "Sum" in line:
        break
    temp = float(line)
    storage.append(temp)

print("Standard deviation is: ")
print(np.std(storage))
