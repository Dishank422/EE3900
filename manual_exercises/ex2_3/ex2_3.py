import soundfile as sf
from scipy import signal

input_signal, fs = sf.read('Sound_Noise.wav')

sampl_freq = fs

order = 4

cutoff_freq = 4000.0

Wn = 2*cutoff_freq/sampl_freq

b, a = signal.butter(order,Wn,'low')

output_signal = signal.filtfilt(b,a,input_signal)

sf.write('Sound_With_ReducedNoise.wav',output_signal,fs)
