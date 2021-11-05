import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

input_signal, fs = sf.read('input.wav')

n_samples = len(input_signal)

output_signal = np.zeros(n_samples)

output_signal[0] = 0.00345416*input_signal[0]
output_signal[1] = 0.00345416*input_signal[1] + 0.01381663*input_signal[0] + 2.5194645*output_signal[0]
output_signal[2] = 0.00345416*input_signal[2] + 0.01381663*input_signal[1] + 0.02072494*input_signal[0] + 2.5194645*output_signal[1] - 2.56083711*output_signal[0]
output_signal[3] = 0.00345416*input_signal[3] + 0.01381663*input_signal[2] + 0.02072494*input_signal[1] + 0.01381663*input_signal[0] + 2.5194645*output_signal[2] - 2.56083711*output_signal[1] + 1.20623537*output_signal[0]

for i in range(4, n_samples):
    output_signal[i] = 0.00345416*input_signal[i] + 0.01381663*input_signal[i-1] + 0.02072494*input_signal[i-2] + 0.01381663*input_signal[i-3] + 0.00345416*input_signal[i-4] + 2.5194645*output_signal[i-1] - 2.56083711*output_signal[i-2] + 1.20623537*output_signal[i-3] - 0.22012927*output_signal[i-4] 

sf.write('Sound_With_ReducedNoise1.wav',output_signal,fs)
