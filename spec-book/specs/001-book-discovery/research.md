# Research: Book Discovery and Browsing

## Decision 1: Use Python file-backed data source

- **Decision**: Store sample books in a Python module as a list of dictionaries and load
  them directly in application services/helpers.
- **Rationale**: The constitution explicitly prohibits database usage and requires a
  simple educational architecture.
- **Alternatives considered**:
  - JSON file storage: readable but less Python-native for this constrained setup.
  - SQLite/ORM: rejected due to constitutional prohibition.

## Decision 2: Split class-based views by action module

- **Decision**: Create a `views` package with one class per module:
  `home_view.py`, `book_list_view.py`, `book_detail_view.py`.
- **Rationale**: Satisfies one-class-per-action rule and makes code easier to teach and
  maintain.
- **Alternatives considered**:
  - Single `views.py` with multiple classes: rejected by constitution.
  - Function-based views: rejected by constitution.

## Decision 3: Perform search and category filter in list view query handling

- **Decision**: Use query parameters (`q`, `category`) on the catalog endpoint; apply
  filtering in memory against the file-backed dataset.
- **Rationale**: Keeps URL behavior intuitive and avoids extra complexity while supporting
  combined search/filter behavior from the spec.
- **Alternatives considered**:
  - Separate search endpoint: unnecessary complexity for current scope.
  - Client-side filtering only: would weaken server-side behavior validation.

## Decision 4: Template inheritance with Bootstrap CDN

- **Decision**: Build `base.html` with shared navigation and Bootstrap CDN; extend it from
  homepage, list, and detail templates.
- **Rationale**: Meets constitution and reduces duplication.
- **Alternatives considered**:
  - Per-page standalone templates: rejected due to repetition.
  - Local Bootstrap assets/build pipeline: rejected for unnecessary setup complexity.

## Decision 5: Validate behavior with Django test client

- **Decision**: Use Django tests to verify route status, filtering behavior, empty states,
  and not-found detail handling.
- **Rationale**: Fast feedback loop and good educational coverage for MVT behavior.
- **Alternatives considered**:
  - Manual-only verification: insufficient for regression safety.
  - Browser E2E tooling: unnecessary overhead for this feature size.
