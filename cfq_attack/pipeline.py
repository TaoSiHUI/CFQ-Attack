"""High-level two-component CFQ-Attack pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .config import CFQConfig
from .interfaces import BackendBundle


@dataclass(frozen=True)
class CFQResult:
    adversarial_image: Any
    metadata: dict[str, Any]


class CFQAttackPipeline:
    """Coordinate attack construction and quality optimization."""

    def __init__(self, config: CFQConfig, backend: BackendBundle) -> None:
        self.config = config
        self.backend = backend

    def run(self, clean_image: Any, annotations: Any, condition: Any) -> CFQResult:
        initial_latent = self.backend.diffusion.invert(clean_image, condition)
        attack_state = self._construct_attack_state(
            initial_latent, clean_image, annotations, condition
        )
        final_latent = self._optimize_quality(
            attack_state, clean_image, annotations, condition
        )
        adversarial_image = self.backend.diffusion.decode(final_latent, condition)
        return CFQResult(
            adversarial_image=adversarial_image,
            metadata={"method": self.config.method},
        )

    def _construct_attack_state(
        self,
        initial_latent: Any,
        clean_image: Any,
        annotations: Any,
        condition: Any,
    ) -> Any:
        del initial_latent, clean_image, annotations, condition
        raise NotImplementedError("Connect the attack-state optimizer")

    def _optimize_quality(
        self,
        attack_state: Any,
        clean_image: Any,
        annotations: Any,
        condition: Any,
    ) -> Any:
        del attack_state, clean_image, annotations, condition
        raise NotImplementedError("Connect the quality optimizer")

