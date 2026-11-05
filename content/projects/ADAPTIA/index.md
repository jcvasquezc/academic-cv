---
title: "ADAPT-IA: Towards Adaptive AI in Language Technologies Applied to RIS3 Industrial Sectors"
date: 2023-04-01T00:00:00Z
summary: "Research and development of Adaptive AI and MLOps methodologies for Language Technologies in Basque, building robust ASR systems for in-cabin vehicle interaction inside driving simulators."

links:
  - type: site
    url: https://www.vicomtech.org/en/rdi-tangible/projects/project/towards-an-adaptive-ai-in-language-technologies-applied-to-industrial-sectors-ris3
tags:
  - Automatic Speech Recognition
  - Automotive & Mobility
  - Human Machine Interaction
  - MLOps

publications:
  - alvarez-2025-adapt
  - akcharov-2025-multilingual
---

The **ADAPT-IA** project addressed the research and development of Adaptive Artificial Intelligence paradigms, combining Active Learning, Transfer Learning, and Reinforcement Learning with Machine Learning Operations (MLOps) practices applied to Language Technologies (LT) for Basque across strategic industrial sectors. Its goal was to overcome the severe scarcity of annotated data in regional and technical domains, enabling continuous adaptation and deployment of neural speech and language models while keeping human expertise at the center of the learning loop.

As a speech researcher at Vicomtech, I was responsible for designing and developing automatic speech recognition (ASR) systems tailored to the automotive sector. Specifically, I built speech recognition models to enable natural voice interaction within vehicle cockpits, integrating and testing them within a controlled driving simulator in collaboration with the Automotive Intelligence Center (AIC) to ensure robust performance under challenging acoustic and operational conditions.

### Key Objectives and Technological Challenges

ADAPT-IA targeted critical scientific and operational bottlenecks at the intersection of Adaptive AI and industrial language processing:

* **Adaptive Speech Recognition for In-Cabin Environments:** Developing neural ASR models capable of adapting to restricted-domain automotive vocabularies, speaker variability, and cockpit background noise with minimal manually transcribed training data.
* **Active Learning and Data Curation:** Implementing active data selection strategies to identify the most informative speech samples for annotation, drastically reducing the cost and effort of continuous model retraining.
* **Interaction in Driving Simulators:** Deploying speech technologies in real-time simulation environments provided by AIC, evaluating vehicle-occupant communication and voice-activated controls without compromising driver focus or safety[cite: 114, 120, 137].
* **Low-Resource Language Adaptation (Basque):** Overcoming the lack of specialized industrial and automotive speech corpora in Basque through transfer learning and domain-specific terminology standardization[cite: 68, 69, 70, 80, 85].
* **Industrial MLOps Workflows:** Combining adaptive learning loops with automated MLOps pipelines to manage continuous data curation, model training, evaluation, and deployment in production[cite: 68, 69, 70, 84].

### Automotive Use Case & Simulator Demonstrator

Within the project's automotive track, AIC established an agile, controlled driving simulator testbed to evaluate voice communication systems in replicable driving scenarios. The speech recognition models developed for this demonstrator enabled seamless driver interaction, including hands-free infotainment, command-and-control, and cabin comfort settings, minimizing visual and cognitive distraction while benchmarking recognition accuracy under realistic vehicle dynamics.

### The Six ADAPT-IA Industrial Prototypes

Beyond the automotive track, ADAPT-IA demonstrated the versatility of Adaptive AI across four RIS3 sectors through six dedicated prototypes:

| Use Case | Sector | Description |
| :--- | :--- | :--- | :--- |
| **UC1: Speech-Based Driver Assistant** | Automotive | Multilingual (EUS/ENG) conversational voice assistant integrated into the AIC vehicle simulator. |
| **UC2: Technical Norm Assistant** | Machine Tool | Retrieval-Augmented Generation system for querying UNE machinery standards with INVEMA. |
| **UC3: Software Documentation Assistant** | Energy | Documentation exploration chatbot with the ACE cluster. |
| **UC4: PCB Assembling Guidance** | Energy |  Step-by-step assembly guidance system with memory mechanisms and technical illustration retrieval. |
| **UC5: CNC Voice Assistant** | Machine Tool | Voice-driven control system to extract CNC codes interfacing with Fagor Automation simulators |
| **UC6: Adaptive Machine Translation** | Cross-Sector (TRL 7) |  Terminology-constrained Basque-Spanish translation (ADAPTIA-MT suite) embedded into the Batua/Itzuli production ecosystem. |

---

### Consortium Partners

The project brought together applied research institutions, academic groups, and industrial cluster bodies:

* **Vicomtech Foundation** (Project Coordinator – Speech and Natural Language Technologies)
* **University of the Basque Country (UPV/EHU)** (SPIN Research Group – Dialogue Systems and Signal Processing)
* **UZEI** (Basque Center for Terminology and Lexicography - Linguistic Resources and Standardization)
* **Automotive Intelligence Center (AIC)** (Automotive Sector Use Case and Driving Simulator)
* **INVEMA / AFM Cluster** (Machine Tool and Advanced Manufacturing Cluster)
* **Basque Energy Cluster (ACE)** (Energy Sector Domain)
* **MAFEX** (Spanish Railway Association)

### Related Publications
{{< related-publications >}}

---

> **Funding Acknowledgment:**  
> This project received funding from the Department of Economic Development, Sustainability and Environment of the Basque Government through the ELKARTEK Collaborative Research Program, under grant agreement **No. KK-2023/00035**.