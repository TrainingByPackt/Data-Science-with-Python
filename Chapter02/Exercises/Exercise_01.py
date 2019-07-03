# Exercise 1: Line Plot

# create an array of numbers for x
import numpy as np
x = np.linspace(0, 10, 20)
print(x)

# create y
y = x**3
print(y)

# create the plot
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

# add x-axis label
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.show()

# add y-label
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.show()

# add title
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# change line color
import matplotlib.pyplot as plt
plt.plot(x, y, 'k') # change color to black
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# make markers into diamonds
import matplotlib.pyplot as plt
plt.plot(x, y, 'Dk') # make markers into diamonds
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# connect markers with a solid line
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k') # connect markers with a solid line
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed') # add title
plt.show()

# increase title font size
import matplotlib.pyplot as plt
plt.plot(x, y, 'D-k') # connect markers with a solid line
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value') # add y axis label
plt.title('x by x Cubed', fontsize=22) # increase font size
plt.show()


