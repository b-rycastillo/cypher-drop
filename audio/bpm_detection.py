from pathlib import Path
import sys

import librosa


def detect_bpm(audio_path: str) -> None:
    file_path = Path(audio_path)

    if not file_path.exists():
        print(f"Error: file not found -> {file_path}")
        sys.exit(1)

    print(f"Loading audio file: {file_path}")
    y, sr = librosa.load(file_path, sr=None)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo_value = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(f"Detected BPM: {tempo_value:.2f}")
    print("First 20 beat timestamps:")
    for beat_time in beat_times[:20]:
        print(f"  Beat at {beat_time:.2f}s")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio/bpm_detection.py <audio_file>")
        sys.exit(1)

    detect_bpm(sys.argv[1])