import pandas as pd

# 1. Load your main summary data
# (Make sure this filename matches your actual CSV file exactly)
df_summary = pd.read_csv("Data details.xlsx - Sheet1.csv")

# Create an empty list to store the calculated NRMS values
nrms_list = []

# 2. Loop through every row in the summary data
for index, row in df_summary.iterrows():
    
    # Get the Air SLPM value to figure out the file name (e.g., 65.0 -> '65')
    air_flow = int(row['Air (SLPM)'])
    filename = f"{air_flow}.xlsx"
    
    try:
        print(f"Opening {filename}...")
        
        # 3. Read the specific CH amplitude file
        # Using header=None and names as we figured out earlier to fix the column issue
        df_ch = pd.read_excel(filename, header=None, names=['Time', 'Amplitude'])
        
        # 4. Calculate Mean and Standard Deviation for the 'Amplitude' column
        mean_ch = df_ch['Amplitude'].mean()
        std_ch = df_ch['Amplitude'].std()
        
        # 5. Calculate NRMS (Standard Deviation divided by the Mean)
        nrms = std_ch / mean_ch
        
        # Add it to our list
        nrms_list.append(nrms)
        print(f"  -> Calculated NRMS: {nrms:.4f}")
        
    except FileNotFoundError:
        print(f"  -> ERROR: Could not find {filename}. Skipping...")
        nrms_list.append(None) # Put a blank if the file is missing

# 6. Add the new NRMS list as a brand new column in your main summary table
df_summary['Calculated_NRMS'] = nrms_list

# 7. Print a preview of the final combined table
print("\n--- Final Data with NRMS ---")
print(df_summary[['Air (SLPM)', 'Equivalence ratio', 'Fi/FI_LBO', 'Calculated_NRMS']])

# 8. Save the new complete table to a new CSV file
df_summary.to_csv("Final_Data_with_NRMS.csv", index=False)
print("\nSaved everything to 'Final_Data_with_NRMS.csv'")