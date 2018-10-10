import pyaudio
import numpy as np
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 2   # in seconds, may be float
f = 100.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
i = 0
while(True):
    #i+=1
    #if i == 1:
    #    f += 1
    #    print(f)
    #    i = 0
    f = 440
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    #stream.write(volume*samples)
    f = 880
    samples += (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    stream.write(volume*samples)
    #samples1 = (np.sin(2*np.pi*np.arange(fs*duration)*100/fs)).astype(np.float32)
    #samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*400/fs)).astype(np.float32)
    #stream.write(volume*(samples1 + samples2))
#samples1 = (np.sin(2*np.pi*np.arange(fs*duration)*100/fs)).astype(np.float32)
#samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*400/fs)).astype(np.float32)
#plt.plot(samples1 + samples2)
#plt.show()
stream.stop_stream()
stream.close()

p.terminate()

