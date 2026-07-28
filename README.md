# X-O-Booster

A multi-file, organized Python application that provides real system optimizations to improve gaming FPS (frames per second). This is **not a simulation** - it applies actual system-level optimizations.

## Features

- 🖥️ **Hardware Detection**: Automatically detects your CPU, GPU, RAM, and disk information
- 📊 **Performance Scoring**: Get a performance score and recommendations for your system
- ⚡ **Real FPS Boost**: Applies genuine system optimizations including:
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

### GUI Mode

When you run the application in GUI mode, you'll see three tabs:

1. **Hardware Info**: View detailed information about your system hardware including CPU, GPU, RAM, and disk. Also shows a performance score with recommendations.

2. **Boost FPS**: Click the "BOOST FPS NOW" button to apply all available system optimizations. A progress bar shows the status, and results are displayed showing which optimizations were successfully applied.

3. **RAM Monitor**: Monitor your RAM usage in real-time with a visual indicator. You can also clear RAM cache (requires admin/root privileges on some systems).

### CLI Mode

Run the application with `--cli` flag for command-line output. It will:
- Display all hardware information
- Show performance score and recommendations
- Apply optimizations automatically
- Display RAM status

## Optimizations Applied

### Windows
- ✅ High Performance power plan activation
- ✅ Game DVR disabling
- ✅ Fullscreen optimizations hint
- ✅ Background service reduction
- ✅ Visual effects optimization
- ✅ Network interrupt moderation disabling

### Linux
- ✅ CPU governor set to performance mode (requires root)
- ✅ Swappiness reduction (requires root)
- ✅ Process priority optimization tips
- ✅ Compositor disabling tips
- ✅ RAM cache clearing (requires root)

### macOS
- ✅ Power settings optimization
- ✅ Visual effects reduction

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

**Made with ❤️ for gamers**
