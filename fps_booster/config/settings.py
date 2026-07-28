"""
FPS Booster Configuration Module
Stores system optimization settings and paths
"""

import os

# Application paths
APP_NAME = "RealFPSBooster"
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

# System optimization settings
OPTIMIZATION_SETTINGS = {
    "power_plan": "High Performance",
    "disable_game_mode": False,  # Keep game mode enabled
    "disable_fullscreen_optimizations": True,
    "priority_class": "High",
    "disable_background_apps": True,
    "clean_standby_list": True,
}

# Hardware detection thresholds
THRESHOLDS = {
    "low_ram_gb": 8,
    "recommended_ram_gb": 16,
    "low_cpu_cores": 4,
    "recommended_cpu_cores": 8,
}

# Windows registry paths for optimizations (Windows only)
WINDOWS_REGISTRY_PATHS = {
    "game_dvr": r"Software\Microsoft\Windows\CurrentVersion\GameDVR",
    "graphics_scheduling": r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers",
}
