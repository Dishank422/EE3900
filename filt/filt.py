import serial
import numpy as np
import soundfile as sf
import json

input_signal, fs = sf.read('input.wav')
output_signal = np.zeros(len(input_signal))

esp_serial = serial.Serial(port="/dev/ttyS0", baudrate=115200, timeout=10)
esp_serial.flush()

for i in range(len(input_signal)//600):
    tmp = input_signal[600*i:600*(i+1)]
    sent = {"d":tmp.tolist()}
    esp_serial.write(json.dumps(sent).encode('ascii'))
    rec = esp_serial.readline().decode('utf-8').rstrip()
    tmp2 = json.loads(rec)
    tmp3 = tmp2["d"]
    output_signal[600*i:600*(i+1)] = np.array(tmp3)
    print(i)

sf.write('output.wav',output_signal,fs)

