# Brain2Qwerty — Collection Capture

Date: 2026-10-08
Canonical repository: https://github.com/facebookresearch/brain2qwerty
Canonical project name: Brain2Qwerty
Alias/search term: BrainQwerty / brainqwerty (no separate canonical GitHub repository verified)

## What it is
Meta/Facebook Research project for non-invasive brain-to-text decoding. It decodes typed/natural sentences from MEG and EEG recordings using deep-learning architectures.

## Current generations
- v1: keystroke prediction from MEG brain activity using convolution + Transformer.
- v2: moves toward natural sentence generation without requiring keypress timing; the project documentation describes CTC/contrastive components and an LLM-based decoding stage.
- Infrastructure includes NeuralSet and NeuralTrain.

## Reusable capabilities
1. Non-invasive brain-signal → text research pipeline.
2. Neural sequence decoding architecture.
3. CTC-based continuous-signal segmentation/alignment.
4. Neuro-linguistic representation and decoding research.
5. Research-agent orientation via AGENT_README.md.

## Important constraints
- Repository code is released under CC BY-NC 4.0.
- The v2 dataset is under embargo according to the repository.
- v1 data is linked to the BCBL SpanishBCBL dataset and has its own terms.
- Therefore: collect for research/engineering intelligence and future capability extraction; do NOT assume commercial reuse of the code/data is permitted.

## Strategic value for our collection
HIGH research value; LOW immediate revenue value.
Potential future use: neuro-AI/BCI research, sequence-decoding techniques, agent-readable research patterns, and architectural ideas transferable to non-neural sequence problems.

## Sources
- https://github.com/facebookresearch/brain2qwerty
- https://facebookresearch.github.io/brain2qwerty/
