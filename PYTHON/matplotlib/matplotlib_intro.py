import matplotlib.pyplot as plt

# Matplotlib is a powerful data visualization library for Python.
# It is designed to create high-quality plots, charts, and figures.

# Matplotlib can be used for a wide range of applications, including:
# - Exploratory data analysis
# - Presenting data in a visually appealing way
# - Creating publication-quality figures for scientific papers
# - Building interactive plots for web applications

# The core of Matplotlib is the pyplot module, which provides a simple interface
# for creating and customizing plots. It is typically imported as plt.

# Let's start by creating a simple line plot:
x = [1, 3, 2, 5, 4]
y = [2, 4, 1, 8, 6]

plt.plot(x)
plt.plot(y)
plt.grid()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot trial', loc = "left")
plt.show()

# This code will create a line plot with x-values [1, 2, 3, 4, 5] and y-values [2, 4, 6, 8, 10].
# The plot will have labeled x and y axes, as well as a title.

# Matplotlib provides a wide range of plot types, including line plots, scatter plots,
# bar plots, histograms, and more. It also allows for extensive customization of plots,
# such as changing colors, adding legends, and adjusting axis scales.

# To learn more about Matplotlib and its capabilities, you can refer to the official documentation:
# https://matplotlib.org/stable/index.html

#matplotlib's most useful features:

# - Line plots: plt.plot()

# - Scatter plots: plt.scatter()

# - Bar plots: plt.bar()

# - Histograms: plt.hist()

# - Pie charts: plt.pie()

# - Customizing plots: labels, titles, colors, legends, etc.

# - Saving plots to files: plt.savefig()

# - Subplots: plt.subplot()

# - 3D plots: mpl_toolkits.mplot3d

# - Interactive plots: plt.show() with interactive backend