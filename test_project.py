import unittest
import pandas as pd
import matplotlib.pyplot as plt
from scatter_plot import create_scatter_plot
import os

# Q1

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

if __name__ == '__main__':
    unittest.main()
