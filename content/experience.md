---
title: 'Experience'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: resume-experience
    content:
      username: me
    design:
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: false
  # - block: resume-skills
  #   content:
  #     title: Skills & Hobbies
  #     username: me
  - block: resume-skills
    id: skills
    content:
      title: Skills & Expertise
      username: me
    design:
      columns: '1'
      css_class: 'skills-3col max-w-6xl mx-auto px-4 clear-both'
  - block: resume-awards
    content:
      title: Awards
      username: me
  - block: resume-languages
    content:
      title: Languages
      username: me
  - block: markdown
    content:
      text: |-
        <style>
          /* Force 3 columns on large screens for the resume-skills grid */
          @media (min-width: 1024px) {
            .skills-3col .grid {
              display: grid !important;
              grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
              gap: 2rem !important;
            }
            .skills-3col [class*="max-w-"] {
              max-width: 100% !important;
            }
          }
        </style>
---
