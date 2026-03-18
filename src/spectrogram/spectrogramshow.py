import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

def genSpectrogram(wavfile, sample_rate, onsets=None):
    ft_wav = librosa.stft(wavfile)

    magnitude = abs(ft_wav)

    db_wav = librosa.amplitude_to_db(magnitude, ref=np.max)

    return magnitude, db_wav


def plotSpectrogram(db_wav, sample_rate, onsets = None):
    
    plt.figure(figsize=(10, 6))

    librosa.display.specshow(db_wav, sr=sample_rate, x_axis="time", y_axis="log")

    if onsets is not None:
        plt.vlines(onsets, ymin = 0, ymax = sample_rate/2, color="white", linestyle="--")


    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.show()
