import librosa
import soundfile as sf
# These imports are needed for plotting spectrograms
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load(librosa.util.example_audio_file())
librosa.output.write_wav('example_original.wav', y, sr)

my_file = sf.read('example_original.wav')

# All in one line, stft -> hpss -> istft
y_harmonic, y_percussive = librosa.effects.hpss(y)
# y_harmonic, y_percussive = librosa.effects.hpss(y, margin=(1.0, 5.0))

sf.write('example_harmonic.wav', y_harmonic, sr)
sf.write('example_percussive.wav', y_percussive, sr)


'''
    Spectrograms
    Sorry this part is not in the video, but I figure it would be important to include nevertheless.
    In order to visualize the previous time-series arrays, we need to manually return the decomposed stft's.
'''

'''
plt.figure()

plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(3, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y_harmonic)), ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Harmonic power spectrogram')

plt.subplot(3, 1, 3)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y_percussive)), ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Percussive power spectrogram')

plt.tight_layout()
plt.show()
'''