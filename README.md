# f1_utils.py - FastF1 Telemetry Helper Functions

## This module contains utility functions for working with FastF1 Python library.

### compare_race_laps(): It automates session loading, telemetry comparison, and plots track dominance between two drivers for a given lap of the race.
- Visualizes
  - Side-by-side telemetry plots:
    - Brake Input
    - Speed (km/h)
    - DRS Activation
    - RPM
    - Gear Number
    - Throttle Input
  - Track dominance plot
 
### compare_fastest_laps(): It automates session loading, telemetry comparison, and plots track dominance between two drivers for their fastest  laps in a given session.

Example:

```
from f1_utils import compare_race_laps

compare_race_laps(year=2021, gp='abu dhabi', driver_1 = "VER", driver_2 = "HAM")

from f1_utils import compare_fastest_laps
compare_fastest_laps(year=2021, gp='abu dhabi',session_type: str = 'Q', driver_1 = "VER", driver_2 = "HAM")
```
![telemetry](https://github.com/user-attachments/assets/8f4e12de-2478-4b6c-9080-dc1e2c4b4344)

![td](https://github.com/user-attachments/assets/8e963aeb-7749-409b-9dbf-35b035d5567e)

# pia_nor_quali_comparison.ipynb - Piastri vs Norris 2025 Qualifying Lap Comparison

## This Jupyter Notebook compares the fastest qualifying laps of Oscar Piastri and Lando Norris during the 2025 season. It uses the helper functions created in `f1_utils.py`
