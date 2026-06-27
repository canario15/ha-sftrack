# ha-sftrack

# SafeTrack for Home Assistant

A custom Home Assistant integration for the SafeTrack GPS platform.

This integration allows Home Assistant to communicate with the SafeTrack REST API to monitor GPS devices such as tractors, trucks, harvesters, and other fleet vehicles.

> **Project status:** 🚧 Early development

## Features

### Current

- Configuration Flow
- API Key validation
- Multi-language support (English and Spanish)
- SafeTrack API client

### Planned

- Device discovery
- Device Tracker entities
- Sensors
  - Speed
  - Odometer
  - Today's distance
  - Battery
  - Last GPS update
  - Ignition status
- Historical playback
- Alarm entities
- Diagnostics
- HACS support

## Supported API

Current endpoints:

- `/api/v1/device/list`
- `/api/v1/device/detail`
- `/api/v1/track`
- `/api/v1/playback`
- `/api/v1/alarm/list`

## Installation

Currently under development.

## Roadmap

- [x] Project structure
- [x] Config Flow
- [x] API Key validation
- [x] SafeTrack API client
- [ ] Device discovery
- [ ] DataUpdateCoordinator
- [ ] Device Tracker
- [ ] Sensors
- [ ] Historical playback
- [ ] Alarms
- [ ] Tests
- [ ] HACS
- [ ] Documentation

## License

MIT