# Changelog - X-O-Booster

## [2.0.0] - 2026-08-04

### 🎉 Major New Features

#### Enhanced System Optimizations
- **Windows (4 new optimizations)**:
  - Windows Telemetry Disabling - Reduces background data collection
  - Startup Apps Optimization - Guidance for disabling unnecessary startup programs
  - Game Mode Enablement - Activates Windows Game Mode for better gaming performance
  - Windows Search Optimization - Reduces indexing overhead during gaming

- **Linux (3 new optimizations)**:
  - Transparent Hugepages Disabling - Improves latency for real-time applications
  - IRQ Balancing Optimization - Stops irqbalance service for consistent performance
  - Desktop Effects Guidance - Tips for disabling compositing while gaming

- **macOS (2 new optimizations)**:
  - Spotlight Optimization - Excludes game folders from indexing
  - Login Items Optimization - Guidance for removing unnecessary startup items

#### Core Improvements
- **Logging System**: Added comprehensive logging module (`utils/logger.py`)
  - Timestamped log files in `/logs` directory
  - Configurable log levels (DEBUG, INFO, WARNING, ERROR)
  - Automatic log rotation and cleanup
  
- **Configuration Enhancement**: Extended `config/settings.py`
  - GPU-specific optimization settings (NVIDIA/AMD)
  - Hardware detection thresholds for VRAM
  - Logging configuration options
  - All new optimization toggles

#### Code Quality Improvements
- Better error handling with detailed exception messages
- Improved code organization with clear section markers
- Enhanced logging throughout the optimization process
- Fallback mechanisms for missing dependencies

### 🔧 Bug Fixes & Improvements
- Fixed duplicate return statement in optimizer
- Improved cross-platform compatibility
- Better handling of read-only file systems
- Enhanced permission checking for root/admin operations
- More informative error messages for failed optimizations

### 📝 Documentation
- Updated README with new features
- Added CHANGELOG for version tracking
- Improved inline code documentation

---

## [1.0.0] - Previous Version

### Initial Features
- CPU Boosters (Priority & Affinity Management)
- GPU Boosters (Low Latency, Texture Cache, Shader Cache)
- System Optimizations (Power plan, Game DVR, Visual effects)
- Hardware Detection with VRAM monitoring
- GUI and CLI interfaces
- RAM Monitor with cache clearing
