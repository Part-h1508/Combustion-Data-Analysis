# imports
import matplotlib.pyplot as plt
import pandas as pd

# variables 
main_file = "Data details.xlsx"
nrms_file = "NRMS_values.xlsx"

df = pd.read_excel(main_file)
df1 = pd.read_excel(nrms_file)

# Plot using Fi/FI_LBO on the x-axis 
plt.plot(df['Fi/FI_LBO'], df1['NRMS'], marker='o')

# plotting the values
plt.xlabel('$\Phi / \Phi_{lbo}$')
plt.ylabel('NRMS')
plt.title('NRMS vs Normalized Equivalence Ratio')
plt.grid(True)
plt.show()