import numpy as np
import matplotlib.pyplot as plt
from modulate_rf import *

savefig = False

f_rev = 43.45e3  # Hz, to convert turns to time and vice versa
f_rf = 400e6  # frequency of the RF in Hz
turns_max = int(5e5)

std_noise_PN = 0.005  # amplitude of the white noise kicks in rads. aprox from real noise spectrum

# parameters for modulating the phase of the RF
A_sec = 75e-12  # amplitude of the RF modulation in seconds
mod_period_sec = 4.5e-3  # period of the RF phase modulation in seconds

# Create white noise
white_PN = np.random.normal(0, std_noise_PN, turns_max)

# simulation time
turns = np.arange(turns_max)
time = turns/f_rev  # seconds

# Create the sin signal
mod_rf_signal = modulated_rf_phase(A_sec, mod_period_sec, f_rf, turns_max, f_rev)



# Plotting
plt.plot(turns, white_PN+mod_rf_signal, label='White noise + modulation')
plt.plot(turns,  mod_rf_signal, label='RF modulation')
plt.plot(turns, white_PN, label='White noise')
plt.ylabel('Amplitude (rad)')
plt.xlabel('Turns')
plt.xlim(0, 700)

plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_turns.png')
plt.show()

plt.plot(time, white_PN+mod_rf_signal, label='White noise + modulation')
plt.plot(time,  mod_rf_signal, label='RF modulation')
plt.plot(time, white_PN, label='White noise')
plt.ylabel('Amplitude (rad)')
plt.xlabel('Time (s)')
plt.xlim(0, 700/f_rev)
plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_time.png')
plt.show()



plt.plot(time, rad_to_sec(white_PN+mod_rf_signal, f_rf)*1e12, label='White noise + modulation')
plt.plot(time,  rad_to_sec(mod_rf_signal, f_rf)*1e12, label='RF modulation')
plt.plot(time, rad_to_sec(white_PN, f_rf)*1e12, label='White noise')
plt.ylabel('Amplitude (ps)')
plt.xlabel('Time (s)')
plt.xlim(0, 700/f_rev)
plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_AmplitudePs_time.png')
plt.show()

plt.plot(turns, rad_to_sec(white_PN+mod_rf_signal, f_rf)*1e12, label='White noise + modulation')
plt.plot(turns,  rad_to_sec(mod_rf_signal, f_rf)*1e12, label='RF modulation')
plt.plot(turns, rad_to_sec(white_PN, f_rf)*1e12, label='White noise')
plt.ylabel('Amplitude (ps)')
plt.xlabel('Turns')
plt.xlim(0, 700)
plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_AmplitudePs_turns.png')
plt.show()
