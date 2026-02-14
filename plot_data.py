# imports
import matplotlib.pyplot as plt
import pandas as pd

# variables 
main_file = "Data details.xlsx"
nrms_file = "NRMS_values.xlsx"


# we take Fi/FI data from Data details.xlsx file and plot on X axis
# we take NRMS values from NRMS_values.xlsx file and plot on Y axis
df = pd.read_excel(main_file)
df1 = pd.read_excel(nrms_file)

# plot the data
plt.plot(df['Air (SLPM)'], df1['NRMS'], marker='o')
plt.xlabel('Air (SLPM)')
plt.ylabel('NRMS')
plt.title('NRMS vs Air (SLPM)')
plt.grid(True)
plt.show()
