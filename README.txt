#Guitar-Tab-App-Py 

Is a python script which aims to generate tabliture of a certain raw DI from a guitar using the librosa library.
The the script is under a big work in progress disclamer.

#What it does:
- Loads wav audio file;
- Finds onsets;
- Estimates notes pitch with pYIN;
- Outputs the notes found;
- Outputs ASCII tabliture;
- Outputs a spectrogram of the audio file;

#Limitations

- Monophonic only, meaning the pipeline only assumes one note at a time due to the core limitations of the pYIN algorithm.
- The mapping is set to favor always the lowest possible fret + string combo which makes for terrible scalar runs and, obviously, no one in the real world actually plays like that.
- No rhythm/timing — the tab output spaces notes evenly by count, not by actual duration. A quarter note and a sixteenth note look identical in the output.

#Next to come

Most likely the determination pipeline will be migrated to a deeplearning CNN approach - trained on labled DI guitar recordings.
Inteligent string/position mapping as well as better rhythmic anotations and support for things such as slides, bends, pinch harmonics etc.

#Usage

- Install dependencies:

pip install librosa numpy matplotlib

- Run:
python main.py "path/to/your/di_guitar.wav"

The script will print a note list and ASCII tab to the console, then display a spectrogram with onset markers.

#Project Structure
src/
  audio/        # Audio loading
  onset/        # Onset detection
  pitch/        # pYIN pitch detection
  tabgen/       # Note to fret mapping and ASCII tab generation
  spectrogram/  # Spectrogram generation and display
  util/         # Test scripts
main.py

#Requirements

Python 3.10+
librosa
numpy
matplotlib