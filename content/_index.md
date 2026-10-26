---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: 'Research'
      text: |-
        My research centers on bridging theoretical deep learning with practical, human-centered applications in speech processing, affective computing, audio security, and clinical health. A major foundation of my academic output focuses on biomedical signal processing, where I have pioneered multimodal deep learning architectures, transfer learning strategies, and digital health tools for the automated assessment and telemonitoring of neurodegenerative disorders like Parkinson’s and Alzheimer’s disease. 
        Building on this foundation, my current research interests include:

        <div class="not-prose" style="position:relative;left:50%;transform:translateX(-50%);width:min(1100px,92vw);">
        <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <div class="flex flex-col rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">🎙️</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">Speech & Multimodal AI</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Multilingual ASR, generative speech and language models, speech-driven avatar animation.</p>
        <div class="mt-auto flex flex-wrap gap-2 pt-4">
        <a href="tags/automatic-speech-recognition/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Automatic Speech Recognition</a>
        <a href="tags/large-language-models/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Large Language Models</a>
        <a href="tags/facial-avatar-animation/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Facial Avatar Animation</a>
        </div>
        </div>
        <div class="flex flex-col rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">🙂</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">Emotion & HCI</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Emotion-aware, personalized, human-centered interaction.</p>
        <div class="mt-auto flex flex-wrap gap-2 pt-4">
        <a href="tags/emotion-recognition/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Emotion Recognition</a>
        <a href="tags/affective-computing/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Affective Computing</a>
        <a href="tags/human-machine-interaction/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Human Machine Interaction</a>
        </div>
        </div>
        <div class="flex flex-col rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">🛡️</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">Security & Biometrics</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Voice anti-spoofing and speaker verification.</p>
        <div class="mt-auto flex flex-wrap gap-2 pt-4">
        <a href="tags/biometrics/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Biometrics</a>
        <a href="tags/antispoofing/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Antispoofing</a>
        <a href="tags/digital-security/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Digital Security</a>
        </div>
        </div>
        <div class="flex flex-col rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">❤️</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">AI for Healthcare</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Speech, handwriting and gait biomarkers for patients affected by neurodegenerative and mental diseases.</p>
        <div class="mt-auto flex flex-wrap gap-2 pt-4">
        <a href="tags/pathological-speech-processing/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Pathological Speech Processing</a>
        <a href="tags/parkinsons-disease/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Parkinson's Disease</a>
        <a href="tags/alzheimers-disease/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Alzheimer's Disease</a>
        <a href="tags/gait-processing/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Gait Processing</a>
        <a href="tags/handwriting-processing/" class="rounded-full border border-gray-300 px-3 py-1 text-xs no-underline hover:border-primary-500 hover:text-primary-600 dark:border-gray-600">Handwriting Processing</a>
        </div>
        </div>
        </div>
        </div>
    design:
      columns: '1'
  - block: collection
    id: publications
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 3
  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation


  - block: collection
    id: projects
    content:
      title: Recent Projects
      filters:
        folders:
          - projects
    design:
      view: card

  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 3
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
