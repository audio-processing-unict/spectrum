import argparse
import numpy
from scipy import fft
from scipy.io import wavfile
from matplotlib import pyplot as plt

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_path", type=str)
    parser.add_argument("plot_path", type=str)
    args = parser.parse_args()

    rate, signal = wavfile.read(args.audio_path)

    spectrum = fft.fft(signal)
    points = fft.fftfreq(len(spectrum), 1.0 / 44100)
    plt.plot(numpy.abs(points), numpy.abs(spectrum))
    plt.savefig(args.plot_path)

if __name__ == "__main__":
    main()
