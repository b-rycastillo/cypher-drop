from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from cypher_drop.audio.bpm_detection import BeatAnalysis, detect_bpm


def _write_test_audio_file(tmp_path: Path) -> Path:
    sample_rate = 22050
    duration_seconds = 1.0

    time = np.linspace(
        0,
        duration_seconds,
        int(sample_rate * duration_seconds),
        endpoint=False,
    )
    audio = 0.5 * np.sin(2 * np.pi * 220 * time)

    audio_file = tmp_path / "test_audio.wav"
    sf.write(audio_file, audio, sample_rate)

    return audio_file


def test_detect_bpm_returns_beat_analysis(tmp_path: Path) -> None:
    audio_file = _write_test_audio_file(tmp_path)

    analysis = detect_bpm(str(audio_file))

    assert isinstance(analysis, BeatAnalysis)


def test_detect_bpm_returns_float_tempo(tmp_path: Path) -> None:
    audio_file = _write_test_audio_file(tmp_path)

    analysis = detect_bpm(str(audio_file))

    assert isinstance(analysis.tempo, float)


def test_detect_bpm_returns_list_of_beat_times(tmp_path: Path) -> None:
    audio_file = _write_test_audio_file(tmp_path)

    analysis = detect_bpm(str(audio_file))

    assert isinstance(analysis.beat_times, list)


def test_detect_bpm_missing_file_exits() -> None:
    missing_file = "does_not_exist.wav"

    with pytest.raises(SystemExit):
        detect_bpm(missing_file)
