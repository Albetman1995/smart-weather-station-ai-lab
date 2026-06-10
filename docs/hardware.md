
## Contenido para `docs/hardware_plan.md`

```markdown
# Hardware Plan

## Version

v0.0 — Initial hardware planning

## Goal

Build a low-cost weather station using simple electronic components and recycled materials.

## Candidate boards

| Board | Advantages | Notes |
|---|---|---|
| ESP32 | Wi-Fi, low cost, strong IoT ecosystem | Recommended option |
| Raspberry Pi Pico W | MicroPython, low power, simple | Good alternative |
| Raspberry Pi Zero | Linux, camera support, more powerful | Better for later phases |

## Initial sensors

| Sensor | Measures | Priority |
|---|---|---|
| BME280 | Temperature, humidity, pressure | High |
| DHT22 | Temperature, humidity | Medium |
| BH1750 | Light intensity | Medium |
| LDR | Basic light level | High for low-cost prototype |

## Recycled enclosure ideas

- Small plastic food container
- Cut PET bottle as rain shield
- Yogurt container as external cover
- Plastic mesh for ventilation
- Bottle caps as spacers or legs
- Fine mesh for insect protection

## Initial risks

- Direct sunlight can distort temperature readings
- Poor ventilation can affect humidity readings
- Rain protection must not block airflow
- Outdoor electronics need basic moisture protection
- Cheap sensors may be noisy or inaccurate