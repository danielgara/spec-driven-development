# Quickstart: Book Discovery and Browsing

## Prerequisites

- Python 3.11+
- `pip` available in shell

## Setup

1. Create and activate a virtual environment.
2. Install Django:
   - `pip install django`
3. From repository root, navigate to the Django project directory (where `manage.py`
   lives).

## Run the Application

1. Start the development server:
   - `python manage.py runserver`
2. Open browser:
   - Homepage: `/`
   - Book catalog (list + search + filter): `/books/`
   - Book detail: `/books/<id>/`

## Manual Verification Checklist

1. Homepage displays featured books or a clear empty-state message.
2. Catalog page lists all books when no filters are set.
3. Searching by title keyword narrows results correctly.
4. Filtering by category narrows results correctly.
5. Combining search and category returns intersection results.
6. Clicking a book opens its detail page with full metadata.
7. Requesting a non-existing book id returns a user-friendly not-found response.

## Run Tests

- Execute: `python manage.py test`
- Expect tests for homepage, list/search/filter, and detail behavior to pass.
