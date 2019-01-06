# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)
y = x**2

# Plot the data
plt.plot(x, y, label='exponential')

# Add a legend
plt.legend("Curve")

# Show the plot
plt.show()