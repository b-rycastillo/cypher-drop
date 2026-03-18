"""
Utilities for visualizing detected beats in an audio waveform.

This module loads an audio file, detects its tempo and beat positions
using librosa, and plots the waveform with vertical markers indicating
each detected beat. It is primarily intended as a debugging and analysis
tool to verify beat detection before connecting the results to robot
movement or other event systems.
"""

import sys

import librosa
import librosa.display
import matplotlib.pyplot as plt

from cypher_drop.audio.bpm_detection import detect_bpm


def visualize_beats(audio_path: str) -> None:
    """
    Visualize beat positions detected in an audio file.

    The function loads the provided audio file, computes the tempo and
    beat frames using librosa, converts the frames into timestamps, and
    plots the waveform with vertical dashed lines marking each beat.

    Args:
        audio_path: Path to the audio file to analyze.

    Exits:
        Terminates the program with a non-zero status if the file does
        not exist.
    """
    # analysis = detect_bpm(audio_path)
    # file_path = Path(audio_path)

    # if not file_path.exists():
    #     print(f"Error: file not found -> {file_path}")
    #     sys.exit(1)

    # y, sr = librosa.load(file_path, sr=None)
    # tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    # tempo_value = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)
    # beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # plt.figure(figsize=(12, 4))
    # librosa.display.waveshow(y, sr=sr, alpha=0.7)

    # for beat_time in beat_times:
    #     plt.axvline(x=beat_time, linestyle="--", alpha=0.6)

    # plt.title(f"Waveform with Beat Markers | BPM: {tempo_value:.2f}")
    # plt.xlabel("Time (seconds)")
    # plt.ylabel("Amplitude")
    # plt.tight_layout()
    # plt.show()

    analysis = detect_bpm(audio_path)

    y, sr = librosa.load(audio_path, sr=None)

    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(y, sr=sr, alpha=0.7)

    for beat_time in analysis.beat_times:
        plt.axvline(x=beat_time, linestyle="--", alpha=0.6)

    plt.title(f"Waveform with Beat Markers | BPM: {analysis.tempo:.2f}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio/visualize_beats.py <audio_file>")
        sys.exit(1)

    visualize_beats(sys.argv[1])
