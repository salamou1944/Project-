# Website Reverse-Engineering / Clone Skill Pattern

Date: 2026-10-07
Source: https://github.com/JCodesMore/ai-website-cloner-template
Source revision evidence:
- SKILL.md SHA: 20d3332dcd10b6e99f9aeac777f5f59d35d7321c
- inspection-guide.md SHA: c4de3176d0c9b1d822520722182b042fb6c180f2
- framer-and-motion.md SHA: 37c59fb766095cbbda12dc82bfd48025e4ba22dd
License: MIT

## Canonical contract extracted
MAP → OBSERVE → BUILD → COMPARE

### MAP
- Map every requested source URL to a local route.
- Preserve existing authored routes/assets and resolve collisions before replacement.
- Record source-to-local route ownership.
- Keep distinct origins isolated unless a combined app is explicitly required.

### OBSERVE
- Inspect desktop and mobile independently.
- Scroll through lazy/reveal content.
- Exercise click, hover, keyboard, touch and other real visitor inputs.
- Record trigger → visible result.
- Extract real text, images, SVGs, fonts and video.
- Verify content type and dimensions instead of trusting URL extensions.
- Record responsive transitions and important computed geometry/type.
- Preserve source URL → local asset provenance.

### BUILD
- Establish shared fonts, layout, routes and components first.
- Use real source content/assets rather than placeholders.
- Recreate observed interactions, not only the initial screenshot.
- Keep source-specific assets scoped and editable.
- Delegate only after shared ownership and evidence are clear.

### COMPARE
- Compare source and local at the same viewport, scroll position and interaction state.
- Review initial/active/settled states and reverse-scroll behavior where applicable.
- Repair in order: geometry → missing sections/layers → typography/wrapping → asset crop → spacing/motion.
- Test navigation, controls, media, mobile overflow and runtime errors.
- Run the production check.

## Completion gate
A clone is not complete from build success alone.
Required evidence:
1. successful production check;
2. rendered source/local comparison at representative desktop/mobile states;
3. meaningful controls exercised;
4. remaining differences explicitly recorded.

## Motion-specific rule
Classify animation drivers as time, scroll, click/hover, pointer/canvas or media. Reproduce the driver, not a static approximation. For Framer/sticky/animated pages, inspect initial, active and settled states and verify reverse behavior.

## Collection integration
This is an extracted Skill/Pattern, not a wholesale import of JCodesMore/ai-website-cloner-template.
Use semantic dedupe before attaching it to existing browser, SOAT, runtime-proof, or agent-skills contracts.
Upgrade existing Skills where overlap exists; preserve this source record for provenance.

## High-value uses
- EASY/public-site reconstruction and visual QA
- agent-generated website implementation with evidence
- source/local screenshot comparison
- route and asset provenance
- frontend reverse engineering
- proof-bound completion for visual work
