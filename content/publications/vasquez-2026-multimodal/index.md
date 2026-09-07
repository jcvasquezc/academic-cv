---
title: "Multimodal Speech Recognition in High-Noise Factory Floors for Human Robot Collaboration"
authors:
- me
- Eneko Tomé
- Haritz Arzelus
- Ana Díaz de Zugazúa
- Sara Sillaurren
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

abstract: Natural language interaction in industrial settings is severely hindered by extreme acoustic noise, which makes standard Automatic Speech Recognition (ASR) systems unreliable. To enable flexible human-robot collaboration, there is a critical need for systems able to interpret operator commands under harsh conditions without requiring expert programming. This paper proposes a novel architecture that integrates an ASR module in parallel with a Visual Speech Recognition model to enhance transcription accuracy under adverse acoustic conditions. To resolve potential discrepancies between the two streams, a Large Language Model (LLM)-based post-processing module acts as a semantic arbitrator, evaluating the most probable transcription based on contextual and industrial task constraints. The framework was tested in an industrial scenario characterized by high non-stationary noise. The multimodal approach, combined with LLM-based arbitration, outperformed both unimodal ASR and VSR baselines across various scenarios. By combining auditory and visual cues with the reasoning capabilities of LLMs, this work provides a solution for hands-free robot programming in noisy manufacturing plants, bridging the gap between human intent and robotic execution.





# Summary. An optional shortened abstract.
tags:
- Automatic Speech Recognition
- Large Language Models
- Robotics

featured: true

hugoblox:
  ids:
    doi: https://doi.org/10.1007/978-3-032-37249-9_45

links: 
- type: source
  url: "https://link.springer.com/chapter/10.1007/978-3-032-37249-9_45"
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
  caption: 'Multimodal Speech Recognition'
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
