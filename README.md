# X-O-Booster

A multi-file, organized Python application that provides real system optimizations to improve gaming FPS (frames per second). This is **not a simulation** - it applies actual system-level optimizations.

## 🚀 Quick Start for Google Colab

Perfect for AI/ML training! Copy and paste this code directly into your Google Colab notebook:

```python
# Clone the repository
!git clone https://github.com/yourusername/X-O-Booster.git
%cd X-O-Booster

# Install dependencies
!pip install psutil

# Run RAM/VRAM optimization with help guide
!python main.py --cli --help-cmd

# Apply all optimizations for AI training
!python main.py --cli
```

### Essential Commands for AI Training

```python
# Show complete help guide for RAM/VRAM management
!python main.py --help-cmd

# Optimize RAM before loading large datasets
!python main.py --cli

# Monitor RAM usage during training
!python main.py --cli | grep -A 10 "RAM MONITOR"
```

## Features

- 🖥️ **Hardware Detection**: Automatically detects your CPU, GPU, RAM, and disk information
- 🎮 **GPU VRAM Detection**: Detailed GPU information including:
  - Total, used, and free VRAM monitoring
  - Per-GPU details with driver versions
  - CUDA availability detection for NVIDIA GPUs
  - DirectX version detection (Windows)
  - Support for NVIDIA, AMD, and Intel GPUs
- ⚡ **GPU Optimization**: Intelligent GPU-specific optimizations:
  - NVIDIA: Persistence mode, power limit management, PowerMizer optimization
  - AMD: Performance profile tuning, compute mode optimization
  - VRAM-based recommendations for optimal gaming performance
- 📊 **Performance Scoring**: Get a performance score and recommendations for your system
- ⚡ **Real FPS Boost**: Applies genuine system optimizations including:
  - **CPU Boosters (2 New)**:
    - CPU Priority Optimization for better process scheduling
    - CPU Affinity Management for efficient core allocation
  - **GPU Boosters (3 New)**:
    - Low Latency Mode for reduced input lag
    - Texture Cache Optimization for faster texture loading
    - Shader Cache Enhancement to reduce stuttering
  - **System Optimizations**:
    - Power plan optimization (High Performance mode)
    - Game DVR disabling (Windows)
    - Background process reduction
    - Visual effects optimization
    - Network adapter optimization
    - CPU governor tuning (Linux)
    - Memory cache clearing
- 💾 **RAM Monitor**: Real-time RAM usage monitoring with visual indicators
- 🎨 **GUI Interface**: User-friendly graphical interface with tabs
- 💻 **CLI Mode**: Command-line interface for advanced users

## Project Structure

```
X-O-Booster/
├── main.py                 # Main entry point
├── __init__.py
├── config/
│   ├── __init__.py
│   └── settings.py         # Configuration settings
├── core/
│   ├── __init__.py
│   └── optimizer.py        # System optimization logic
├── utils/
│   ├── __init__.py
│   └── hardware.py         # Hardware detection utilities
├── gui/
│   ├── __init__.py
│   └── interface.py        # Graphical user interface
└── README.md
```

## Requirements

- Python 3.7+
- psutil (for detailed hardware monitoring)
- tkinter (usually pre-installed with Python)

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install psutil
```

3. Run the application:

**GUI Mode:**
```bash
python main.py
```

**CLI Mode:**
```bash
python main.py --cli
```

## Usage

### 🤖 Google Colab / AI Training Mode

For AI training and Google Colab environments, use the `/help` command to see all available RAM/VRAM optimization commands:

```python
# Show complete help guide
!python main.py --help-cmd
```

This displays:
- All available commands for RAM and VRAM optimization
- Google Colab best practices
- AI training notes for memory management

### GUI Mode

When you run the application in GUI mode, you'll see three tabs:

1. **Hardware Info**: View detailed information about your system hardware including CPU, GPU, RAM, and disk. Also shows a performance score with recommendations.

2. **Boost FPS**: Click the "BOOST FPS NOW" button to apply all available system optimizations. A progress bar shows the status, and results are displayed showing which optimizations were successfully applied.

3. **RAM Monitor**: Monitor your RAM usage in real-time with a visual indicator. You can also clear RAM cache (requires admin/root privileges on some systems).

### CLI Mode

Run the application with `--cli` flag for command-line output. It will:
- Display all hardware information including detailed GPU/VRAM stats
- Show performance score and recommendations
- Apply optimizations automatically (including GPU-specific optimizations)
- Display RAM status

### GPU Information Available

The hardware detection now provides comprehensive GPU information:
- **GPU Count & Names**: List of all detected GPUs
- **VRAM Metrics**: Total, used, and free VRAM in MB
- **Driver Version**: Installed GPU driver version
- **CUDA Support**: Detection of NVIDIA CUDA availability
- **DirectX Version**: DirectX version on Windows systems
- **Multi-GPU Support**: Works with NVIDIA, AMD, and Intel GPUs

## Optimizations Applied

### Windows
- ✅ High Performance power plan activation
- ✅ Game DVR disabling
- ✅ Fullscreen optimizations hint
- ✅ Background service reduction
- ✅ Visual effects optimization
- ✅ Network interrupt moderation disabling
- ✅ **CPU Boosters**:
  - CPU Priority Optimization (registry tweaks for better scheduling)
  - CPU Affinity Management (efficient core allocation)
- ✅ **GPU Boosters**:
  - Low Latency Mode (NVIDIA Ultra Low Latency)
  - Texture Cache Optimization (increased Direct3D texture memory)
  - Shader Cache Enhancement (Direct3D shader pre-caching)
- ✅ **GPU Optimization**: NVIDIA persistence mode, PowerMizer enablement, AMD hardware scheduling recommendations

### Linux
- ✅ CPU governor set to performance mode (requires root)
- ✅ Swappiness reduction (requires root)
- ✅ Process priority optimization tips
- ✅ Compositor disabling tips
- ✅ RAM cache clearing (requires root)
- ✅ **CPU Boosters**:
  - CPU Priority suggestions (nice command guidance)
  - CPU Affinity management (taskset support with root)
- ✅ **GPU Boosters**:
  - Low Latency Mode (NVidia NVENC or AMD AFMF recommendations)
  - Texture Cache (OpenGL cache optimization tips)
  - Shader Cache (Vulkan pipeline library support)
- ✅ **GPU Optimization**: NVIDIA persistence mode & power limits, AMD performance profile tuning

### macOS
- ✅ Power settings optimization
- ✅ Visual effects reduction
- ✅ **CPU Boosters**:
  - CPU Priority (automatic handling by macOS)
  - CPU Affinity (automatic core management)
- ✅ **GPU Boosters**:
  - Low Latency Mode (Metal API automatic handling)
  - Texture Cache (Metal API automatic management)
  - Shader Cache (Metal compile-time shaders)

### GPU-Specific Optimizations
- **NVIDIA GPUs**: 
  - Persistence mode enabled for reduced latency
  - Power limit management for optimal performance
  - PowerMizer prefer maximum performance (Windows)
  - Ultra Low Latency mode support
- **AMD GPUs**:
  - Performance profile tuning (Linux)
  - Hardware-accelerated GPU scheduling recommendations (Windows)
  - AFMF (AMD Fluid Motion Frames) support recommendations
- **VRAM Monitoring**:
  - Low VRAM warnings for systems with <4GB
  - Optimal capacity confirmation for systems with ≥8GB

## Important Notes

⚠️ **Administrator/Root Privileges**: Some optimizations require elevated privileges. Run as administrator (Windows) or with sudo (Linux/macOS) for full functionality.

⚠️ **System Restart**: After applying optimizations, a system restart is recommended for all changes to take full effect.

⚠️ **Game-Specific Settings**: Some optimizations (like fullscreen optimizations) need to be applied per-game executable through the game's properties.

⚠️ **Results May Vary**: FPS improvements depend on your specific hardware configuration and the games you play. Typical improvements range from 5-20% depending on your system.

## Safety

This application only applies safe, reversible system optimizations. All optimizations are standard Windows/Linux/macOS settings that can be reset. The application does not:
- Modify game files
- Install drivers
- Make irreversible changes
- Overclock hardware

## Troubleshooting

**GUI doesn't open:**
- Ensure tkinter is installed: `pip install tk` (or reinstall Python with tkinter)
- Try running in CLI mode: `python main.py --cli`

**Google Colab Issues:**
- Make sure you've cloned the repository first: `!git clone <repo-url>`
- Install dependencies: `!pip install psutil`
- Use `--help-cmd` flag to see all available commands: `!python main.py --help-cmd`

**Optimizations fail:**
- Run the application as administrator/root
- Check the results section for specific error messages

**No FPS improvement:**
- Ensure you restarted your system after applying optimizations
- Some games may not show immediate improvements
- Check if your hardware meets the game's requirements

## License

This project is provided as-is for educational purposes. Use at your own discretion.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Made with ❤️ for gamers and AI researchers**

## 📚 Command Reference

### All Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `/help` | Show complete help guide for RAM/VRAM optimization | `python main.py --help-cmd` |
| `optimize ram` | Clear and optimize system RAM | Automatic in CLI mode |
| `clear vram` | Clear GPU VRAM cache | Automatic during optimization |
| `monitor ram` | Display RAM usage statistics | Shown in CLI output |
| `apply optimizations` | Apply all system optimizations | Automatic in CLI mode |

### Quick Command Examples

```bash
# Show help guide
python main.py --help-cmd

# Run full optimization (CLI mode)
python main.py --cli

# Run GUI mode
python main.py

# Force CLI mode even if GUI is available
python main.py --no-gui
```
