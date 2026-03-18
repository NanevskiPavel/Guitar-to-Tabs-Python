import librosa

def detectOnset(wavform, sample_rate):
    onset = librosa.onset.onset_detect(y=wavform, sr=sample_rate, units="time")
    return onset