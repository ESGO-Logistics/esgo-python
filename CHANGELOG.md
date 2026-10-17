# Changelog

All notable changes to this package are documented here. Versions follow
[Semantic Versioning](https://semver.org/). Before 1.0, minor versions may
contain breaking changes; they are marked as such.

## 0.1.0 (unreleased)

All endpoints of API v1.

- New: `matches.search(...)`, `open_requests.create(...)`,
  `open_requests.list_matches(request_id)`, in both call styles.
- **Breaking:** responses are typed objects from `esgo.models` instead of
  `dict` (`me.account_role` instead of `me["account_role"]`); `.to_dict()`
  returns the old form.
- **Breaking:** requires Python 3.11 or newer (was 3.10).
- Unknown or missing keyword arguments raise `TypeError` before any request.
- Exceptions show as `esgo.RateLimitError` etc. in tracebacks.
- New dependency: `attrs`. Models are generated from the OpenAPI spec with
  openapi-python-client (`scripts/generate.py`).

## 0.0.1 (2026-10-17)

First pre-release.

- `esgo.Client(api_key=...)` and the global style `esgo.api_key = ...`.
- `me.retrieve()` (`GET /v1/me`), returns the response as a `dict`.
- Typed exceptions for the ESGO error envelope (`AuthenticationError`,
  `RateLimitError` with `retry_after`, ...).
