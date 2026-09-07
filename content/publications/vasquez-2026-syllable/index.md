---
title: "Syllable Stress Detection to Evaluate Pathological Speech and L2 Language"
authors:
- me
- Haritz Arzelus
- Aitor Álvarez
date: "2026-05-03"

# Schedule page publish date (NOT publication's date).
publishDate: "2026-09-07T10:22:36.318647Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication metadata — structured fields used by citation styles and BibTeX export.
# Preprints typically have no formal venue; omit `publication` until the work is accepted.

peer_reviewed: true
open_access: false

publication: '*International Conference on Text, Speech, and Dialogue (TSD) 2026*'


funding:
  - funder: "Basque Government (Spri Group)"
    grant: "IKASPROD (KK-2024/00050)"

abstract: Syllable stress is a major key aspect of speech frequently altered by neurological impairments and varying levels of non-native language proficiency. This paper presents a novel syllable stress detection pipeline designed to evaluate pathological speech and assess L2 learner pronunciation. Separate models for Spanish and English were trained using Common Voice and Librispeech corpora. The proposed architecture extracts multidimensional syllable-level acoustic representations, combining prosodic, spectral, and articulatory features. These representations are processed through a 1D-convolutional projection and a Transformer encoder to capture inter-syllabic dependencies, followed by a time-distributed multi-layer perceptron for per-syllable stress prediction. In-domain evaluations demonstrated overall accuracies of 97.5% for Spanish and 93.9% for English. Furthermore, the model’s practical utility was validated through benchmark evaluations on out-of-domain datasets, spanning L2 Spanish learners and clinical populations with Aphasia, Alzheimer’s, and Parkinson’s diseases. The model successfully captured deviations in stress patterns, with detection accuracy reflecting both Aphasia severity and Spanish L2 proficiency levels. These findings suggest that automated syllable stress detection serves as a viable, objective tool for clinical speech assessment and language learning tracking.



# Summary. An optional shortened abstract.
tags:
- Prosody
- Second Language Learning
- Pathological Speech Processing
- Alzheimer's Disease
- Parkinson's Disease
- Aphasia

featured: true

hugoblox:
  ids:
    doi: https://doi.org/10.1007/978-3-032-37249-9_23

links: 
- type: source
  url: "https://link.springer.com/chapter/10.1007/978-3-032-37249-9_23"
# - type: preprint
#   provider: arxiv
#   id: 1512.04133v1
# - type: code
#   url: https://github.com/HugoBlox/kit
# - type: slides
#   url: https://www.slideshare.net/
# - type: dataset
#   url: "#"
# - type: poster
#   url: "#"

# - type: video
#   url: https://youtube.com
# - type: custom
#   label: Custom Link
#   url: http://example.org

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Syllable Stress detection'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/projects/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
# - internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: ""
---
<!-- 
This work is driven by the results in my [previous paper](/publications/conference-paper/) on LLMs.

> [!NOTE]
> Create your slides in Markdown - click the *Slides* button to check out the example.

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
