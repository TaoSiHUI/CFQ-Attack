# Method-to-code overview

| CFQ-Attack component | Reference module |
| --- | --- |
| Overall two-component trajectory | `cfq_attack/pipeline.py` |
| Model-independent backend contracts | `cfq_attack/interfaces.py` |
| Object-aware spatial support | `cfq_attack/masks.py` |
| Attack and quality coordination | `cfq_attack/optimization.py` |

Model-specific implementations are connected through the backend interfaces.

