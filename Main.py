# Ganpati bappa morya

# lets just figure out how to open
# a word file and extract data from it

import pandas as pd

# Data entry points:
Data1 = 4000
i = 1

# 1. header=None: Tells pandas "The first row is data, not names"
# 2. names=['Time', 'Value']: Gives your columns actual names
df = pd.read_excel('65.xlsx', header=None, names=['Time', 'Value'])

for time in df['Time'].head(Data1):
    print(f"{i}: " + str(time))
    i+=1