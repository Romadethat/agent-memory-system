# Changelog

## [5.2.0] — 2026-05-20

### Added

- Agent Index System (section #29) — file-based navigation map for multi-project agents
- Boot protocol for session startups
- Search protocol for finding answers before asking
- Memory indexing system with P0-P3 priority levels
- Template system for projects, relays, tasks, decisions, and memories
- Inbox processing workflow (raw → needs-review → processed)
- Clutter prevention rules for maintaining a clean agent brain
- CLI integration pattern for index management

### Changed

- docs/full-reference-guide.md expanded from 45 to 46 sections
- README docs table updated

## [5.1.0] — 2026-05-20

### Added

- Cross-machine relay bridge documentation for Google Drive / cloud sync workflows
- Optional Multi-Agent Relay Ingestion Layer for cloud-to-local agent handoffs
- Canonical relay format guidance using plain `.md` or `.txt` files plus matching `.ready` markers
- Agent card guidance for multi-agent discovery
- Protocol file guidance for relay laws, naming conventions, message types, ready-marker rules, and safety rules
- Updated relay message header fields: Status, Protocol Version, Authority Level, No Secrets Included, and Real-World Action Authorized
- Documentation for the `.gdoc` limitation and the rclone-based ingestion fix

### Changed

- README now points users to the advanced relay bridge pattern
- docs/multi-agent-bridge.md now covers both local bridges and cross-machine relay ingestion

## [5.0.0] — 2026-05-18

### Major

- Complete repo polish for public launch
- Rewrote README with landing-page structure, badges, and quick start
- Added SECURITY.md with safe-usage guidance
- Added CONTRIBUTING.md with contribution guidelines
- Added CHANGELOG.md (this file)
- Created full examples/ directory with basic-agent-brain and multi-agent-bridge setups

### Added

- docs/windows-setup.md — Windows-specific setup guide
- docs/obsidian-setup.md — Optional Obsidian integration guide
- docs/multi-agent-bridge.md — Multi-agent coordination patterns
- docs/security-notes.md — Detailed security reference
- assets/ folder with placeholder structure for screenshots and diagrams
- Example project-state.md, user-rules.md, daily-log.md, bridge handoff files

### Changed

- .gitignore fully expanded with security and IDE patterns
- README structure revised — short and powerful, deep docs separated
- Scripts polished with --help, error handling, cross-platform path support
- requirements.txt cleaned up with clearer comments

### Scripts

- init-agent-brain.py: Added --help flag, better error messages, Windows path handling
- end_of_session.py: Added --help, summary argument, AGENT_BRAIN env var support

## [4.0.0] — 2026-05-17

### Added

- Starter kit scripts (init-agent-brain.py, end_of_session.py)
- Skills folder with example workflows
- Templates folder with AGENT_PROFILE, MEMORY_RULES, project-state, user-rules
- docs/full-reference-guide.md with 43-section deep reference
- docs/architecture.md with flow diagram

### Changed

- Full README rewrite with starter kit focus

## [3.0.0] — 2026-05-14

### Added

- Multi-agent bridge concept
- Bridge folder structure with inbox, outbound, done, blocked

## [2.0.0] — 2026-05-10

### Added

- Vault knowledge system
- Daily log system
- Project state file concept

## [1.0.0] — 2026-05-05

### Added

- Initial release — core memory system concept
- AGENT_PROFILE / SOUL.md idea
- Memory vs files principle
