# Debugging Flow — Skill

## When to Use
When something isn't working and you need to find the root cause.

## Workflow

### 1. Reproduce
- What exact input causes the error?
- Is it consistent or intermittent?
- Screenshot the error if visual

### 2. Read the Error
- What's the exact error message?
- What line/number does it point to?
- Is it a known pattern (null ref, timeout, permission)?

### 3. Check Recent Changes
- What changed since it last worked?
- Check git log, file timestamps, config diffs

### 4. Isolate
- Can you reproduce in isolation (not in the full app)?
- Is the problem in the data or the code?

### 5. Fix + Verify
- Fix the root cause, not the symptom
- Verify fix: reproduce the original scenario and confirm it's gone
- Check for new bugs introduced by the fix

## Common Patterns

| Error | Likely Cause | Check |
|-------|-------------|-------|
| File not found | Wrong path | Absolute vs relative |
| Permission denied | File locked | Is another process using it? |
| Timeout | Too slow or hung | Is there a deadlock? |
| Null reference | Missing initialization | Was the object created? |
| Port in use | Previous instance still running | Kill the old process |
