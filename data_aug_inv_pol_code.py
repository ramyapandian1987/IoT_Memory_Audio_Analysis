import sys
import os
import random
import numpy as np
import soundfile as sf
import librosa
import librosa.display
import matplotlib.pyplot as plt


def Augmented_WavCreation(appName):
    main_directory = "New_Wav_Dumps/" + appName + "/"

    '''
    main_directory_lst = []
    main_directory_lst.append(main_directory)
    apps = {}
    apps_list = []
    '''
    for file in os.listdir(main_directory):
        print(file)
        signal, sr = librosa.load(main_directory+file)
        augmented_signal = invert_polarity(signal)
        new_file_name = main_directory + "Aug_" + file
        sf.write(new_file_name, augmented_signal, sr)
        print("Augmented wave created")
    '''
    for main_directory in main_directory_lst:
        wav_list = {}
        wav_files = []
        for folder in os.listdir(main_directory):
            print ("Main Directory:" + folder)
    '''

# polarity inversion
def invert_polarity(signal):
    return signal * -1
    

# Usage: data_aug_inv_pol_code.py Fingerprint_App

if __name__ == "__main__":
    appName = sys.argv[1]
    if appName == sys.argv[1]:
        print("Application Name:" + appName)
        augmented_wav_list = Augmented_WavCreation(appName)
    else:
        print("Invalid app name provided")
        exit(0) 
    


'''
    signal, sr = librosa.load("Mem_dump_rfid_benign_t0.wav")
    augmented_signal = invert_polarity(signal)
    sf.write("Aug_IP_Mem_rfid_Benign_t0.wav", augmented5_signal, sr)
'''   