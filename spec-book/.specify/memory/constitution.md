<!--
Sync Impact Report
- Version change: N/A -> 1.0.0
- Modified principles:
  - Principle 1 -> I. Django MVT and Single-App Boundaries
  - Principle 2 -> II. File-Based Book Data Only (No Database)
  - Principle 3 -> III. Class-Based Views with One-Class-Per-Action Modules
  - Principle 4 -> IV. Template Reuse and Bootstrap-Only UI
  - Principle 5 -> V. Educational Simplicity and Readability
- Added sections:
  - Implementation Constraints
  - Development Workflow and Quality Gates
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (compatible, no update needed)
  - ✅ .specify/templates/spec-template.md (compatible, no update needed)
  - ✅ .specify/templates/tasks-template.md (compatible, no update needed)
- Follow-up TODOs: None
-->
# Book Management Platform Constitution

## Core Principles

### I. Django MVT and Single-App Boundaries
The system MUST use Django with the MVT pattern and MUST contain exactly one Django app
named `books`. New domain behavior MUST be implemented within this app instead of
creating additional apps or layers. This keeps architecture approachable for learners
while preserving clear separation between models-like data structures, views, and
templates.

### II. File-Based Book Data Only (No Database)
Persistent storage via Django ORM or any database backend MUST NOT be used. Book data
MUST be sourced from Python files containing lists of dictionaries with sample records.
Any read/write operations MUST operate through this file-backed approach only.
Rationale: the project emphasizes MVT flow and class-based view structure without adding
database setup complexity.

### III. Class-Based Views with One-Class-Per-Action Modules
All request handling MUST use class-based views. A single aggregated `views.py` file
MUST NOT be used. Each action (for example list, detail, create, update, delete) MUST
have exactly one class in its own module under a views package. URL routing MUST import
these explicit modules to keep action boundaries obvious and maintainable.

### IV. Template Reuse and Bootstrap-Only UI
The interface MUST use Django templates and include a reusable base layout template that
centralizes shared structure (head, navigation, footer, and style/script includes).
Styling MUST use Bootstrap via CDN and MUST avoid local framework builds for this
project. Shared UI fragments SHOULD use template inheritance and includes to minimize
duplication and improve instructional clarity.

### V. Educational Simplicity and Readability
Design decisions MUST favor clarity over abstraction. Code SHOULD be short, explicit,
and easy to follow by developers learning Django. Indirection, premature optimization,
and unnecessary framework additions MUST be avoided. Names, module structure, and view
responsibilities MUST remain consistent and self-explanatory.

## Implementation Constraints

- Authentication and authorization features MUST NOT be implemented.
- The project MUST remain centered on book management behavior only.
- Any new dependency MUST have a clear educational purpose and minimal setup cost.
- Error handling MUST be user-friendly and visible in templates without complex
  infrastructure.

## Development Workflow and Quality Gates

- Every specification and implementation plan MUST include a Constitution Check mapping
  decisions to these principles.
- Tasks MUST preserve one-class-per-action view modules and template inheritance usage.
- Reviews MUST verify: single `books` app, no database usage, class-based views only,
  separate view modules, reusable base template, and Bootstrap CDN usage.
- If a requirement conflicts with this constitution, the constitution takes precedence
  until formally amended.

## Governance

This constitution is the highest project authority for engineering and architectural
choices.

Amendments require:
- a documented rationale,
- explicit statement of impacted principles and templates, and
- a semantic version update in this file.

Versioning policy:
- MAJOR: incompatible principle removals or redefinitions,
- MINOR: new principle or materially expanded constraint,
- PATCH: clarifications that do not change required behavior.

Compliance review expectations:
- each planning cycle MUST perform a Constitution Check before implementation, and
- each pull request SHOULD include a short note confirming constitutional compliance.

**Version**: 1.0.0 | **Ratified**: 2026-05-27 | **Last Amended**: 2026-05-27
