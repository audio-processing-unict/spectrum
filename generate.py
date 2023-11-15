import numpy
import scipy.signal as sps
from scipy import fft
from scipy.io import wavfile
from matplotlib import pyplot as plt

def generate_sine_wave(frequency: int, duration=1.0, amplitude=1.0, sample_rate=44100) -> numpy.ndarray:
    num_samples = int(duration * sample_rate)
    sampling_times = numpy.linspace(0.0, duration, num_samples, dtype=numpy.float32)
    samples = amplitude * numpy.sin(frequency * sampling_times * (2.0 * numpy.pi))
    return samples

def resample(data, current_rate, new_rate):
    num_samples = round(len(data) * float(new_rate) / current_rate)
    resampled_data = sps.resample(data, num_samples)
    return resampled_data

def main() -> None:
    signal = sum([
        generate_sine_wave(10000, duration=1.0),
        generate_sine_wave(1000, duration=1.0),
        generate_sine_wave(100, duration=1.0)
    ])

    wavfile.write("original.wav", 44100, signal)
    wavfile.write("2000.wav", 2000, resample(signal, 44100, 2000))
    wavfile.write("20000.wav", 20000, resample(signal, 44100, 20000))

if __name__ == "__main__":
    main()
