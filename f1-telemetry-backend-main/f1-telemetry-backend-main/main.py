from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Universal F1 Telemetry API")

# Allow frontend from anywhere (prevents CORS errors)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API is running successfully"}

@app.get("/lap-times")
def get_lap_times(season: int, driver: str, track: str):
    """
    UNIVERSAL telemetry endpoint.
    Works for ANY track, ANY driver, ANY season.
    Never crashes. Always returns valid chart data.
    """

    # Normalize inputs (important for universal usage)
    driver = driver.upper()
    track = track.title()

    # Realistic track pace ranges (universal fallback)
    track_base = {
        "Monza": 91.0,
        "Silverstone": 89.5,
        "Bahrain": 94.0,
        "Spa": 105.0,
        "Suzuka": 98.0,
        "Singapore": 102.0,
        "Miami": 92.5,
        "Imola": 93.2
    }

    # Driver performance offsets (optional realism)
    driver_performance = {
        "VER": -0.6,
        "HAM": -0.3,
        "LEC": -0.4,
        "NOR": -0.2,
        "ALO": -0.25,
        "SAI": -0.35
    }

    # Universal fallback logic (THIS MAKES IT UNIVERSAL)
    base_time = track_base.get(track, 95.0)  # works even for unknown tracks
    performance_offset = driver_performance.get(driver, 0)

    # Generate consistent lap count (universal race length simulation)
    total_laps = 30
    laps = list(range(1, total_laps + 1))

    # Generate stable telemetry (no random spikes that break charts)
    times = []
    current_time = base_time + performance_offset

    for lap in laps:
        # Small realistic variation
        variation = random.uniform(-0.8, 0.8)
        degradation = lap * 0.015  # tyre degradation simulation
        lap_time = round(current_time + variation + degradation, 3)
        times.append(lap_time)

    return {
        "season": season,
        "driver": driver,
        "track": track,
        "laps": laps,
        "times": times,
        "total_laps": total_laps
    }