# Implementation Plan: Book Discovery and Browsing

**Branch**: `001-book-discovery` | **Date**: 2026-05-27 | **Spec**: `specs/001-book-discovery/spec.md`

**Input**: Feature specification from `/specs/001-book-discovery/spec.md`

## Summary

Implement a Django MVT book management application that lets anonymous users browse
books, view detail pages, search by title, filter by category, and see featured books on
the homepage. The plan uses one Django app (`books`), class-based views split into
one-class-per-action modules, file-backed sample data (list of dictionaries), and
template inheritance with Bootstrap CDN.

## Technical Context

**Language/Version**: Python 3.11+, Django 5.x

**Primary Dependencies**: Django, Bootstrap 5 CDN (UI only)

**Storage**: Python file-based in-memory catalog (list of dictionaries), no database

**Testing**: Django `TestCase` + Django test client

**Target Platform**: Local development server and standard web browsers

**Project Type**: Single Django web application

**Performance Goals**: Search/filter/detail page render under 1 second for sample dataset
size

**Constraints**: No authentication, no ORM/database usage, one app named `books`,
class-based views only, no monolithic `views.py`

**Scale/Scope**: Educational/demo scope with a small static catalog (dozens to low
hundreds of books)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Django MVT and Single-App Boundaries**: PASS
  - Plan uses one app named `books` and standard Django MVT conventions.
- **II. File-Based Book Data Only (No Database)**: PASS
  - Data source is a Python file exposing a list of book dictionaries.
- **III. Class-Based Views with One-Class-Per-Action Modules**: PASS
  - Views package will split homepage, list/search/filter, and detail into separate
    modules with one class each.
- **IV. Template Reuse and Bootstrap-Only UI**: PASS
  - Base template is shared across all pages; Bootstrap is loaded via CDN in base layout.
- **V. Educational Simplicity and Readability**: PASS
  - Minimal service/data helpers, explicit routing, and straightforward templates.

Post-design re-check: PASS (design artifacts conform to all constitutional gates).

## Project Structure

### Documentation (this feature)

```text
specs/001-book-discovery/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── web-routes.md
└── tasks.md
```

### Source Code (repository root)

```text
books/
├── manage.py
├── books_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── books/
    ├── data/
    │   └── books_data.py
    ├── views/
    │   ├── home_view.py
    │   ├── book_list_view.py
    │   └── book_detail_view.py
    ├── templates/
    │   └── books/
    │       ├── base.html
    │       ├── home.html
    │       ├── book_list.html
    │       └── book_detail.html
    ├── urls.py
    └── tests/
        ├── test_home.py
        ├── test_list_search_filter.py
        └── test_detail.py
```

**Structure Decision**: Use a single Django project with one app `books` to satisfy
constitution constraints and keep architecture educational and maintainable.

## Complexity Tracking

No constitutional violations identified; complexity exceptions are not required.
