import importlib
import subprocess
import sys
import os

def install_and_import(package: str):
    """Install and import a Python package if not already installed."""
    try:
        return importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return importlib.import_module(package)


def compare_laps(year: int = 2021, gp: str = "abu dhabi", session_type: str = "Q", driver_1: str = 'VER', driver_2: str = 'HAM') -> None:
    """Compare the fastest laps of two drivers for a given F1 session
    Args:
        year (int): The season year (e.g. 2025)
        gp (str): Grand Prix name (e.g., 'monaco', 'silverstone')
        session_type (str): Session code ('FP1', 'FP2', 'FP3', 'Q', 'S', 'SS', 'SQ', 'R')
        driver_1 (str): Three-letter identifier for driver_1 (e.g., 'VER') 
        driver_2 (str): Three-letter identifier for driver_2 (e.g., 'HAM')
    """
    fastf1 = install_and_import("fastf1")
    plt = install_and_import("matplotlib.pyplot")

    # Create session 
    session = fastf1.get_session(year, gp, session_type)
    session.load()

    # Select fastest lap for driver_1 and driver_2
    laps_driver_1 = session.laps.pick_drivers(driver_1)
    laps_driver_2 = session.laps.pick_drivers(driver_2)

    fastest_lap_driver_1 = laps_driver_1.pick_fastest()
    fastest_lap_driver_2 = laps_driver_2.pick_fastest()

    # Retrieve telemetry data
    telemetry_driver_1 = fastest_lap_driver_1.get_telemetry().add_distance()
    telemetry_driver_2 = fastest_lap_driver_2.get_telemetry().add_distance()

    # Create dataframe for turns
    circuit_info = session.get_circuit_info()
    corners_df = circuit_info.corners.set_index('Number')
    corners = corners_df[['Distance']]

    # Plot the Circuit
    corner_pos = []
    for num, row in corners.iterrows():
        idx = (telemetry_driver_1['Distance'] - row['Distance']).abs().idxmin()
        pos = telemetry_driver_1.loc[idx, ['X', 'Y']]
        corner_pos.append((num, pos['X'], pos['Y']))

    # Draw track map
    plt.figure(figsize=(8,8))
    plt.plot(telemetry_driver_1['X'], telemetry_driver_1['Y'])

    # Plot turns
    for num, x, y, in corner_pos:
        plt.plot(x, y, 'o', color='red')
        plt.text(x, y, f'T{num}', color='green', fontsize=15)

    plt.axis('off')
    plt.title(f'{session.event.EventName} Map')

    ## Plot Telemetry Data
    plot_title = f"{session.event.year} {session.event.EventName} - {session.name} - {driver_1} vs {driver_2}"
    plt.rcParams['figure.figsize'] = [15,15]

    fig, ax = plt.subplots(6)

    for num, (i, row) in enumerate(corners.iterrows(), start=1):
        distance = row['Distance']
        for axis in ax:
            axis.axvline(x=distance, color='gray', linestyle='--', alpha=0.6)
            axis.text(distance, ax[0].get_ylim()[1]*0.95, f'T{num}', fontsize=8)

    ax[0].title.set_text(plot_title)
    # BrakeBalance trace
    ax[0].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1, color='red')
    ax[0].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2, color='blue')
    ax[0].set(ylabel = 'Brake')

    # CarSpeed trace
    ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1, color='red')
    ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2, color='blue')
    ax[1].set(ylabel = 'Speed [km/h]')

    # DRS Rear Wing Activated
    ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=driver_1, color='red')
    ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=driver_2, color='blue')
    ax[2].set(ylabel = 'DRS Activated')

    # EngineRevs trace
    ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1, color='red')
    ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2, color='blue')
    ax[3].set(ylabel = 'Revs per minute')

    # GearNumber trace
    ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1, color='red')
    ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2, color='blue')
    ax[4].set(ylabel = 'Gear Number')

    # Throttle trace
    ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1, color='red')
    ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2, color='blue')
    ax[5].set(ylabel = 'Throttle')

    ax[5].set(xlabel = "Distance [m]")
    plt.legend();

    # Print drivers' fastest lap and difference between them
    d1_fastest_lap = fastest_lap_driver_1.LapTime
    d2_fastest_lap = fastest_lap_driver_2.LapTime

    print(f'Piastri Fastest Qualifying Lap {d1_fastest_lap}')
    print(f'Norris Fastest Qualifying Lap {d2_fastest_lap}')

    fastest_lap_diff = (d1_fastest_lap - d2_fastest_lap).total_seconds()
    print(f'Difference In Lap time: {fastest_lap_diff} seconds')