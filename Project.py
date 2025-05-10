import pandas as pd
import matplotlib.pyplot as plt
from scatter_plot import create_scatter_plot
from square_root_regression import fit_square_root_regression
from logarithmic_regression import fit_logarithmic_regression
from surface_plot import create_surface_plot
from animated_plot import create_animated_plot
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import numpy as np
import os


# Q1: Create a scatter plot of y = x^2 using data from a CSV file

def create_scatter_plot(csv_file='mathematics.csv'):
    # Do your coding here
    return fig


# Q2: Logarithmic Regression - Fit a logarithmic regression model to noisy data and plot the result.

def fit_logarithmic_regression(data_file='noisy_data.txt'):
    # Do your coding here
    return fig


# Q3: Fit a square root regression model to data and plot the result.

def fit_square_root_regression(data_file='data.txt'):
    # Do your coding here
    pass

# Q4: Create a 3D plot for the given function z = exp(-0.01*x**2 - 0.01*y**2) over x, y in (-20, 20).

# Define the range and step size
h = 0.05
x = np.arange(-20, 20, h)
y = np.arange(-20, 20, h)
X, Y = np.meshgrid(x, y)

# Define the function
Z = np.exp(-0.01 * X**2 - 0.01 * Y**2)

# Create the plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='rainbow')

# Labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z = exp(-0.01*x² - 0.01*y²)')
ax.set_title('3D Surface Plot of z = exp(-0.01*x² - 0.01*y²)')

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()

# Q5: Create an animated plot for the given function y = 4*cos(2*x) over x in (-4, 4) with step length h=0.01.
#Prepare data
a=4
h=0.01
n=100
x=np.linspace(-a,a,n)
y= a*np.cos(2*x)

#Plot setup
fig, ax=plt.subplots(figsize=(10,8))
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y=2cos(4x)')
ax.set_title("animation of function")
ax.grid(True)


#Initialize the line
line,=ax.plot([],[],'b-',label='y')
ax.legend()

#Initialization
def init():
  line.set_data([],[])
  return line,

  #Update function

def update(frame):
  line.set_data(x[:frame],y[:frame])

#Create animation
ani=FuncAnimation(fig,update,frames=len(x),init_func=init,blit=False,interval=n)

#Display animation
plt.close()
HTML(ani.to_jshtml())


if __name__ == '__main__':
    unittest.main()
