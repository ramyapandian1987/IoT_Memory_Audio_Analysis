import random
import numpy as np
import soundfile as sf
import librosa
import librosa.display
import matplotlib.pyplot as plt
import pandas as pd
import os
from tqdm import tqdm

# Waveplots
def _plot_signal_and_augmented_signal(signal, augmented_signal, sr):
    fig, ax = plt.subplots(nrows=2)
    librosa.display.waveshow(signal, sr=sr, ax=ax[0])
    ax[0].set(title="Original signal")
    librosa.display.waveshow(augmented_signal, sr=sr, ax=ax[1])
    ax[1].set(title="Augmented signal")
    plt.show()



# adding white noise
def add_white_noise(signal, noise_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_factor
    return augmented_signal
    
# adding time stretch
def time_stretch(signal, stretch_rate):
    return librosa.effects.time_stretch(signal, stretch_rate)
    
# pitch scaling
def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr, num_semitones)

# polarity inversion
def invert_polarity(signal):
    return signal * -1
    
# random gain
def random_gain(signal, min_gain_factor, max_gain_factor):
    gain_factor = random.uniform(min_gain_factor, max_gain_factor)
    return signal * gain_factor


if __name__ == "__main__":
    
    path = "Datasets/test/folder"
    data = pd.read_csv("Datasets/metadata/IoT_Mem_Sound_Classes.csv")
    for i in range(len(data)):
        fold_no=str(data.iloc[i]["Folder_Num"])
        #print(fold_no)
        file=data.iloc[i]["File_Name"]
        print(file)
        label = data.iloc[i]["Class_ID"]
        #print (label)
        filename = path + fold_no + "/" + file
        print(filename)
        #aug_filename = path + fold_no + "/" + "WN1_" + file
        #print(aug_filename)
        signal, sr = librosa.load(filename)
        #signal, sr = librosa.load("scale.wav")
        
        ## Creating Augmented signals
        augmented1_signal = add_white_noise(signal, 0.01)
        print("WN1 Augmented wave created")
        augmented2_signal = add_white_noise(signal, 0.02)
        print("WN2 Augmented wave created")
        #augmented3_signal = time_stretch(signal, stretch_rate = 0.01)
        augmented4_signal = pitch_scale(signal, sr = 48000, num_semitones = 1) # Must be between -5 to +5
        print("PS1 Augmented wave created")
        augmented5_signal = pitch_scale(signal, sr = 48000, num_semitones = 2) # Must be between -5 to +5
        print("PS2 Augmented wave created")
        augmented6_signal = invert_polarity(signal)
        print("IP Augmented wave created")
        augmented7_signal = random_gain(signal, 0.2, 0.4)
        print("RG1 Augmented wave created")
        
        ### Saving the Augmented Signals
        sf.write(path + fold_no + "/" + "Aug_WN1_" + file, augmented1_signal, sr)
        sf.write(path + fold_no + "/" + "Aug_WN2_" + file, augmented2_signal, sr)
        #sf.write(path + fold_no + "/" + "Aug_TS1_" + file, augmented3_signal, sr)
        sf.write(path + fold_no + "/" + "Aug_PS1_" + file, augmented4_signal, sr)
        sf.write(path + fold_no + "/" + "Aug_PS2_" + file, augmented5_signal, sr)
        sf.write(path + fold_no + "/" + "Aug_IP_" + file, augmented6_signal, sr)
        sf.write(path + fold_no + "/" + "Aug_RG1_" + file, augmented7_signal, sr)
        
    
    '''
    _plot_signal_and_augmented_signal(signal, augmented1_signal, sr)
    _plot_signal_and_augmented_signal(signal, augmented2_signal, sr)
    _plot_signal_and_augmented_signal(signal, augmented3_signal, sr)
    _plot_signal_and_augmented_signal(signal, augmented4_signal, sr)
    _plot_signal_and_augmented_signal(signal, augmented5_signal, sr)
    '''

