"""
In the context of your Thermoacoustic Instability (TAI) research, 
autocorrelation is a fantastic metric. 
The paper points out that while a stable flame's 
fluctuations are mostly random noise, 
near-blowout combustion oscillations actually 
become more deterministic. 
Autocorrelation proves this by measuring how much a 
signal looks like a delayed version of itself
""" 

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# variables
main_file = "Data details.xlsx"
air_name = "Air (SLPM)"

# open the main data file
df = pd.read_excel(main_file)

# loop thru the data file to get the air values
for index, row in df.iterrows():
    # emptty list to store the autocorrelation values for the current air value
    ac_vlues = []

    # get the air value for the current row
    air_value = row[air_name]
    
    # open the file with the air value
    file_name = str(int(air_value)) + ".xlsx"
    df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])

    # On X axis they have plotted the LAGS from autocorrelation and on Y axis they have plotted the autocorrelation values.
    # we can use the pandas autocorrelation function to get the autocorrelation values for different lags
    autocorr_values = [df1['Amplitude'].autocorr(lag=i) for i in range(1, 20)] # calculating autocorrelation for lags from 1 to 20

    # creating a nested loop from k=0 to 20.
    for k in range(1, 20):

        # append the autocorrelation value for the current lag to the list
        ac_vlues.append(autocorr_values[k-1]) # k-1 because the index starts from 0

    # now we plot the autocorrelation values for the current air value
    lags = np.arange(1, 20) # lags from 1 to 20
    plt.plot(lags, ac_vlues, label=f"Air value: {air_value}", marker='x')

# plotting the values
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation of Chemiluminescence Signal')
plt.legend()
plt.grid(True)
plt.show()