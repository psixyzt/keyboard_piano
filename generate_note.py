import numpy as np
import soundfile as sf
import os

# Create a directory for sound files if it doesn't exist
sound_dir = "sounds"
os.makedirs(sound_dir, exist_ok=True)

# Define note frequencies (A4 = 440 Hz reference)
note_frequencies = {
    "c3": 130.81, "c3#": 138.59, "d3": 146.83, "d3#": 155.56, "e3": 164.81,
    "f3": 174.61, "f3#": 185.00, "g3": 196.00, "g3#": 207.65, "a4": 220.00,
    "a4#": 233.08, "b4": 246.94, "c4": 261.63, "c4#": 277.18, "d4": 293.66,
    "d4#": 311.13, "e4": 329.63, "f4": 349.23, "f4#": 369.99, "g4": 392.00,
    "g4#": 415.30, "a5": 440.00, "a5#": 466.16, "b5": 493.88, "c5": 523.25,
    "c5#": 554.37, "d5": 587.33, "d5#": 622.25, "e5": 659.25, "f5": 698.46,
    "f5#": 739.99, "g5": 783.99, "g5#": 830.61, "a6": 880.00, "a6#": 932.33,
    "b6": 987.77, "c6": 1046.50, "c6#": 1108.73, "d6": 1174.66, "d6#": 1244.51,
    "e6": 1318.51, "f6": 1396.91, "f6#": 1479.98, "g6": 1567.98, "g6#": 1661.22,
    "a7": 1760.00, "a7#": 1864.66, "b7": 1975.53, "c7": 2093.00
}

# Generate waveforms for each note
sample_rate = 44100  # CD quality
duration = 30.0  # 30 seconds

for note, freq in note_frequencies.items():
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)  # Sine wave
    sf.write(os.path.join(sound_dir, f"{note}.wav"), wave, sample_rate)

# Confirm generation
os.listdir(sound_dir)[:10]  # Show first 10 generated files
