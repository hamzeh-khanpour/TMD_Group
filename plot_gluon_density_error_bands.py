import lhapdf
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the nuclear PDF set (replace with your actual set name)
pdf_set = 'nPDFs_nlo_208_82'  # Update with your set name if different
central_pdf = lhapdf.mkPDF(pdf_set, 0)  # 0 is the central PDF member
n_members = central_pdf.set().size  # Number of PDF members for uncertainty calculation

# 2. Define x values (momentum fractions) and Q^2
x_values = np.logspace(-5, 0, 100)  # x ranges from 10^-5 to 1
Q2 = 100  # GeV^2 (Q = 10 GeV)

# 3. Extract gluon distribution for the central value and all members for uncertainties
central_gluon_density = np.array([central_pdf.xfxQ2(21, x, Q2) for x in x_values])

# Initialize arrays to hold the PDF members (for uncertainty)
gluon_densities = np.zeros((n_members, len(x_values)))

# Loop over each PDF member (replicas) and extract the gluon distribution
for member in range(n_members):
    pdf = lhapdf.mkPDF(pdf_set, member)
    gluon_densities[member, :] = [pdf.xfxQ2(21, x, Q2) for x in x_values]

# Calculate the upper and lower bounds (error bands)
gluon_density_upper = np.max(gluon_densities, axis=0)
gluon_density_lower = np.min(gluon_densities, axis=0)

# 4. Create the plot
plt.figure(figsize=(8, 6))

# Plot the central gluon density
plt.plot(x_values, central_gluon_density, label=f"Gluon Density (Q² = {Q2} GeV²)", color='blue')

# Plot the uncertainty band (shaded region)
plt.fill_between(x_values, gluon_density_lower, gluon_density_upper, color='blue', alpha=0.3, label='Uncertainty Band')

# Logarithmic scale for x-axis and y-axis
plt.xscale('log')
#plt.yscale('log')

# Labels and title
plt.xlabel('x (Momentum Fraction)')
plt.ylabel('xg(x, Q²)')
plt.title(f'Gluon Density with Uncertainty Bands at Q² = {Q2} GeV²')

# Legend
plt.legend()

# Grid for better readability
plt.grid(True)

# 5. Save the plot as a PDF
plt.savefig('gluon_density_with_error_bands.pdf', format='pdf')
plt.savefig('gluon_density_with_error_bands.jpg', format='jpg')

# Optionally, display the plot
plt.show()
