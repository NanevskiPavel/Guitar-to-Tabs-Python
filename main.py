import sys
from src.audio.audioload import loadAudio
from src.onset.onsetdetect import detectOnset
from src.spectrogram.spectrogramshow import plotSpectrogram, genSpectrogram
from src.pitch.pitchdetect import detectPitch
from src.tabgen.tab_generation import ascii_mapping, format_note_list
import librosa

def main(audio_file):


    #loading audio
    print("\nLoading audio file")
    wav, sr = loadAudio(sys.argv[1])
    print(f"\nSample Rate: {sr}, waveform duration {len(wav)/sr} seconds")


    #onset detection
    print("\nDetecting Onsets")
    onset_detect = detectOnset(wavform=wav, sample_rate=sr)
    
    #spectral generation
    magnitude, db_wav = genSpectrogram(wavfile= wav, sample_rate=sr, onsets=onset_detect)
    plotSpectrogram(db_wav, sample_rate=sr, onsets=onset_detect)

    print("Detected onsets:")
    for t in onset_detect:
        print(f"{t:.3f}")

    #PYIN
    print("\nDetecting notes")
    note_events = detectPitch(wav, sr, onset_detect)

    if len(note_events) == None:
        print("\n No notes were detected")
        return

    print(f"\n There are {len(note_events)} notes found in the file")

    #Tab Gen

    print("\n" + "=" * 56)
    print("NOTE LIST")
    print("=" * 56)
    print(format_note_list(note_events))

    print("\n" + "=" * 56)
    print("GUITAR TAB")
    print("=" * 56)
    tab = ascii_mapping(note_events)
    print(tab)



    
#sys check
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("insufficient args")
        sys.exit(1)
    main(sys.argv[1])