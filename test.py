import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

def updatefig(i):
    fig.clear()
    p = plt.plot(np.random.random(100))
    plt.draw()

anim = animation.FuncAnimation(fig, updatefig, 10)
anim.save("/tmp/test.avi", fps=1)