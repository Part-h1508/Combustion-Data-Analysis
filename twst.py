import numpy as np
import matplotlib.pyplot as plt

def plot_frequency_amplitude(time_series_data1, sampling_rate1, marker_color1, marker_color2, time_series_data2, sampling_rate2):
    """
    Generates and plots the frequency-amplitude spectrum from a time series signal.

    Args:
        time_series_data (np.array): The input signal (amplitude vs time).
        sampling_rate (float): The number of samples per second (Hz).
    """
    N1 = len(time_series_data1) # Number of samples
    print("Number of samples (N1): " + str(N1))
    T1 = 1.0 / sampling_rate1   # Sample time interval

    # Perform the Fast Fourier Transform (FFT)
    # The result will be complex numbers representing magnitude and phase
    yf = np.fft.fft(time_series_data1)
    print("FFT output: " + str(yf))
    
    
    # Calculate the frequencies corresponding to the FFT output
    xf = np.fft.fftfreq(N1, T1)

    # Focus on the positive frequencies only (spectrum is symmetric)
    # np.abs() is used to get the magnitude (amplitude)
    positive_freq_indices = np.where(xf >= 0)
    positive_xf = xf[positive_freq_indices]
    positive_yf = 2.0/N1 * np.abs(yf[positive_freq_indices]) # Scale amplitude for single-sided spectrum


    # do the same for the second time series data
    N2 = len(time_series_data2) # Number of samples
    T2 = 1.0 / sampling_rate2   # Sample time interval
    yf2 = np.fft.fft(time_series_data2)
    xf2 = np.fft.fftfreq(N2, T2)
    positive_freq_indices2 = np.where(xf2 >= 0)
    positive_xf2 = xf2[positive_freq_indices2]
    positive_yf2 = 2.0/N2 * np.abs(yf2[positive_freq_indices2]) # Scale amplitude for single-sided spectrum


    # Plot the frequency-amplitude spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(positive_xf, positive_yf, color=marker_color1)
    plt.plot(positive_xf2, positive_yf2, color=marker_color2)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Frequency-Amplitude Plot")
    plt.grid()
    plt.show()


import pandas as pd

# open the main data file
main_file = "Data details.xlsx"
df = pd.read_excel(main_file)

for index, row in df.iterrows():
    air_value = row["Air (SLPM)"]
    file_name = str(int(air_value)) + ".xlsx"
    if file_name == "65.xlsx":  # Only process the file for 65 SLPM
        df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])
        
        time_series_data1 = df1['Amplitude'].to_numpy()
        time_series_data_mean = np.mean(time_series_data1)
        time_series_data = time_series_data1 - time_series_data_mean  
        sampling_rate = 2000  

        print(time_series_data)

    # get the same data for 90 SLPM
    elif file_name == "90.xlsx":  # Only process the file for 90 SL
        df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])
        
        time_series_data2 = df1['Amplitude'].to_numpy()
        time_series_data_mean2 = np.mean(time_series_data2)
        time_series_data3 = time_series_data2 - time_series_data_mean2 
        sampling_rate2 = 2000  

        print(time_series_data)
    else: pass

"""
for index, row in df.iterrows():
    air_value = row["Air (SLPM)"]
    file_name = str(int(air_value)) + ".xlsx"
    if file_name == "65.xlsx":  # Only process the file for 65 SLPM
        df1 = pd.read_excel(file_name, header=None, names=['Time', 'Amplitude'])
        
        time_series_data = df1['Amplitude'].to_numpy()
        sampling_rate = 2000  

        print(time_series_data)
    else: pass
"""
plot_frequency_amplitude(time_series_data, sampling_rate, marker_color1='tab:blue', marker_color2='tab:red', time_series_data2=time_series_data3, sampling_rate2=sampling_rate2)

