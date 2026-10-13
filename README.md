# F1 Telemetry Backend

A lightweight FastAPI backend that exposes simulated Formula 1 lap-time telemetry for charts and dashboards. It is designed to provide a simple, reliable API for frontend applications without requiring a full telemetry database or external service.

## Features

- FastAPI application with CORS enabled for browser-based clients
- Root health check endpoint
- `/lap-times` endpoint for generating sample lap-time data by season, driver, and track
- Universal fallback logic for unknown tracks or drivers
- Realistic lap-time variations and degradation simulation

## Tech Stack

- Python
- FastAPI
- Uvicorn
- pandas
- fastf1

## Project Structure

```text
.
├── main.py
├── requirements.txt
└── README.md
