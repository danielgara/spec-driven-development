# Tasks: Book Discovery and Browsing

**Input**: Design documents from `/specs/001-book-discovery/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md,
data-model.md, contracts/

**Tests**: Tests are not included as standalone tasks because explicit TDD/test-task
generation was not requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and
testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and baseline Django structure

- [X] T001 Create Django project scaffold in `books/manage.py` and `books/books_project/`
- [X] T002 Create single Django app `books/books/` and register it in
      `books/books_project/settings.py`
- [X] T003 [P] Create view package scaffolding in `books/books/views/__init__.py`
- [X] T004 [P] Create template directories in `books/books/templates/books/`
- [X] T005 [P] Create data package scaffolding in `books/books/data/__init__.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be
implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create file-backed sample dataset in `books/books/data/books_data.py`
- [X] T007 Create data access and filtering helpers in `books/books/services/book_service.py`
- [X] T008 Configure root URL routing in `books/books_project/urls.py`
- [X] T009 Create app URL routes in `books/books/urls.py`
- [X] T010 Create reusable base template with Bootstrap CDN in
      `books/books/templates/books/base.html`
- [X] T011 Add shared navigation partial in `books/books/templates/books/partials/nav.html`
- [X] T012 Create custom 404 template in `books/books/templates/404.html`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Browse and Discover Books (Priority: P1) 🎯 MVP

**Goal**: Users can browse all books and narrow results by title search and category
filter

**Independent Test**: Open `/books/`, verify full list, apply `q` and `category` query
params, verify filtered results and empty state behavior

### Implementation for User Story 1

- [X] T013 [US1] Implement catalog class-based view in `books/books/views/book_list_view.py`
- [X] T014 [US1] Wire catalog route in `books/books/urls.py`
- [X] T015 [US1] Create catalog template in `books/books/templates/books/book_list.html`
- [X] T016 [P] [US1] Add reusable filter form partial in
      `books/books/templates/books/partials/book_filters.html`
- [X] T017 [US1] Implement no-results empty-state rendering in
      `books/books/templates/books/book_list.html`
- [X] T018 [P] [US1] Add catalog page tests in `books/books/tests/test_list_search_filter.py`

**Checkpoint**: User Story 1 should be fully functional and independently testable

---

## Phase 4: User Story 2 - View Book Details (Priority: P2)

**Goal**: Users can open a selected book and view complete details with clear not-found
handling

**Independent Test**: Open a valid detail URL `/books/<id>/` and verify book metadata; open
an invalid id and verify user-friendly 404 behavior

### Implementation for User Story 2

- [X] T019 [US2] Implement detail class-based view in `books/books/views/book_detail_view.py`
- [X] T020 [US2] Wire detail route in `books/books/urls.py`
- [X] T021 [US2] Create detail template in `books/books/templates/books/book_detail.html`
- [X] T022 [US2] Implement not-found handling path in `books/books/views/book_detail_view.py`
- [X] T023 [P] [US2] Add detail page tests in `books/books/tests/test_detail.py`

**Checkpoint**: User Stories 1 and 2 should both work independently

---

## Phase 5: User Story 3 - See Featured Books on Homepage (Priority: P3)

**Goal**: Homepage highlights featured books and gracefully handles no-featured scenarios

**Independent Test**: Open `/`, verify only featured books are shown with links to detail
pages, or an empty-state message appears when none are featured

### Implementation for User Story 3

- [X] T024 [US3] Implement homepage class-based view in `books/books/views/home_view.py`
- [X] T025 [US3] Wire homepage route in `books/books_project/urls.py`
- [X] T026 [US3] Create homepage template in `books/books/templates/books/home.html`
- [X] T027 [US3] Implement featured empty-state rendering in
      `books/books/templates/books/home.html`
- [X] T028 [P] [US3] Add homepage tests in `books/books/tests/test_home.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T029 [P] Add template consistency cleanup in `books/books/templates/books/*.html`
- [X] T030 Verify URL-name consistency and reverse lookups in `books/books/urls.py` and
      `books/books_project/urls.py`
- [X] T031 Validate quickstart steps against implementation in
      `specs/001-book-discovery/quickstart.md`
- [X] T032 [P] Run full Django test suite and fix regressions in `books/books/tests/`
- [X] T033 Document final route behavior alignment in
      `specs/001-book-discovery/contracts/web-routes.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: Depend on Foundational phase completion
- **Polish (Phase 6)**: Depends on all implemented user stories

### User Story Dependencies

- **User Story 1 (P1)**: Starts after Foundational; no dependency on other stories
- **User Story 2 (P2)**: Starts after Foundational; reuses shared data/service layer
- **User Story 3 (P3)**: Starts after Foundational; reuses shared data/service layer

### Within Each User Story

- View implementation before route wiring
- Route wiring before template integration checks
- Story-specific verification before moving to next story

### Parallel Opportunities

- Phase 1: T003, T004, T005 can run in parallel
- Phase 3: T016 and T018 can run in parallel with non-overlapping files
- Phase 4: T023 can run in parallel once route and template contracts are stable
- Phase 5: T028 can run in parallel once homepage contract is stable
- Phase 6: T029 and T032 can run in parallel

---

## Parallel Example: User Story 1

```bash
Task: "T016 [US1] Add reusable filter form partial in books/books/templates/books/partials/book_filters.html"
Task: "T018 [US1] Add catalog page tests in books/books/tests/test_list_search_filter.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. Validate browse, search, and category filtering behavior on `/books/`

### Incremental Delivery

1. Deliver US1 (catalog browse/search/filter)
2. Deliver US2 (detail pages + not-found handling)
3. Deliver US3 (featured homepage)
4. Run polish phase and final verification

### Parallel Team Strategy

1. One developer finalizes shared foundation (Phases 1-2)
2. Then split by story:
   - Developer A: US1
   - Developer B: US2
   - Developer C: US3
3. Merge for Phase 6 polish and final validation

---

## Notes

- Task IDs are sequential and executable in listed order.
- All story tasks include `[US#]` labels and exact file paths.
- Architecture constraints are preserved: single app, class-based views, split view modules,
  file-backed data, and Bootstrap-based templates.
