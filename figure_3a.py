"""
Figure 3a is a pure frequency spectrum graph
its a PSD vs Frequency graph

We are using Welch's method to
estimate the power spectral density (PSD) of the chemiluminescence signal.



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
        fs = 1  # default to 1 Hz if there is not enough time data

    # using welch's method to estimate the power spectral density
    frequencies, psd = welch(df1['Amplitude'].to_numpy(), fs=fs, nperseg=4096)

    # plotting the PSD vs Frequency graph for the current air value
    plt.semilogy(frequencies, psd, label=f"Air: {air_value} SLPM")

# formatting the plot
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (PSD)')
plt.title('Power Spectral Density of Chemiluminescence Signal')

# Zooming in on the low frequencies (0 to 500 Hz) where combustion dynamics live
plt.xlim(0, 500) 

plt.legend()
plt.grid(True)
plt.show()