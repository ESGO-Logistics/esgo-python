# Changelog

All notable changes to this package are documented here. Versions follow
[Semantic Versioning](https://semver.org/). Before 1.0, minor versions may
contain breaking changes; they are marked as such.

## 0.0.1 (2026-10-17)

First pre-release.

- `esgo.Client(api_key=...)` and the global style `esgo.api_key = ...`.
- `me.retrieve()` (`GET /v1/me`), returns the response as a `dict`.
- Typed exceptions for the ESGO error envelope (`AuthenticationError`,
  `RateLimitError` with `retry_after`, ...).
