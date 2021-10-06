import numpy as np
import wave

input_file = wave.open('Sound_Noise.wav','rb')
output_file = wave.open('Sound_Filtered.wav','wb')

for i in range(44):

