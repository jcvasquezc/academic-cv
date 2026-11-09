---
title: "SIBERIA - Self-Sovereign Identity with Biometric Encrypted and Robust Integrated Authentication"
date: 2024-06-19T00:00:00Z
summary: "Decentralized digital identity management framework combining Self-Sovereign Identity (SSI) with spoofing-aware speaker verification (SASV) and continuous behavioral authentication."

tags:
- Self-Sovereign Identity (SSI)
- Digital Wallet
- Digital Security
- Voice Biometrics
- Speaker Verification
- Homomorphic Encryption

publications:
  - paredes-2025-siberia
---

The **SIBERIA** project developed an integrated, user-controlled digital identity management platform that combines Self-Sovereign Identity (SSI), multi-factor verification, and privacy-preserving biometrics. Designed to eliminate the vulnerabilities inherent in centralized credential repositories, the architecture grants users direct ownership over their digital identity, ensuring that biometric verification can occur securely without exposing raw biometric data to third-party services.

In the project, I was part of the core team responsible for developing and evaluating the **Spoofing-Aware Speaker Verification (SASV)** module. My work focused on engineering the deep learning pipelines for speaker verification and anti-spoofing countermeasures, integrating homomorphic cryptographic routines to verify voiceprints in the encrypted domain, and validating system robustness against synthetic speech and audio deepfakes.

Beyond voice biometrics, the SIBERIA platform integrates two complementary security layers to deliver holistic identity lifecycle management:

* **Self-Sovereign Identity (SSI) & Decentralized Wallet:** Built on European Blockchain Services Infrastructure (EBSI) principles, using a private EOSIO blockchain as a decentralized trust registry for verifiable credential status and issuer verification without storing any personal user data.
* **Continuous Behavioral Authentication:** A passive monitoring engine that analyzes keyboard and mouse telemetry (cursor trajectory, speed, keystroke intervals), detecting anomalous session takeovers in real time without extra hardware.

### Project Video

<div class="not-prose my-6 aspect-video w-full max-w-3xl mx-auto overflow-hidden rounded-xl shadow-lg">
  <iframe 
    class="w-full h-full"
    src="https://www.youtube-nocookie.com/embed/zCH3ackv0Ck" 
    title="SIBERIA Project Video" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
  </iframe>
</div>

{{< related-publications >}}

---

> **Funding Acknowledgment:**  
> This research was developed as a Multi-Area Internal Project (MIP) within Vicomtech.

