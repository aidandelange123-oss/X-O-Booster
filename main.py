"""
FPS Booster - Main Application Entry Point
A real system optimizer to improve gaming performance
"""

import sys
import os

# Import from local modules directly since we are in the root directory
from utils.hardware import HardwareDetector
from core.optimizer import SystemOptimizer

# Only import GUI if tkinter is available
try:
    from gui.interface import FPSBoosterGUI
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []
    
    try:
        import psutil
    except ImportError:
        missing.append("psutil")
    
    try:
        import tkinter
    except ImportError:
        missing.append("tkinter")
    
    return missing


def run_cli_mode():
    """Run the application in command-line mode."""
    print("=" * 60)
    print("🚀 Real FPS Booster - Command Line Mode")
    print("=" * 60)
    print()
    
    # Initialize components
    print("Initializing hardware detector...")
    detector = HardwareDetector()
    
    print("Displaying hardware information...\n")
    hw_info = detector.get_system_report()
    perf_score = detector.get_performance_score()
    
    # Display hardware info
    print("=" * 60)
    print("HARDWARE INFORMATION")
    print("=" * 60)
    
    # CPU
    cpu = hw_info.get('cpu', {})
    print(f"\n⚙️  CPU: {cpu.get('model', 'Unknown')}")
    print(f"   Physical Cores: {cpu.get('physical_cores', 'N/A')}")
    print(f"   Logical Cores: {cpu.get('cores', 'N/A')}")
    
    # RAM
    ram = hw_info.get('ram', {})
    print(f"\n💾 RAM: {ram.get('total_gb', 'N/A')} GB Total")
    print(f"   Available: {ram.get('available_gb', 'N/A')} GB")
    print(f"   Used: {ram.get('used_gb', 'N/A')} GB ({ram.get('percent_used', 'N/A')}%)")
    
    # GPU
    gpu = hw_info.get('gpu', {})
    gpus = gpu.get('gpus', [])
    print(f"\n🎮 GPU:")
    if gpus:
        for i, gpu_name in enumerate(gpus, 1):
            print(f"   {i}. {gpu_name}")
    else:
        print("   No dedicated GPU detected")
    
    vram = gpu.get('vram_total')
    if vram:
        print(f"   Total VRAM: {round(vram, 2)} MB")
    
    # Performance Score
    print(f"\n📈 PERFORMANCE SCORE: {perf_score['score']}/100 ({perf_score['rating']})")
    
    if perf_score['recommendations']:
        print("\n💡 RECOMMENDATIONS:")
        for rec in perf_score['recommendations']:
            print(f"   • {rec}")
    
    print("\n" + "=" * 60)
    
    # Apply optimizations
    print("\n⚡ APPLYING SYSTEM OPTIMIZATIONS...")
    print("=" * 60)
    
    optimizer = SystemOptimizer()
    results = optimizer.apply_all_optimizations()
    
    report = optimizer.get_optimization_report()
    
    print(f"\n✅ Successfully Applied: {report['total_applied']}")
    print(f"❌ Failed: {report['total_failed']}")
    
    if report['applied']:
        print("\nAPPLIED OPTIMIZATIONS:")
        for opt in report['applied']:
            print(f"   ✓ {opt}")
    
    if report['failed']:
        print("\nFAILED OPTIMIZATIONS:")
        for opt in report['failed']:
            print(f"   ✗ {opt}")
    
    print("\n" + "=" * 60)
    print("⚠️  NOTE: Some optimizations may require administrator/root privileges.")
    print("⚠️  A system restart is recommended for changes to take full effect.")
    print("=" * 60)
    
    # RAM monitoring option
    print("\n🔍 RAM MONITOR")
    print("-" * 40)
    total = ram.get('total_gb', 0)
    used = ram.get('used_gb', 0)
    available = ram.get('available_gb', 0)
    percent = ram.get('percent_used', 0)
    
    print(f"Total: {total} GB | Used: {used} GB | Available: {available} GB")
    print(f"Usage: {percent}%")
    
    if percent < 50:
        print("Status: ✓ Healthy")
    elif percent < 80:
        print("Status: ⚠ Moderate")
    else:
        print("Status: ⚠️ HIGH - Consider closing applications")
    
    print("\n" + "=" * 60)
    print("Done! Your system has been optimized for better FPS.")
    print("=" * 60)


def run_gui_mode():
    """Run the application in GUI mode."""
    if not GUI_AVAILABLE:
        print("GUI mode is not available (tkinter not installed).")
        print("Falling back to CLI mode...\n")
        run_cli_mode()
        return
    
    # Check dependencies
    missing = check_dependencies()
    if missing:
        print("Error: Missing required dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        print("\nInstall them with: pip install " + " ".join(missing))
        print("\nNote: tkinter usually comes pre-installed with Python.")
        sys.exit(1)
    
    # Initialize components
    print("Starting FPS Booster GUI...")
    detector = HardwareDetector()
    optimizer = SystemOptimizer()
    
    # Create and run GUI
    app = FPSBoosterGUI(detector, optimizer)
    app.run()


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Real FPS Booster - Optimize your system for better gaming performance"
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in command-line mode (default: GUI mode)"
    )
    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Force command-line mode even if GUI is available"
    )
    
    args = parser.parse_args()
    
    if args.cli or args.no_gui:
        run_cli_mode()
    else:
        try:
            run_gui_mode()
        except Exception as e:
            print(f"GUI mode failed: {e}")
            print("Falling back to CLI mode...\n")
            run_cli_mode()


if __name__ == "__main__":
    main()
