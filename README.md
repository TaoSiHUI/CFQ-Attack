# CFQ-Attack

PyTorch reference framework for **CFQ-Attack: Transferable Diffusion-Based
Unrestricted Attacks on Object Detectors via Attack-Preserving Quality
Optimization**.

## Overview

CFQ-Attack is a diffusion-based unrestricted adversarial attack for object
detectors. It aims to improve black-box transferability while maintaining the
perceptual quality of generated adversarial examples.

The method follows a continuous latent-space trajectory. It first constructs a
transferable attack state from complementary detector feedback and then
continues from the same state to improve visual quality while retaining the
established attack behavior.

## Highlights

- Complementary detector feedback at the output, transformed-view, and feature
  levels.
- A unified attack direction with object-aware spatial emphasis.
- Continuous quality optimization from the constructed attack state without a
  second inversion.
- Coordinated perceptual and structural updates with attack-retention checks.
- Evaluation across conventional and cross-paradigm object detectors.

## Method outline

CFQ-Attack contains two consecutive components:

1. **Attack-state construction.** Complementary feedback from the surrogate
   detector is combined to update the diffusion latent and form a transferable
   attack state.
2. **Attack-preserving quality optimization.** Perceptual and structural
   feedback refines the same latent trajectory, while candidate validation
   prevents destructive updates that substantially weaken the attack.

The repository organizes these components through model-independent interfaces,
allowing detector and diffusion backends to be connected without changing the
high-level pipeline.

## Experiments

The accompanying paper evaluates CFQ-Attack on MS COCO and PASCAL VOC. The
evaluation covers standard two-stage, one-stage, point-based, and transformer
detectors, together with cross-paradigm and open-vocabulary targets. Additional
experiments study surrogate generalization, input preprocessing, image quality,
and component ablations.

Please refer to the paper for quantitative results and experimental settings.

## Repository structure

```text
cfq_attack/
  interfaces.py      model-independent backend interfaces
  masks.py           object-aware support hook
  optimization.py    attack and quality coordination hooks
  pipeline.py        two-component CFQ-Attack workflow
configs/
  cfq_attack.yaml    method structure
examples/
  backend_template.py
tests/
  test_core.py
```

## Backend integration

Detector and diffusion implementations are connected through the interfaces in
`cfq_attack/interfaces.py`. The template in `examples/backend_template.py`
illustrates the expected adapter structure. Pretrained checkpoints, datasets,
and third-party model repositories are obtained separately from their original
providers and are not redistributed here.

## Citation

If this project is useful for your research, please cite the corresponding
CFQ-Attack paper. BibTeX information will be added with the publication record.

## Responsible use

This project is intended for academic research on adversarial robustness and
defensive evaluation. Users should evaluate only systems and data for which
they have authorization.

