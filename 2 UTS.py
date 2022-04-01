'''
Nama   : Tria Suci Cahyani
NIM    : 20051397054
Kelas  : 2020B
'''

import numpy as np
import matplotlib.pyplot as plt
import random


n = 100
x = np.random.standard_normal(n)
y = 3.0 * x

fig = plt.subplots(figsize =(10, 7))

plt.hist2d(x, y)



plt.show()
