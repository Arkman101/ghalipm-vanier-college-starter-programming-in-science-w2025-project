# Programming in Science - Project

This template repository is the starter project for the Programming in Science Project. Written in Python and tested with Pytest.

## Project: Data Visualization

For this project, you are provided with the `mathematics.csv` file containing a dataset that includes values of `x` and their corresponding `y` values based on the equation `y = x^2`. Additionally, a `logarithm_noisy.csv` dataset has been provided, which contains logarithmic values with added white noise. Your task is to analyze this data and create various visualizations following these instructions:

### Instructions:

1. **Scatter Plot**: **(20%)**  (Use mathematics.csv for this question)
   - Create a scatter plot to visualize the relationship between `x` and `y`, where `y = x^2`.
   - Ensure that the axes are labeled and the plot has an appropriate title.

2. **Logarithmic Regression**: **(20%)**  (Use noisy_data.txt for the question)
   - Use a logarithmic regression model to fit the noisy logarithmic data.
   - Plot the best-fit logarithmic curve on the scatter plot.
   - Ensure proper axis labeling and titling.

3. **Square Root Regression**: **(20%)**  
   - Fit a square root regression model to the data.
   - Plot the best-fit square root curve.
   - Ensure the plot clearly shows both the data points and the regression line.

4. **Surface Plot** : **(20%)**  
   - Create a **3D plot** for the function `z=exp(-0.01*x**2-0.01*y**2)` for `x` and `y` both in (-20, 20) with step length h=0.05.
   - Ensure proper axis labeling and titling.

5. **Animation**: **(20%)**  
   - Create an animated plot for `y = 4*cos(2*x)`, for `x` in (-4,4) with step length h=0.01 where the plot progressively adds data points to simulate the evolution of the graph over time.
   - The animation should be playable on Colab.

### Guidelines:
- Use libraries like `matplotlib`, `seaborn`, `numpy`, and `scipy` to generate the required plots.
- Save each plot as an image file or GIF as instructed.
- Ensure all visualizations are clear and well-labeled.
- Submit your code and all the generated images and animations for evaluation.

### Run Command

`pytest`

