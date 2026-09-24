"""Reference framework for CFQ-Attack."""

from .config import CFQConfig, load_config
from .pipeline import CFQAttackPipeline, CFQResult

METHOD_NAME = "CFQ-Attack"
STAGES = (
    "complementary_feedback_attack_construction",
    "attack_preserving_quality_optimization",
)

__all__ = [
    "CFQAttackPipeline",
    "CFQConfig",
    "CFQResult",
    "METHOD_NAME",
    "STAGES",
    "load_config",
]

