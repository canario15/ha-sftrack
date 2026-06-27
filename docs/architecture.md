# Architecture

## Overview

```text
                Home Assistant
                      │
                      ▼
               Config Flow
                      │
                      ▼
               Config Entry
                      │
                      ▼
             SafeTrackApi (SDK)
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
   Device          Track           Alarm
    Model          Model           Model
      │               │               │
      └───────────────┼───────────────┘
                      ▼
                Home Assistant
                Device Registry
                      │
                      ▼
                    Entities
```

## Layers

### Home Assistant

Responsible for:

- Configuration Flow
- Coordinator
- Device Registry
- Entities

### SDK

Responsible for:

- HTTP communication
- Authentication
- Response validation

### Parsers

Responsible for converting SafeTrack JSON into Python models.

### Models

Represent the SafeTrack domain.

Examples:

- Device
- Track
- Alarm

## Design Principles

- Single Responsibility Principle
- Separation of concerns
- SDK independent from Home Assistant
- Strong typing
- Easy testing