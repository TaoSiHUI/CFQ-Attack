# CFQ-Attack

Anonymous review-time code for **CFQ-Attack: Transferable Object Detection
Attacks via Attack-Preserving Latent Optimization**.

CFQ-Attack follows one continuous diffusion latent trajectory with two stages:

1. **Complementary-feedback attack-state construction** combines
   output-frequency, object-aware geometry, and multi-level feature feedback.
2. **Attack-preserving quality optimization** improves perceptual and
   structural quality while retaining the attack state established in Stage A.

This compact repository intentionally uses the terminology from the paper.
Internal experiment numbers, historical method names, absolute server paths,
evaluation caches, and development-only branches are not included.

## Repository layout

```text
cfq_attack/
  cli.py             COCO-style image generation entry point
  config.py          paper-aligned configuration dataclasses
  interfaces.py      diffusion/detector/quality backend contracts
  masks.py           object-aware spatial support maps
  optimization.py    gradient normalization and conflict projection
  pipeline.py        two-stage CFQ-Attack optimization loop
configs/
  cfq_attack.yaml    settings reported in the paper
examples/
  backend_template.py  template for model-specific adapters
scripts/
  generate_coco.sh   portable launch example
tests/
  test_core.py       lightweight mathematical checks
```

## Installation

Create a Python 3.10 environment with a CUDA-enabled PyTorch installation,
then install the compact package:

```bash
pip install -e .
```

The detector and diffusion adapters additionally require the versions of
MMDetection and Stable Diffusion used by the host environment. Model weights
and datasets are not redistributed.

## Data format

The generation entry point accepts COCO-style annotations. Each selected image
must have at least one valid bounding box. Images are resized to 512 x 512 and
boxes are scaled consistently before optimization. Generated files use:

```text
<12-digit-image-id>_adv_image.png
```

## Generation

Model-specific initialization is isolated behind a backend factory. Copy
`examples/backend_template.py`, connect it to local Stable Diffusion 2.1 and
MMDetection installations, and provide the resulting factory on the command
line:

```bash
python -m cfq_attack.cli \
  --config configs/cfq_attack.yaml \
  --backend my_backend:create_backend \
  --annotations /path/to/instances.json \
  --image-root /path/to/images \
  --output outputs/cfq_attack \
  --device cuda:0
```

For an ordered subset, additionally pass a JSON list using
`--image-id-manifest`. Resume-safe execution skips only complete output PNGs.

## Method configuration

The default configuration mirrors the paper:

- 30 attack-state iterations with AdamW learning rate 0.01;
- 40 quality iterations with AdamW learning rate 0.0025;
- Stable Diffusion 2.1-base, 30 DDIM steps, inversion step 25, CFG 3;
- feature feedback on zero-based iterations 1, 3, ..., 29;
- attack-retention threshold 0.98 with at most three backtracking retries;
- 512 x 512 LPIPS/MS-SSIM quality objectives.

## Release scope

This submission snapshot contains the paper-facing optimization structure and
portable interfaces. Large checkpoints, datasets, generated samples, target
model evaluators, internal audit logs, and historical ablation implementations
are excluded. See [METHOD_MAP.md](METHOD_MAP.md) for the paper-to-code mapping
and [RELEASE_SCOPE.md](RELEASE_SCOPE.md) for the intentional release boundary.
