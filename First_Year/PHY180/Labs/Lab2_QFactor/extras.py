import numpy as np
from matplotlib import pyplot as plt 
from scipy import signal
import math

times = np.genfromtxt('notThetas.csv', delimiter=',')
print(times)
timesdiff = np.diff(times, 1)
# print(timesdiff)
# print(np.std(timesdiff))

indeces = []
for i in range(0, len(timesdiff)):
    if(timesdiff[i] < 3.0 and timesdiff[i] > 2.3):
        indeces.append(i)

print(np.std(timesdiff[indeces])) 
print(np.average(timesdiff[indeces]))
