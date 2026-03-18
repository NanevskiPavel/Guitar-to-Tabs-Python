import librosa

def loadAudio(path) :
    return librosa.load(path, sr=None, mono=True)

