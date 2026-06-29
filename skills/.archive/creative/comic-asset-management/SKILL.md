---
name: comic-asset-management
description: Standardized workflow for indexing and managing comic book and sequential art assets.
---
# Comic Asset Management

Standardized workflow for indexing and managing comic book and sequential art assets within the project ecosystem.

## Protocol 1: Visual Audit
- Never trust file modification timestamps for sequence.
- Always perform a visual audit of the directory using `ls`.
- Confirm actual page numbers by reading the text inside the art (top-right corner).
- Treat visual marker discrepancies as the 'ground truth' over directory order.

## Protocol 2: Consistent Indexing
- Page 0: Reserved for Splash Covers / Title Cards.
- Page 1 to N: Sequential narrative pages.
- Naming format: `[Series]_[Episode]_Page[Num]_[Title].png`
- Use underscores instead of spaces.

## Protocol 3: Verification
- Always execute `vision_analyze` on comic pages to confirm the internal page marker before starting a multi-file rename operation.
- Use `ls` after renames to verify the final order is correct.

## References
- references/naming-convention.md: Exact string formatting rules for sequential assets.
