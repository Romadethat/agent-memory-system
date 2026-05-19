# Daily Summary — 2026-05-18

## Completed

- Implemented POST /api/auth/login endpoint
- Added rate limiting middleware (5 req/min per IP)
- Created login audit logger (structured JSON)
- Wrote 12 unit tests for login flow
- Fixed email validation regex in validators.py

## Decisions Made

- JWT tokens with 24h expiry (not session-based)
- Rate limit tracked via in-memory store (not Redis — deferred)
- Login audit logs written to stdout (not file — handled by infra)

## Problems Found

- Email validator rejected `user+tag@domain.com` addresses
- Rate limit config was hardcoded — moved to env var

## Fixes Applied

- Updated regex in `src/auth/validators.py` to allow `+` in local part
- Added `RATE_LIMIT_PER_MINUTE` to env config
- PR #42 merged

## Blockers

- Still waiting on design team for reset-password mockup (due 2026-05-20)
- DevOps staging db credentials not received yet

## Next Actions

- Start password reset flow (blocked on mockup)
- Research email verification service options (SendGrid vs SES)
- Document JWT configuration in vault/

## Notes for Next Session

- Review design mockups when they arrive
- Consider moving rate limit store to Redis in future sprint
