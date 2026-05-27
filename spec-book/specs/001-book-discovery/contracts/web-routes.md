# Web Routes Contract: Book Discovery and Browsing

## Overview

This document defines user-facing route contracts for the Django MVT book discovery
feature.

## Route: Homepage

- **Method**: `GET`
- **Path**: `/`
- **Purpose**: Show featured books section.
- **Inputs**: None
- **Success Behavior**:
  - Returns `200 OK`.
  - Renders featured books if available.
  - Renders empty-state message when no featured books exist.

## Route: Book Catalog

- **Method**: `GET`
- **Path**: `/books/`
- **Purpose**: Show list of books with optional search/filter behavior.
- **Inputs**:
  - Query `q` (optional): title keyword
  - Query `category` (optional): category label
- **Success Behavior**:
  - Returns `200 OK`.
  - With no query params: returns full catalog.
  - With `q`: returns books whose titles match keyword.
  - With `category`: returns books in category.
  - With both: returns intersection of both criteria.
  - If no matches: returns empty-state message in list view.

## Route: Book Detail

- **Method**: `GET`
- **Path**: `/books/<id>/`
- **Purpose**: Show complete details for a single book.
- **Inputs**:
  - Path `id` (required): book identifier
- **Success Behavior**:
  - Returns `200 OK` and full book data when id exists.
- **Failure Behavior**:
  - Returns `404 Not Found` and user-friendly message when id does not exist.

## Navigation Contract

- Base layout provides stable navigation links between homepage and catalog.
- Catalog entries provide links to detail pages.
- Not-found and empty-state views provide clear path back to browsing routes.
