# f1_utils.py - FastF1 Telemetry Helper Functions

## This module contains utility functions for working with FastF1 Python library.

### compare_laps(): It automates session loading, lap time analysis, circuit plotting, and telemetry comparison between the fastest laps of two drivers during a session.
- Retrieves and compares the fastest laps of two drivers.
- Visualizes
  - Circuit layout
  - Side-by-side telemetry plots:
    - Brake Input
    - Speed (km/h)
    - DRS Activation
    - RPM
    - Gear Number
    - Throttle Input

Example:

```
from f1_utils import compare_laps

compare_laps(year=2021, gp='abu dhabi', session_type='Q', driver_1 = "VER", driver_2 = "HAM")
```

# pia_nor_quali_comparison.ipynb - Piastri vs Norris 2025 Qualifying Lap Comparison

## This Jupyter Notebook compares the fastest qualifying laps of Oscar Piastri and Lando Norris during the 2025 season. It uses the helper functions created in `f1_utils.py`
