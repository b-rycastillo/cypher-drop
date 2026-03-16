from pathlib import Path
import sys

import librosa
import librosa.display
import matplotlib.pyplot as plt


def visualize_beats(audio_path: str) -> None:
    file_path = Path(audio_path)

    if not file_path.exists():
        print(f"Error: file not found -> {file_path}")
        sys.exit(1)

    y, sr = librosa.load(file_path, sr=None)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo_value = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(y, sr=sr, alpha=0.7)

    for beat_time in beat_times:
        plt.axvline(x=beat_time, linestyle="--", alpha=0.6)

    plt.title(f"Waveform with Beat Markers | BPM: {tempo_value:.2f}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio/visualize_beats.py <audio_file>")
        sys.exit(1)

    visualize_beats(sys.argv[1])