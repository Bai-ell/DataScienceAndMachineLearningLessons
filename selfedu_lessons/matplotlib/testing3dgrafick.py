import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np 
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7, 4))

ax_3d = fig.add_subplot(111, projection='3d')


x = np.linspace(-5, 5, 100)
y = x
z = np.cos(x)

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines')])

plt.show()

