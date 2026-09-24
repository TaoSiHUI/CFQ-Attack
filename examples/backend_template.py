"""Template for connecting detector, diffusion, and quality backends."""

from __future__ import annotations


class DiffusionAdapter:
    def invert(self, clean_image, condition):
        raise NotImplementedError("Connect a diffusion inversion backend")

    def decode(self, latent, condition):
        raise NotImplementedError("Connect a diffusion decoding backend")


class DetectorAdapter:
    def complementary_feedback(self, image, annotations):
        raise NotImplementedError("Connect a detector backend")


class QualityAdapter:
    def quality_feedback(self, image, reference):
        raise NotImplementedError("Connect a quality backend")

