---
from: architect-agent
to: dev-agent
type: task-handoff
status: ready
priority: P1
created: 2026-05-18
---

## Task: Implement User Login API

## Context

The frontend team needs a login endpoint for the authentication flow. Architecture decisions were finalized in yesterday's design review.

## Requirements

- POST /api/auth/login accepts email + password
- Returns JWT token on success
- Returns 401 with error message on failure
- Rate limit: 5 attempts per minute per IP
- Log all login attempts (success + failure)

## Files Involved

- src/api/routes/auth.py — create new route file
- src/api/middleware/rate_limit.py — extend if exists
- src/auth/hash.py — use existing bcrypt wrapper
- src/auth/jwt.py — use existing JWT utility

## Constraints

- Follow existing route patterns in `src/api/routes/`
- Use the project's existing error response format
- Test user table already has hashed passwords

## Expected Output

- Working login endpoint with tests
- Updated project-state.md with status
- Bridge handoff to review-agent when ready
