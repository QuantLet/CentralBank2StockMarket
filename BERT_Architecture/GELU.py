import torch
import numpy as np
import matplotlib.pyplot as plt

plt.plot(x, gelu, color='blue', label='GELU')
plt.plot(x, relu, color='red', label='ReLU')
plt.savefig('GELU_activation.png', dpi=300, transparent=True)
plt.show()
