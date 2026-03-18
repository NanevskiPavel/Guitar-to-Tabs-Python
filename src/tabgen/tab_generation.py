import numpy as np
import librosa

STRING_NAMES = ["e", "B", "G", "D", "A", "E"]
sOPEN_NOTES = ["E4", "B3", "G3", "D3", "A2", "E2"]
sOPEN_MIDI = [librosa.note_to_midi(n) for n in sOPEN_NOTES]
MAX_FRET = 24

def hz_to_notename(freq):
    midi = librosa.hz_to_midi(freq)
    return librosa.midi_to_note(int(round(midi)))

def hz_to_string(freq):

    target_midi = round(librosa.hz_to_midi(freq))
    positions = []

    for string_indx, open_midi in enumerate(sOPEN_MIDI):
        fret = target_midi - open_midi

        if 0 <= fret <= MAX_FRET:
            positions.append((string_indx, fret))

    positions.sort(key=lambda p: (p[1],p[0]))
    return positions


def best_position(freq):
    positions = hz_to_string(freq)

    if not positions:
        return None, None
    return positions[0]

def ascii_mapping(note_events, beats_per_line=16):
    if not note_events:
        return "no notes have been found"

    columns = []

    for onset, freq in note_events:
        string_indx, fret = best_position(freq)

        if string_indx is None:
            continue

        col = ["-"] * 6
        col[string_indx] = str(fret)
        columns.append(col)

    if not columns:
        return "no notes were mappable"

    matrix = np.array(columns).T

    # Split into chunks of beats_per_line
    n_notes = matrix.shape[1]
    for chunk_start in range(0, n_notes, beats_per_line):
        chunk = matrix[:, chunk_start:chunk_start + beats_per_line]
        for string_name, row in zip(STRING_NAMES, chunk):
            # Pad each cell to 3 chars wide for readability
            cells = [cell.ljust(3, "-") for cell in row]
            print(string_name + "|" + "".join(cells) + "|")
        print()  # blank line between lines


def format_note_list(note_events):
    """Return a simple list of detected notes with timestamps."""
    rows = []
    rows.append(f"{'Time (s)':<12} {'Frequency (Hz)':<18} {'Note':<8} {'String':<8} {'Fret'}")
    rows.append("-" * 56)
    for onset, freq in note_events:
        note_name = hz_to_notename(freq)
        string_idx, fret = best_position(freq)
        string_label = STRING_NAMES[string_idx] if string_idx is not None else "?"
        fret_label = str(fret) if fret is not None else "?"
        rows.append(f"{onset:<12.3f} {freq:<18.2f} {note_name:<8} {string_label:<8} {fret_label}")
    return "\n".join(rows)