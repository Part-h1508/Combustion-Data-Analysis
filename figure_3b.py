"""
Fig 3b shows the percentage of the cumulative energy.

The flow will be
Calculate PDF --> sum the energy --> add up energy in low freqiuency range --> divide low energy by total energy
"""
# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# variables
main_file = "Data details.xlsx"
air_name = "Air (SLPM)"

# open the main data file
df = pd.read_excel(main_file)

# loop thru the data file to get ALL the air values
for index, row in df.iterrows():
    # get the air value for the current row
    air_value = row[air_name]
    
    # open the file with the air value
    file_name = str(int(air_value)) + ".xlsx"
    df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])

    # finding the sampling frequency from the time data
    time_data = df1['Time']
    if len(time_data) > 1:
        sampling_interval = time_data.iloc[1] - time_data.iloc[0]
        fs = 1 / sampling_interval
    else:
        fs = 1  

    # using welch's method to estimate the power spectral density
    frequencies, psd = welch(df1['Amplitude'].to_numpy(), fs=fs, nperseg=4096)

    # 1. calculate the running total of the energy at every frequency bin
    cumulative_energy = np.cumsum(psd)
    
    # 2. find the absolute total energy (the very last number in our running total)
    total_energy = cumulative_energy[-1]

    # 3. divide the running total by the absolute total to get a percentage (0.0 to 1.0)
    zeta_array = cumulative_energy / total_energy

    # plotting Frequency (X) vs Cumulative Fraction (Y)
    plt.plot(frequencies, zeta_array, label=f"Air: {air_value} SLPM")

# Formatting the plot
plt.xlabel("Frequency (Hz)")
plt.ylabel('$\zeta$ (Cumulative Energy Fraction)')
plt.title('Cumulative Energy Fraction vs Frequency')
plt.grid()
plt.legend()
plt.xlim(0, 100)  # Limit x-axis to 5000 Hz for better visualization
plt.ylim(0, 0.935)  # Limit y-axis to 1 for better visualization
plt.show()  