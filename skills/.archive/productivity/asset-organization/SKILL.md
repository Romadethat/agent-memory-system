---
name: asset-organization
description: Systematic renaming and classification of unstructured asset directories.
---

# Asset Organization and Labeling

A systematic approach to organizing and labeling unstructured folders of assets (images, concept art, references), especially when file names are generic like 'ChatGPT Image...'.

## Triggers
- Ro drops a folder full of generic filenames (ChatGPT, screenshot, image01).
- Ro says "look at them so you can title them properly" or "organize this."
- A project folder has cluttered, non-descriptive media assets.

## Workflow
1.  **Scan:** Use `terminal` with `ls -F` to list all files in the target directory.
2.  **Identify:** Use `vision_analyze` on representative samples to identify the subject (character, scene, wardrobe, pose).
3.  **Standardize:** Determine a naming convention based on the content (e.g., `<character_name>_<context>_<index_or_type>.png`).
    - Use clear, descriptive class names.
    - Keep filenames short, lowercase, and underscores instead of spaces.
4.  **Confirm:** Propose the rename plan to Ro clearly (List old -> new).
5.  **Execute:** Rename using a batch `terminal` command (prefer `mv` in bash).

## Pitfalls
- **Cost:** Don't analyze 100+ images individually if a single summary works. Analyze a subset first.
- **Ambiguity:** If multiple images aren't clearly unique, use index counters (01, 02) to maintain order.
- **Verification:** Always `ls` again after renaming to verify the folder state.

## Tip
- The goal is 'findable assets', not just 'renamed files'. Keep a project index for quick lookup if the folder grows large.
