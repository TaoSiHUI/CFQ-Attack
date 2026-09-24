"""Object-aware spatial support interface."""

from __future__ import annotations

from typing import Any


def build_object_support(clean_image: Any, current_image: Any, annotations: Any) -> Any:
    """Build an object-aware support map for spatial weighting."""

    del clean_image, current_image, annotations
    raise NotImplementedError("Connect an object-support implementation")

