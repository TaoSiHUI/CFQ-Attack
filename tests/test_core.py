from __future__ import annotations

import unittest
from pathlib import Path

from cfq_attack import METHOD_NAME, STAGES, load_config


ROOT = Path(__file__).resolve().parents[1]


class ReferenceStructureTests(unittest.TestCase):
    def test_public_identity(self) -> None:
        self.assertEqual(METHOD_NAME, "CFQ-Attack")
        self.assertEqual(len(STAGES), 2)

    def test_config_structure(self) -> None:
        config = load_config(ROOT / "configs" / "cfq_attack.yaml")
        self.assertEqual(config.method, METHOD_NAME)
        self.assertEqual(config.stage_names, STAGES)


if __name__ == "__main__":
    unittest.main()

