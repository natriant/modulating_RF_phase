import numpy as np
import matplotlib.pyplot as plt


def seconds_to_rad(my_t, my_f_rf):
    phi = my_t*2*np.pi*my_f_rf
    return phi


def rad_to_sec(my_rad, my_f_rf):
    sec = my_rad/(2*np.pi*my_f_rf)
    return sec

savefig = False

f_rev = 43.45e3  # Hz, to convert turns to time and vice versa
f_rf = 400e6  # frequency of the RF in Hz
turns_max = int(5e5)

std_noise_PN = 0.005  # amplitude of the white noise kicks in rads. aprox from real noise spectrum

# parameters for modulating the phase of the RF
A_sec = 75e-12  # amplitude of the RF modulation in seconds
A_rad = seconds_to_rad(A_sec, f_rf)  # amplitude of the RF modulation in rad
print(A_rad)

mod_period_sec = 4.5e-3  # period of the RF phase modulation in seconds
mod_freq_Hz = 1 / mod_period_sec  # frequency of the RF phase modulation in Hz


# Create white noise
white_PN = np.random.normal(0, std_noise_PN, turns_max)

# simulation time
turns = np.arange(turns_max)
time = turns/f_rev  # seconds

# Create the sin signal
my_signal = A_rad*np.sin(2*np.pi*mod_freq_Hz*time)


# Plotting

plt.plot(turns, white_PN+my_signal, label='White noise + modulation')
plt.plot(turns,  my_signal, label='RF modulation')
plt.plot(turns, white_PN, label='White noise')
plt.ylabel('Amplitude (rad)')
plt.xlabel('Turns')
plt.xlim(0, 700)

plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_turns.png')
plt.show()

plt.plot(time, white_PN+my_signal, label='White noise + modulation')
plt.plot(time,  my_signal, label='RF modulation')
plt.plot(time, white_PN, label='White noise')
plt.ylabel('Amplitude (rad)')
plt.xlabel('Time (s)')
plt.xlim(0, 700/f_rev)
plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_time.png')
plt.show()



plt.plot(time, rad_to_sec(white_PN+my_signal, f_rf)*1e12, label='White noise + modulation')
plt.plot(time,  rad_to_sec(my_signal, f_rf)*1e12, label='RF modulation')
plt.plot(time, rad_to_sec(white_PN, f_rf)*1e12, label='White noise')
plt.ylabel('Amplitude (ps)')
plt.xlabel('Time (s)')
plt.xlim(0, 700/f_rev)
plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_AmplitudePs_time.png')
plt.show()

plt.plot(turns, rad_to_sec(white_PN+my_signal, f_rf)*1e12, label='White noise + modulation')
plt.plot(turns,  rad_to_sec(my_signal, f_rf)*1e12, label='RF modulation')
plt.plot(turns, rad_to_sec(white_PN, f_rf)*1e12, label='White noise')
plt.ylabel('Amplitude (ps)')
plt.xlabel('Turns')
plt.xlim(0, 700)
plt.legend(loc=4)
if savefig:
    plt.savefig('modulating_RF_AmplitudePs_turns.png')
plt.show()
