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

file_path = ('mathematics.csv')
df = pd.read_csv(file_path)
df.head()
x = df['x']
y = df['y (y = x^2)']

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.6)
plt.title('Scatter Plot of y = x²')
plt.xlabel('x')
plt.ylabel('y = x²')
plt.grid(True)
plt.tight_layout()
plt.show()
# Q2: Logarithmic Regression - Fit a logarithmic regression model to noisy data and plot the result.

def fit_logarithmic_regression(data_file='noisy_data.txt'):
    # Do your coding here
    return fig


# Q3: Fit a square root regression model to data and plot the result.

def fit_square_root_regression(data_file='data.txt'):
    # Do your coding here
    pass

# Q4: Create a 3D plot for the given function z = exp(-0.01*x**2 - 0.01*y**2) over x, y in (-20, 20).

def create_surface_plot():
     # Do your coding here
    pass


# Q5: Create an animated plot for the given function y = 4*cos(2*x) over x in (-4, 4) with step length h=0.01.
def create_animated_plot():
    """    
    Returns:
        ani: Matplotlib FuncAnimation object.
    """
    pass


if __name__ == '__main__':
    unittest.main()
