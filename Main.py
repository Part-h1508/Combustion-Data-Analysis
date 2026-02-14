# restarting
 

# variables for rows and columns
main_file = "Data details.xlsx"
air_name = "Air (SLPM)"

# importing libraries
import pandas as pd
import time

# opening the main data file
df = pd.read_excel(main_file)


# creating an empty list to store the calculated NRMS values
NV = []

# now we loop thru every row and column in the table
for index, row in df.iterrows():
    air_value = row[air_name]

    # creating the file name for the current row based on the 'Air (SLPM)' value
    file_name = str(int(air_value)) + ".xlsx"

    # now we open the file with the air value
    df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])
    
    # now we calculate the mean for amplitudes
    # this mean represents q_bar in the equation.
    mean_amplitude = df1['Amplitude'].mean()

    # now we calculat the standard deviation for the amplitudes
    # std represents the sigma in equation
    std_amplitude = df1['Amplitude'].std()

    # now calculat NRMS by using the formula: NRMS = (sigma / q_bar)
    if mean_amplitude != 0:
        nrms = std_amplitude / mean_amplitude

    else:
        nrms = 0 
    # we use a for loop because if mean amplitude is zero, 
    # the flmae is either blown out or sensor is not working
    # avoiding divide by zero error, we set the nrms value to zero.

    # append the calculated NRMS value to the list
    NV.append(nrms)
    print(NV)

# now we create a new data frame
new_table = pd.DataFrame({
    "Air (SLPM)": df[air_name],
    "NRMS": NV
 })

new_table.to_excel("NRMS_values.xlsx", index=False)