import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Fortran-generated file
data = np.loadtxt('xg-Q2-100GeV2.dat')

# Extract x values and gluon density values
x = data[:, 0]
gluon_density = data[:, 1]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, gluon_density, label="Gluon Density (Q² = 100 GeV²)", color='blue')

# Logarithmic scale for x-axis
plt.xscale('log')
#plt.yscale('log')

# Labels and title
plt.xlabel('x (Momentum Fraction)')
plt.ylabel('xg(x, Q²)')
plt.title('Gluon Density as a Function of x at Q² = 100 GeV²')

# Legend
plt.legend()

# Grid for better readability
plt.grid(True)

# Save the plot as a PDF
plt.savefig('gluon_density_plot.pdf', format='pdf')

# Optionally, you can also display the plot
plt.show()
