import numpy as np

import cypher_drop.audio.visualize_beats as visualize_beats_module
from cypher_drop.audio.bpm_detection import BeatAnalysis


def test_visualize_beats_calls_detect_bpm(monkeypatch) -> None:
    called_paths = []

    def fake_detect_bpm(audio_path: str) -> BeatAnalysis:
        called_paths.append(audio_path)
        return BeatAnalysis(tempo=120.0, beat_times=[0.5, 1.0, 1.5])

    def fake_load(audio_path: str, sr=None):
        return np.zeros(100), 22050

    monkeypatch.setattr(visualize_beats_module, "detect_bpm", fake_detect_bpm)
    monkeypatch.setattr(visualize_beats_module.librosa, "load", fake_load)
    monkeypatch.setattr(
        visualize_beats_module.librosa.display,
        "waveshow",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "figure", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "axvline", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "title", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "xlabel", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "ylabel", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt,
        "tight_layout",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "show", lambda *args, **kwargs: None
    )

    visualize_beats_module.visualize_beats("assets/dummy.wav")

    assert called_paths == ["assets/dummy.wav"]


def test_visualize_beats_draws_marker_for_each_beat(monkeypatch) -> None:
    beat_markers = []

    def fake_detect_bpm(audio_path: str) -> BeatAnalysis:
        return BeatAnalysis(tempo=120.0, beat_times=[0.5, 1.0, 1.5])

    def fake_load(audio_path: str, sr=None):
        return np.zeros(100), 22050

    def fake_axvline(*args, **kwargs) -> None:
        beat_markers.append((args, kwargs))

    monkeypatch.setattr(visualize_beats_module, "detect_bpm", fake_detect_bpm)
    monkeypatch.setattr(visualize_beats_module.librosa, "load", fake_load)
    monkeypatch.setattr(
        visualize_beats_module.librosa.display,
        "waveshow",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "figure", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(visualize_beats_module.plt, "axvline", fake_axvline)
    monkeypatch.setattr(
        visualize_beats_module.plt, "title", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "xlabel", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "ylabel", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt,
        "tight_layout",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "show", lambda *args, **kwargs: None
    )

    visualize_beats_module.visualize_beats("assets/dummy.wav")

    assert len(beat_markers) == 3


def test_visualize_beats_calls_show(monkeypatch) -> None:
    show_calls = []

    def fake_detect_bpm(audio_path: str) -> BeatAnalysis:
        return BeatAnalysis(tempo=120.0, beat_times=[0.5, 1.0])

    def fake_load(audio_path: str, sr=None):
        return np.zeros(100), 22050

    def fake_show() -> None:
        show_calls.append("show")

    monkeypatch.setattr(visualize_beats_module, "detect_bpm", fake_detect_bpm)
    monkeypatch.setattr(visualize_beats_module.librosa, "load", fake_load)
    monkeypatch.setattr(
        visualize_beats_module.librosa.display,
        "waveshow",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "figure", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "axvline", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "title", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "xlabel", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt, "ylabel", lambda *args, **kwargs: None
    )
    monkeypatch.setattr(
        visualize_beats_module.plt,
        "tight_layout",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(visualize_beats_module.plt, "show", fake_show)

    visualize_beats_module.visualize_beats("assets/dummy.wav")

    assert show_calls == ["show"]
