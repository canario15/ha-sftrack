# ADR-0001 - Create an independent SafeTrack SDK

## Status

Accepted

## Context

The Home Assistant integration needs to communicate with the SafeTrack REST API.

A common approach would be to place all HTTP requests directly inside the Home Assistant integration.

However, this tightly couples the API implementation with Home Assistant, making testing, reuse, and maintenance more difficult.

## Decision

Create an independent SDK responsible for:

- Authentication
- HTTP communication
- Response validation
- Parsing API responses into Python models

Home Assistant will only consume the SDK.

## Consequences

### Advantages

- Separation of concerns
- Easier testing
- Reusable outside Home Assistant
- Cleaner architecture
- Easier maintenance

### Disadvantages

- Slightly more files
- Additional abstraction layer

## Diagram

```text
Home Assistant
        │
        ▼
 SafeTrack SDK
        │
        ▼
 SafeTrack REST API