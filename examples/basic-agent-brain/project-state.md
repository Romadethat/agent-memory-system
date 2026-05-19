# project-state.md — Example

*Last updated: 2026-05-18*

## Active Project

**MyApp** — A task management web application

## Current Priority

Complete the user authentication module (login, signup, password reset)

## Current Status

Login API endpoint implemented. Signup endpoint has a validation bug (email format check too strict). Password reset not started.

## Current Blockers

- Need to research how to handle email verification flow
- Waiting on design team for reset-password UI mockup

## Next Safe Task

Fix email validation regex in `src/auth/validators.py` — the current pattern rejects valid `+` addresses

## Waiting On

- Design team: reset-password mockup (due 2026-05-20)
- DevOps: test database credentials for staging

## Last Completed Task

Login endpoint — POST /api/auth/login — returns JWT on success

## Notes for Next Session

- The auth middleware is in `src/middleware/auth.py`
- Test user credentials are in `.env.test` (not committed)
- Consider rate limiting on login endpoint
