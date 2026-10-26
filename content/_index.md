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
        <div class="not-prose" style="position:relative;left:50%;transform:translateX(-50%);width:min(1100px,92vw);">
        <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <div class="rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">🎙️</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">Speech & Multimodal AI</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Multilingual ASR, generative speech and language models, speech-driven avatar animation.</p>
        </div>
        <div class="rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">🙂</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">Emotion & HCI</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Emotion-aware, personalized, human-centered interaction.</p>
        </div>
        <div class="rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">🛡️</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">Security & Biometrics</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Voice anti-spoofing and speaker verification.</p>
        </div>
        <div class="rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-800/50">
        <div class="mb-3 text-3xl">❤️</div>
        <h3 class="m-0 mb-2 text-lg font-semibold leading-snug">AI for Healthcare</h3>
        <p class="m-0 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Speech, handwriting and gait biomarkers for patients affected by neurodegenerative and mental diseases.</p>
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
