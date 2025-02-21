import numpy as np
import soundfile as sf
import os

# Create a directory for sound files if it doesn't exist
sound_dir = "sounds"
os.makedirs(sound_dir, exist_ok=True)

# Define note frequencies (A4 = 440 Hz reference)

freq_keys = [
    "c3", "c3#", "d3", "d3#", "e3", "f3", 
    "f3#", "g3", "g3#", "a4", "a4#", "b4", 
    "c4", "c4#", "d4", "d4#", "e4", "f4", 
    "f4#", "g4", "g4#", "a5", "a5#", "b5", 
    "c5", "c5#", "d5", "d5#", "e5", "f5",
    "f5#", "g5", "g5#", "a6", "a6#", "b6", 
    "c6", "c6#", "d6", "d6#", "e6", "f6", 
    "f6#", "g6", "g6#", "a7", "a7#", "b7", 
    "c7"
]
freq_values = np.linspace(110.0, 110.0, 49, dtype=np.float64) * 2.0 ** ((np.arange(0, 49, 1, dtype=np.float64) + 3) / 12.0)
note_frequencies = dict(zip(freq_keys, freq_values))

# Generate waveforms for each note
sample_rate = 44000  # CD quality
duration = 30.0  # 30 seconds

for note, freq in note_frequencies.items():
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False, dtype=np.float64)
    wave = 0.15 * np.cos(2 * np.pi * freq * t) # Sine wave
    sf.write(os.path.join(sound_dir, f"{note}.wav"), wave, sample_rate)

# Confirm generation
os.listdir(sound_dir)[:10]  # Show first 10 generated files
