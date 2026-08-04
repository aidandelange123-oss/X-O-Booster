"""
FPS Booster Configuration Module
Stores system optimization settings and paths
Enhanced with new features and configuration options
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
    
    # NEW: Additional Windows optimizations
    "disable_telemetry": True,
    "optimize_startup_apps": True,
    "enable_game_mode": True,
    "optimize_search": True,
    
    # NEW: Linux optimizations
    "disable_transparent_hugepages": True,
    "stop_irq_balance": True,
    "disable_desktop_effects": True,
    
    # NEW: macOS optimizations
    "optimize_spotlight": True,
    "optimize_login_items": True,
}

# Hardware detection thresholds
THRESHOLDS = {
    "low_ram_gb": 8,
    "recommended_ram_gb": 16,
    "low_cpu_cores": 4,
    "recommended_cpu_cores": 8,
    "low_vram_mb": 2048,
    "recommended_vram_mb": 4096,
}

# Windows registry paths for optimizations (Windows only)
WINDOWS_REGISTRY_PATHS = {
    "game_dvr": r"Software\Microsoft\Windows\CurrentVersion\GameDVR",
    "graphics_scheduling": r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers",
    "telemetry": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection",
    "game_bar": r"Software\Microsoft\GameBar",
}

# GPU optimization settings
GPU_SETTINGS = {
    "nvidia": {
        "persistence_mode": True,
        "power_mizer": True,
        "low_latency_mode": True,
    },
    "amd": {
        "performance_profile": True,
        "hardware_scheduling": True,
    }
}

# Logging configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "datefmt": "%Y-%m-%d %H:%M:%S",
    "max_file_size_mb": 10,
    "backup_count": 5,
}

