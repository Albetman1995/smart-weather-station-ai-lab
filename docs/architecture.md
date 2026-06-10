# System Architecture

## Version

v0.0 — Initial architecture draft

## Concept

The Smart Weather Station AI Lab will be built as a modular system that connects physical environmental sensors with Python-based data analysis and future AI models.

## Initial data flow

```text
[Environmental Sensors]
        ↓
[Microcontroller: ESP32 / Raspberry Pi Pico W]
        ↓
[Serial / Wi-Fi Data Transfer]
        ↓
[PC Python Environment]
        ↓
[CSV Dataset]
        ↓
[Data Analysis Notebooks]
        ↓
[Machine Learning Models]
        ↓
[Reports and Visualizations]