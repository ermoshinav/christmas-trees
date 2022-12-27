import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
number_of_colors = 8
colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]


def animate(f):
    fig.clear()
    ax = fig.add_subplot(111, projection="3d")
    k = 300
    X = [math.cos(i / 5 + f / 10) * (k - i) for i in range(k)]
    Y = [math.sin(i / 5 + f / 10) * (k - i) for i in range(k)]
    Z = [i for i in range(k)]
    ax.scatter(X, Y, Z, c="green", marker="^")

    step = 3
    Z = [i for i in range(1, k, step)]
    X = [math.cos(i / 5 + 2 + f / 10) * (k - i + 10) for i in range(1, k, step)]
    Y = [math.sin(i / 5 + 2 + f / 10) * (k - i + 10) for i in range(1, k, step)]
    ax.scatter(X, Y, Z, c=colors[random.randint(0, 7)], marker="o", s=40)
    plt.xlim(-500, 500)
    plt.ylim(-500, 500)
    return fig,


ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
writergif = animation.PillowWriter(fps=30) 
ani.save("Ёлочка.gif", writer=writergif)