# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, rayleigh

# variables
main_file = "Data details.xlsx"
air_name = "Air (SLPM)"

# the flame follows normal distribution when it is stable
# the flame follows Rayleigh distribution when its near blowout

# open the main data file
df = pd.read_excel(main_file)

# find the min, max air LBO value
max_air = df[air_name].max()
min_air = df[air_name].min()

# open the files with the min and max air value
file_name = str(int(max_air)) + ".xlsx"
file_name_min = str(int(min_air)) + ".xlsx"
df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])
df2 = pd.read_excel(file_name_min, header=None, names=['Time', 'Amplitude'])

# get the mean and standard deviation for amplitude
mean_amplitude = df1['Amplitude'].mean()
std_amplitude = df1['Amplitude'].std()

# get the mean and standard deviation for amplitude for min air value
mean_amplitude_min = df2['Amplitude'].mean()
std_amplitude_min = df2['Amplitude'].std()


"""
The Normal distribution is characterized by mean and std 
but the Rayleigh is characterized by std only.
"""

# here X axis will be bin centers and 
# Y axis will be counts.

# bins with a step of 0.01V from min to max amplitude
bins = np.arange(df1['Amplitude'].min(), df1['Amplitude'].max() + 0.01, 0.01)

# histogram of the amplitude data
counts, bin_edges = np.histogram(df1['Amplitude'], bins=bins, density=True)

# find the center of each bin for plotting
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

# The paper compares given curves with
# theroetical normal and rayleigh distribution curves.

# normal distribution curve
normal_curve = norm.pdf(bin_centers, mean_amplitude, std_amplitude)

# rayleigh distribution curve
r_loc, r_scale = rayleigh.fit(df1['Amplitude']) # fitting the rayleigh distribution to the data
rayleigh_curve = rayleigh.pdf(bin_centers, loc=r_loc, scale=r_scale)

# plotting the histogram and the curves
plt.plot(bin_centers, counts, label="Data PDF")
plt.plot(bin_centers, normal_curve, label="Normal Distribution", linestyle='--')
plt.plot(bin_centers, rayleigh_curve, label="Rayleigh Distribution", linestyle='--')

# labling
plt.xlabel('Chemiluminescence (Volt)')
plt.ylabel('PDF')
plt.title("PDF of OH* chemiluminescence at max air flow")
plt.legend()
plt.grid(True)
plt.show()
min, 

"""
from the file, The 90SLPM data fits the normal distribution curve well
That means 90SLPM isnt the blowout threshold yet.
"""

# we will do the same for min air values.

# bins with a step of 0.01V from min to max amplitude
bins_min = np.arange(df2['Amplitude'].min(), df2['Amplitude'].max() + 0.01, 0.01)

# histogram of the amplitude data
counts_min, bin_edges_min = np.histogram(df2['Amplitude'], bins=bins_min, density=True)

# find the center of each bin for plotting
bin_centers_min = 0.5 * (bin_edges_min[:-1] + bin_edges_min[1:])

# normal distribution curve
normal_curve_min = norm.pdf(bin_centers_min, mean_amplitude_min, std_amplitude_min)

# rayleigh distribution curve
r_loc_min, r_scale_min = rayleigh.fit(df2['Amplitude']) # fitting the rayleigh distribution to the data
rayleigh_curve_min = rayleigh.pdf(bin_centers_min, loc=r_loc_min, scale=r_scale_min)

# plotting the histogram and the curves
plt.plot(bin_centers_min, counts_min, label="Data PDF")
plt.plot(bin_centers_min, normal_curve_min, label="Normal Distribution", linestyle='--')
plt.plot(bin_centers_min, rayleigh_curve_min, label="Rayleigh Distribution", linestyle='--')

# labling
plt.xlabel('Chemiluminescence (Volt)')
plt.ylabel('PDF')
plt.title("PDF of OH* chemiluminescence at min air flow")
plt.legend()
plt.grid(True)
plt.show()

