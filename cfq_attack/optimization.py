"""Optimization interfaces for the two CFQ-Attack components."""

from __future__ import annotations

from typing import Any


def combine_attack_feedback(*feedback: Any) -> Any:
    """Combine complementary feedback into an attack update."""

    del feedback
    raise NotImplementedError("Connect an attack-feedback implementation")


def coordinate_quality_update(quality_feedback: Any, attack_feedback: Any) -> Any:
    """Coordinate quality improvement with attack preservation."""

    del quality_feedback, attack_feedback
    raise NotImplementedError("Connect a quality-update implementation")


def validate_candidate(candidate: Any, reference: Any) -> bool:
    """Validate a quality candidate against its reference state."""

    del candidate, reference
    raise NotImplementedError("Connect a candidate-validation implementation")

