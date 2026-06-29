---
name: comic-storyboard-org
description: Standardized workflow for organizing, labeling, and managing comic strip/art asset directories.
---
# Comic Storyboard Organization and Management

Standardized workflow for organizing, labeling, and managing comic strip/art asset directories.

## Workflow
1. **Asset Discovery**: Use `terminal` to list files.
2. **Visual Analysis**: Use `vision_analyze` on each image to determine:
   - Series title
   - Episode/Volume number
   - Page number (or index)
   - Visual content theme / Page title (e.g., 'Luxury Lemonade')
3. **Naming Convention**: Apply the canonical naming scheme: `<series>_Ep<n>_Page<n>_<Theme>.png`.
   - Use `Page0` for splash covers.
   - Example: `Vix_and_Carter_Ep1_Page2_Luxury_Lemonade.png`
4. **Execution**: Apply renames using `mv` in a single `terminal` call to maintain batch consistency.
5. **Verification**: Confirm counts and naming matches against the established index.

## Canonical Schemes
- Splash/Cover: `..._Page0_Splash_Cover.png`
- Content Pages: `..._Ep<n>_Page<n>_<Theme>.png`

## Best Practices
- Never manual-rename one-by-one.
- If content page titles are missing or ambiguous, use the narrative theme extracted via AI vision for the `<Theme>` field.
- Always run `ls` before and after to verify state.
- Keep the folder index clean; use directories per episode.