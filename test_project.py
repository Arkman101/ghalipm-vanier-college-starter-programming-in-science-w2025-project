import unittest
import pandas as pd
import matplotlib.pyplot as plt
from scatter_plot import create_scatter_plot
from logarithmic_regression import fit_logarithmic_regression
import os

# Q1: Create a scatter plot of y = x^2 using data from a CSV file 

# Create a test CSV file before running tests
def setup_test_csv():
    data = pd.DataFrame({
        'x': [-2, -1, 0, 1, 2],
        'y': [4, 1, 0, 1, 4]  # y = x^2
    })
    data.to_csv('test_mathematics.csv', index=False)

# Test case for create_scatter_plot() function
def test_create_scatter_plot():
    # Setup the test CSV file
    setup_test_csv()
    
    # Test 1: Check if the CSV file is read correctly
    data = pd.read_csv('test_mathematics.csv')
    assert len(data) == 5, "CSV file should have 5 rows"
    assert list(data.columns) == ['x', 'y'], "CSV file should have 'x' and 'y' columns"
    assert (data['y'] == data['x']**2).all(), "y should equal x^2 for all rows"
    
    # Test 2: Check if the scatter plot is created with correct data
    fig = create_scatter_plot('test_mathematics.csv')
    ax = fig.get_axes()[0]
    scatter = ax.collections[0]
    scatter_data = scatter.get_offsets().data
    expected_data = pd.read_csv('test_mathematics.csv')[['x', 'y']].values
    assert len(scatter_data) == len(expected_data), "Scatter plot should have same number of points as CSV data"
    assert (scatter_data == expected_data).all(), "Scatter plot data should match CSV data"
    
    # Test 3: Check if axes labels and title are set correctly
    assert ax.get_xlabel() == 'x', "X-axis label should be 'x'"
    assert ax.get_ylabel() == 'y', "Y-axis label should be 'y'"
    assert ax.get_title() == 'Scatter Plot of y = x^2', "Title should be 'Scatter Plot of y = x^2'"
    assert len(ax.get_legend().get_texts()) == 1, "Legend should have one entry"
    assert ax.get_legend().get_texts()[0].get_text() == 'y = x^2', "Legend label should be 'y = x^2'"
    
    # Test 4: Check if the plot is created successfully (no errors)
    assert fig is not None, "Figure should be created successfully"
    
    # Clean up
    plt.close(fig)
    os.remove('test_mathematics.csv')

# Q2: Logarithmic Regression - Fit a logarithmic regression model to noisy data and plot the result.
    # Function to set up the test data file
def setup_test_data():
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [0.2, 1.1, 1.5, 1.8, 2.0]  # Noisy logarithmic data
    })
    data.to_csv('test_noisy_data.txt', index=False)

# Test case for fit_logarithmic_regression() function
def test_fit_logarithmic_regression():
    # Setup the test data file
    setup_test_data()
    
    # Test 1: Check if the data file is read correctly
    data = pd.read_csv('test_noisy_data.txt')
    assert len(data) == 5, "Data file should have 5 rows"
    assert list(data.columns) == ['x', 'y'], "Data file should have 'x' and 'y' columns"
    assert (data['x'] == [1, 2, 3, 4, 5]).all(), "x values should match expected values"
    
    # Test 2: Check if logarithmic regression is fitted correctly
    fig, (a, b) = fit_logarithmic_regression('test_noisy_data.txt')
    expected_a = 0.0  # Approximate expected value based on data
    expected_b = 1.0  # Approximate expected value based on data
    assert abs(a - expected_a) < 1.0, f"Expected a ≈ {expected_a}, but got {a}"
    assert abs(b - expected_b) < 1.0, f"Expected b ≈ {expected_b}, but got {b}"
    # Test 3: Check if scatter plot and best-fit curve are plotted
    ax = fig.get_axes()[0]
    assert len(ax.collections) == 1, "Scatter plot should have one set of points"
    scatter_data = ax.collections[0].get_offsets().data
    expected_data = pd.read_csv('test_noisy_data.txt')[['x', 'y']].values
    assert (scatter_data == expected_data).all(), "Scatter plot data should match CSV data"
    assert len(ax.lines) == 1, "Best-fit curve should be plotted"
    
    # Test 4: Check if axes labels and title are set correctly
    assert ax.get_xlabel() == 'x', "X-axis label should be 'x'"
    assert ax.get_ylabel() == 'y', "Y-axis label should be 'y'"
    assert ax.get_title() == 'Logarithmic Regression: y = a + b*ln(x)', "Title should be 'Logarithmic Regression: y = a + b*ln(x)'"
    assert len(ax.get_legend().get_texts()) == 2, "Legend should have two entries"
    
    # Clean up
    plt.close(fig)
    os.remove('test_noisy_data.txt')
    

if __name__ == '__main__':
    unittest.main()
