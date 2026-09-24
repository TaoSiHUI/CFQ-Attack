"""Model-independent interfaces used by CFQ-Attack."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class DiffusionBackend(Protocol):
    def invert(self, clean_image: Any, condition: Any) -> Any:
        """Map a clean image to its initial latent state."""

    def decode(self, latent: Any, condition: Any) -> Any:
        """Decode a latent state to an image."""


class DetectorFeedback(Protocol):
    def complementary_feedback(self, image: Any, annotations: Any) -> Any:
        """Return complementary feedback for attack construction."""


class QualityFeedback(Protocol):
    def quality_feedback(self, image: Any, reference: Any) -> Any:
        """Return feedback for image-quality optimization."""


@dataclass(frozen=True)
class BackendBundle:
    diffusion: DiffusionBackend
    detector: DetectorFeedback
    quality: QualityFeedback

