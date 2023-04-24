import sys
import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
import tadasets
from sklearn.metrics.pairwise import pairwise_distances
from scipy import sparse
import time
from PIL import Image

# IMG_WIDTH = 500
# IMG_HEIGHT = 500
MAX_ITERATIONS = 100
N = 3000

# Load image
img = Image.open("squares.jpg")
IMG_WIDTH, IMG_HEIGHT = img.size

def getprob_OLD(x, y):
    prob = 0.5
    if 200 <= y <= 300 and 300 <= x <= 400:
        prob -= 0.25
    if 200 <= y <= 300 and 100 <= x <= 200:
        prob -= 0.40
    if x > 250:
        prob -= 0.25
    return prob

def getprob(x, y):
    return (img.getpixel((x, y))[0] / 255)

# Choose a random point in the image
rand = np.random.default_rng(1234567890)
points = []
for point in range(N):
    for i in range(MAX_ITERATIONS):
        x = int(rand.random() * IMG_WIDTH)
        y = int(rand.random() * IMG_HEIGHT)
        if rand.random() < getprob(x, y):
            break
    points.append([x, y])

points = np.array(points)

plt.subplot(121)
plt.scatter([x for x,y in points], [y for x,y in points])
plt.subplot(122)
results = ripser(points)
plot_diagrams(results['dgms'])
plt.show()