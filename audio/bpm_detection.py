from pathlib import Path
from dataclasses import dataclass
import sys

import librosa


@dataclass
class BeatAnalysis:
    """
    Structured result of a beat analysis operation.

    Attributes:
        tempo: Estimated beats per minute of the audio.
        beat_times: List of timestamps (seconds) where beats occur.
    """

    tempo: float
    beat_times: list[float]


def detect_bpm(audio_path: str) -> BeatAnalysis:
    """
    Analyze an audio file and detect its tempo and beat timestamps.

    Args:
        audio_path: Path to the audio file to analyze.

    Returns:
        BeatAnalysis containing:
            tempo: Estimated beats per minute.
            beat_times: Time (seconds) of each detected beat.
    """
    file_path = Path(audio_path)

    if not file_path.exists():
        print(f"Error: file not found -> {file_path}")
        sys.exit(1)

    y, sr = librosa.load(file_path, sr=None)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo_value = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)

    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    beat_times_list = beat_times.tolist()

    return BeatAnalysis(
        tempo=tempo_value,
        beat_times=beat_times_list,
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio/bpm_detection.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    analysis = detect_bpm(audio_file)

    print(f"Detected BPM: {analysis.tempo:.2f}")
    print("First 20 beat timestamps:")
    for beat_time in analysis.beat_times[:20]:
        print(f"  Beat at {beat_time:.2f}s")