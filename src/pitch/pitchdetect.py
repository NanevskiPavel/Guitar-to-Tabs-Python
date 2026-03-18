import numpy as np
import librosa


def detectPitch(waveform, sample_rate, onset_time):


    hoplength = 512
    window_duration = 0.15

    results = []

    for i, onset in enumerate(onset_time):

        #onset endtime finder
        if i + 1 < len(onset_time):
            endtime = min(onset + window_duration, onset_time[i+1])
        else:
            endtime = min(onset + window_duration, len(waveform)/sample_rate)


        #setup for pyin
        sample_start = int(onset * sample_rate)
        sample_end = int(endtime * sample_rate)

        segment = waveform[sample_start:sample_end]

        #estimation
        f0, voiced_flag, voiced_probability = librosa.pyin(
            segment,
            fmin=librosa.note_to_hz("E2"),
            fmax=librosa.note_to_hz("E6"),
            sr=sample_rate,
            hop_length=hoplength
        )


        #median finder
        voiced_f0 = f0[voiced_flag]

        if len(voiced_f0) == 0:
            continue

        median_f0 = float(np.median(voiced_f0))
        results.append((float(onset), median_f0))

    return results
