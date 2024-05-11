import matplotlib.pyplot as plt
import numpy as np
from rtlsdr import RtlSdr

sdr = RtlSdr()
sdr.sample_rate = 2.048e6   # Hz
sdr.center_freq = 1575.42e6 # Hz
#sdr.freq_correction = 0    # PPM
sdr.gain = 40
sdr.set_bias_tee(True)

rx = sdr.read_samples(2048)

rx = sdr.read_samples(4096)
print(type(rx))
print(rx)

sdr.close()

fig,ax = plt.subplots()
ax.plot(np.abs(rx))

plt.show()
