import lhapdf
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the nuclear PDF set (replace with your actual set name)
pdf_set = 'nPDFs_nlo_208_82'  # Update this with your set name if different
pdf = lhapdf.mkPDF(pdf_set, 0)  # 0 corresponds to the central PDF member

# 2. Define x values (momentum fractions) and Q^2
x_values = np.logspace(-5, 0, 100)  # x ranges from 10^-5 to 1
Q2 = 100  # GeV^2 (Q = 10 GeV)

# 3. Extract gluon distribution for each x at Q^2 = 100 GeV^2
gluon_density = [pdf.xfxQ2(21, x, Q2) for x in x_values]  # 21 corresponds to the gluon

# 4. Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, gluon_density, label=f"Gluon Density (Q² = {Q2} GeV²)", color='blue')

# Logarithmic scale for x-axis and y-axis
plt.xscale('log')
#plt.yscale('log')

# Labels and title
plt.xlabel('x (Momentum Fraction)')
plt.ylabel('xg(x, Q²)')
plt.title(f'Gluon Density as a Function of x at Q² = {Q2} GeV²')

# Legend
plt.legend()

# Grid for better readability
plt.grid(True)

# 5. Save the plot as a PDF
plt.savefig('gluon_density_plot_full.pdf', format='pdf')
plt.savefig('gluon_density_plot_full.jpg', format='jpg')

# Optionally, display the plot
plt.show()
