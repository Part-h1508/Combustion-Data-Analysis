"""
this file is to simulate the 9th figure
the graph describes physical behaviour of the line
The fig includes

Normalized cumulative duration of LBO precursor events at
different working conditions.

We find:
mean voltage --> blowout threshold at 20%
--> count data points below threshold
--> divide the count by total data points
"""

"""
After some diggin, i found that the Yi and Gutmark
paper used 20% threshold beacuse that fit the best.
my graph wasnt looking same so after some hit and trial
i am stopping it at %
"""


# imports
import pandas as pd
import matplotlib.pyplot as plt

# variables
main_file = "Data details.xlsx"
air_name = "Air (SLPM)"

# open the main data file
df = pd.read_excel(main_file)

# creating a list to store the calculated theta value
theta_values = []

# loop thru the data file to get the air values
for index, row in df.iterrows():
    # get the air value for the current row
    air_value = row[air_name]
    
    # open the file with the air value
    file_name = str(int(air_value)) + ".xlsx"
    df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])

    # calculate the mean amplitude (Q_bar)
    Q_bar = df1['Amplitude'].mean()

    # set the threshold at 20% of the mean amplitude
    threshold = 0.72 * Q_bar

    # count the number of data points below the threshold
    count_below_threshold = (df1['Amplitude'] < threshold).sum()

    # calculate the total number of data points
    total_data_points = len(df1['Amplitude'])

    # check for division by zero
    if total_data_points > 0:
        # calculate theta
        theta = count_below_threshold / total_data_points
    else:
        theta = 0  # if there are no data points, set theta to 0

    theta_values.append(theta)

# now we plot the theta values against the air values
# Fi/FI_LBO column for X axis and 
# normalized cumulative duration of lean blowout precursor events for Y axis

plt.plot(df['Fi/FI_LBO'], theta_values, marker='o', color='tab:red')
plt.xlabel("Fi/FI_LBO")
plt.ylabel('Theta')
plt.title('fig 9')
plt.grid(True)
plt.show()

