# IoT_Memory_Audio_Analysis

## IoT Memory to Sound waves

The transformation of memory into sound wave signals provides critical features in terms of frequency or pitch variations depending on the allocation of various memory components like the heap, code, stack, data, etc. The extracted memory at runtime of an IoT app is converted from binary to a sound wave signal to perform memory-audio analysis by leveraging its MFCC and chroma features.

## Dataset

The dataset for this prototype contains 60 labeled sound waves that corresponds to 3 different IoT applications: Smart_access_system, RFID_access_system, and Smart_fan.
The memory forensics tool "Memfetch" is leveraged to acquire runtime memory of each app at 10 different timestamps. These memory snapshots are then augmented using Librosa's Inverse Polarity function to generate 10 additional sound waves for each app. As a result, we have 20 sound waves for each app. The audio files are in .wav format.

## Features

### MFCCs -

The MFCC feature extraction process is highly critical in terms of recognizing a signal’s behavior. Mel Frequency Cepstral Coefficients (MFCCs) are a unique set of
features that represents the overall shape of a spectral envelope and are mostly used to describe timbre in the field
of Music Information Retrieval (MIR).


### Chromagrams - 

The chromagrams represent the tonal properties of an audio signal in a condensed form. The chroma features are also known as "pitch class profiles" due to its logical categorization of pitches with tuning approximation to equal-tempered scales. The chroma features carry harmonic and melodic characteristics of music and are robust to variations in timbre.

## CNN Model - 

The extracted features are passed to our CNN model, which contains two convolution layers with max pooling and 3 dense layers with dropouts. To train our model, 60 memory-audio signals, including the device-acquired and the augmented waves from 3 different IoT applications, are leveraged. As a result, our model outperforms the existing models with a detection accuracy of 100% without the need for extensive training datasets.


#### Credits to https://github.com/AmritK10/Urban-Sound-Classification for the code reference.
