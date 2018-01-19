from PIL import Image
import numpy as np
import os

image = Image.open('two.jpg').convert("RGB")
r, g, b = image.split()
r = np.matrix(r, dtype=np.int16)
g = np.matrix(g, dtype=np.int16)
b = np.matrix(b, dtype=np.int16)

print(r.sum(1) // r.shape[1] + g.sum(1) // r.shape[1], b.sum(1) // r.shape[1])
