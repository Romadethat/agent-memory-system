# Code Review Checklist — Skill

## When to Use
Before committing, merging, or deploying code changes.

## Checklist

### Quality
- [ ] Does the code actually work? (test it)
- [ ] Are edge cases handled? (empty, null, error states)
- [ ] Is there dead code, commented code, or debug prints?
- [ ] Are error messages helpful?

### Security
- [ ] No hardcoded secrets, tokens, or passwords
- [ ] No command injection vectors
- [ ] Input validation present

### Performance
- [ ] No obvious inefficiencies (N+1 queries, unnecessary loops)
- [ ] Resources released (file handles, connections)
- [ ] Not loading entire files into memory unnecessarily

### Maintainability
- [ ] Consistent naming with rest of project
- [ ] Functions do one thing
- [ ] No magic numbers (use named constants)
- [ ] Comments explain WHY, not WHAT

### Convention
- [ ] Follows project style (indentation, naming, format)
- [ ] No lint errors
- [ ] Respects existing patterns in the codebase
