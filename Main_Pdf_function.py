# imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# variables 
main_file = "Data details.xlsx"
air_name = "Air (SLPM)"

# opening the main data file
df = pd.read_excel(main_file)

# getting the air values
for index, row in df.iterrows():
    air_value = row[air_name]
    
    # open the file with the air value
    file_name = str(int(air_value)) + ".xlsx"
    df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])

    # find min and max amplitude values
    min_amplitude = df1['Amplitude'].min()
    max_amplitude = df1['Amplitude'].max()

    # defining bin on scaled down version from 0.05V to 0.5V with a step of 0.01V
    bins = np.arange(min_amplitude, max_amplitude + 0.01, 0.01)

    # calculate the histogram
    counts, bin_edges = np.histogram(df1['Amplitude'], bins=bins, density=True)

    # Find the center of each bin for plotting
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    #plotting each line inside the loop to get different lines for different air values
    plt.plot(bin_centers, counts, label=f"Air: {air_value} SLPM")


# plotting the values
plt.xlabel('Chemiluminescence (Volt)')
plt.ylabel('PDF')
plt.title("PDF of OH* chemiluminescence")
plt.legend() # This generates the key!
plt.grid(True)
plt.show()