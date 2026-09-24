"""Configuration metadata for the CFQ-Attack workflow."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml


@dataclass(frozen=True)
class CFQConfig:
    method: str
    stage_names: tuple[str, ...]


def load_config(path: str | Path) -> CFQConfig:
    payload: Any = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(payload, Mapping):
        raise TypeError("Configuration must be a mapping")
    stages = payload.get("stages", ())
    if not isinstance(stages, list) or not all(isinstance(item, str) for item in stages):
        raise TypeError("Stages must be a list of names")
    return CFQConfig(
        method=str(payload.get("method", "CFQ-Attack")),
        stage_names=tuple(stages),
    )

