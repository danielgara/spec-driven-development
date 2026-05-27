# Data Model: Book Discovery and Browsing

## Entity: Book

Represents a single catalog entry shown on homepage, list, and detail screens.

### Fields

- `id` (string or int, required, unique): stable identifier used in URL routing.
- `title` (string, required): display title and search target field.
- `author` (string, required): primary author display value.
- `category` (string, required): category label used for filtering.
- `description` (string, optional): longer summary shown on detail pages.
- `featured` (boolean, required): flag controlling homepage featured list.

### Validation Rules

- `id` MUST be unique across all books.
- `title` MUST be non-empty after trimming whitespace.
- `category` MUST be non-empty and normalized for comparison in filtering.
- `featured` defaults to `false` if absent in source data.

## Entity: Category

Logical grouping derived from `Book.category` values in the dataset.

### Fields

- `name` (string, required, unique in generated category list)

### Validation Rules

- Category names are treated case-insensitively for filtering comparisons.

## Entity: Catalog Query

Represents user-selected browse criteria from query parameters.

### Fields

- `q` (string, optional): title keyword search term.
- `category` (string, optional): selected category filter.

### Validation Rules

- Empty or whitespace-only values are treated as unset.
- Unknown categories are allowed but return an empty result list.

## Relationships

- One `Category` to many `Book` entries (derived relationship).
- One `Catalog Query` produces zero-to-many `Book` results.

## State Transitions

This feature is read-only for end users; no create/update/delete transitions are in scope.
