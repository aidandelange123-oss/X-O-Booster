"""
GUI Module for FPS Booster
Provides a user-friendly interface using tkinter
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from typing import Callable


class FPSBoosterGUI:
    """Graphical User Interface for the FPS Booster application."""
    
    def __init__(self, hardware_detector, optimizer):
        self.hardware_detector = hardware_detector
        self.optimizer = optimizer
        
        self.root = tk.Tk()
        self.root.title("Real FPS Booster - Optimize Your Gaming Performance")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colors
        self.bg_color = "#1a1a2e"
        self.fg_color = "#eaeaea"
        self.accent_color = "#0f3460"
        self.success_color = "#00ff88"
        self.warning_color = "#ffaa00"
        
        self.root.configure(bg=self.bg_color)
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TButton", background=self.accent_color, foreground=self.fg_color)
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup the user interface components."""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🚀 Real FPS Booster",
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.success_color
        )
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Tab 1: Hardware Info
        self.hw_frame = ttk.Frame(notebook, padding="20")
        notebook.add(self.hw_frame, text="📊 Hardware Info")
        self._setup_hardware_tab()
        
        # Tab 2: Boost FPS
        self.boost_frame = ttk.Frame(notebook, padding="20")
        notebook.add(self.boost_frame, text="⚡ Boost FPS")
        self._setup_boost_tab()
        
        # Tab 3: RAM Monitor
        self.ram_frame = ttk.Frame(notebook, padding="20")
        notebook.add(self.ram_frame, text="💾 RAM Monitor")
        self._setup_ram_tab()
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            main_frame,
            textvariable=self.status_var,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg=self.accent_color,
            fg=self.fg_color
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
    
    def _setup_hardware_tab(self):
        """Setup the hardware information tab."""
        # Refresh button
        refresh_btn = tk.Button(
            self.hw_frame,
            text="🔄 Refresh Hardware Info",
            command=self._refresh_hardware_info,
            bg=self.accent_color,
            fg=self.fg_color,
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2"
        )
        refresh_btn.pack(pady=(0, 15))
        
        # Hardware info display area
        info_container = ttk.Frame(self.hw_frame)
        info_container.pack(fill=tk.BOTH, expand=True)
        
        # Scrollable text area for hardware info
        self.hw_text = scrolledtext.ScrolledText(
            info_container,
            wrap=tk.WORD,
            width=80,
            height=25,
            bg="#16213e",
            fg=self.fg_color,
            font=("Consolas", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.hw_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Initial load
        self._refresh_hardware_info()
    
    def _setup_boost_tab(self):
        """Setup the boost FPS tab."""
        # Instructions
        instructions = tk.Label(
            self.boost_frame,
            text="Click 'Boost FPS' to apply real system optimizations for better gaming performance.\n\nIncludes:\n• 2 CPU Boosters: Priority Optimization & Affinity Management\n• 3 GPU Boosters: Low Latency Mode, Texture Cache & Shader Cache\n• System Optimizations: Power settings, background processes & more",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Arial", 10),
            justify=tk.CENTER
        )
        instructions.pack(pady=(0, 20))
        
        # Boost button
        self.boost_btn = tk.Button(
            self.boost_frame,
            text="🚀 BOOST FPS NOW",
            command=self._apply_boost,
            bg=self.success_color,
            fg="#000000",
            font=("Arial", 16, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            padx=30,
            pady=15
        )
        self.boost_btn.pack(pady=20)
        
        # Progress indicator
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.boost_frame,
            variable=self.progress_var,
            maximum=100,
            mode='determinate',
            length=400
        )
        self.progress_bar.pack(pady=10)
        
        # Results area
        results_container = ttk.LabelFrame(self.boost_frame, text="Optimization Results", padding="10")
        results_container.pack(fill=tk.BOTH, expand=True, pady=20)
        
        self.results_text = scrolledtext.ScrolledText(
            results_container,
            wrap=tk.WORD,
            width=70,
            height=15,
            bg="#16213e",
            fg=self.fg_color,
            font=("Consolas", 9),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
    
    def _setup_ram_tab(self):
        """Setup the RAM monitor tab."""
        # Refresh button
        refresh_btn = tk.Button(
            self.ram_frame,
            text="🔄 Refresh RAM Info",
            command=self._refresh_ram_info,
            bg=self.accent_color,
            fg=self.fg_color,
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2"
        )
        refresh_btn.pack(pady=(0, 15))
        
        # RAM info display
        ram_container = ttk.Frame(self.ram_frame)
        ram_container.pack(fill=tk.BOTH, expand=True)
        
        self.ram_text = scrolledtext.ScrolledText(
            ram_container,
            wrap=tk.WORD,
            width=80,
            height=20,
            bg="#16213e",
            fg=self.fg_color,
            font=("Consolas", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.ram_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Clear RAM button
        clear_ram_btn = tk.Button(
            self.ram_frame,
            text="🧹 Clear RAM Cache",
            command=self._clear_ram,
            bg=self.warning_color,
            fg="#000000",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            padx=20,
            pady=10
        )
        clear_ram_btn.pack(pady=20)
        
        # Initial load
        self._refresh_ram_info()
    
    def _refresh_hardware_info(self):
        """Refresh and display hardware information."""
        self.status_var.set("Detecting hardware...")
        self.root.update()
        
        try:
            # Re-detect hardware
            self.hardware_detector._detect_hardware()
            hw_info = self.hardware_detector.get_system_report()
            perf_score = self.hardware_detector.get_performance_score()
            
            # Clear previous content
            self.hw_text.delete(1.0, tk.END)
            
            # Format and display hardware info
            output = "=" * 60 + "\n"
            output += "HARDWARE INFORMATION REPORT\n"
            output += "=" * 60 + "\n\n"
            
            # OS Info
            output += "🖥️  OPERATING SYSTEM\n"
            output += "-" * 40 + "\n"
            os_info = hw_info.get("os", {})
            output += f"System: {os_info.get('system', 'N/A')}\n"
            output += f"Version: {os_info.get('version', 'N/A')}\n"
            output += f"Architecture: {os_info.get('machine', 'N/A')}\n"
            output += f"Python Version: {os_info.get('python_version', 'N/A')}\n\n"
            
            # CPU Info
            output += "⚙️  CPU INFORMATION\n"
            output += "-" * 40 + "\n"
            cpu_info = hw_info.get("cpu", {})
            output += f"Model: {cpu_info.get('model', 'N/A')}\n"
            output += f"Physical Cores: {cpu_info.get('physical_cores', 'N/A')}\n"
            output += f"Logical Cores: {cpu_info.get('cores', 'N/A')}\n"
            output += f"Frequency: {cpu_info.get('frequency', 'N/A')}\n\n"
            
            # RAM Info
            output += "💾 RAM INFORMATION\n"
            output += "-" * 40 + "\n"
            ram_info = hw_info.get("ram", {})
            output += f"Total RAM: {ram_info.get('total_gb', 'N/A')} GB\n"
            output += f"Available RAM: {ram_info.get('available_gb', 'N/A')} GB\n"
            output += f"Used RAM: {ram_info.get('used_gb', 'N/A')} GB\n"
            output += f"Usage: {ram_info.get('percent_used', 'N/A')}%\n\n"
            
            # GPU Info
            output += "🎮 GPU INFORMATION\n"
            output += "-" * 40 + "\n"
            gpu_info = hw_info.get("gpu", {})
            gpus = gpu_info.get("gpus", [])
            if gpus:
                for i, gpu in enumerate(gpus, 1):
                    output += f"GPU {i}: {gpu}\n"
            else:
                output += "No GPU detected\n"
            
            vram = gpu_info.get("vram_total")
            if vram:
                output += f"Total VRAM: {round(vram, 2)} MB\n"
            output += "\n"
            
            # Disk Info
            output += "💿 DISK INFORMATION\n"
            output += "-" * 40 + "\n"
            disk_info = hw_info.get("disk", {})
            output += f"Total Space: {disk_info.get('total_gb', 'N/A')} GB\n"
            output += f"Used Space: {disk_info.get('used_gb', 'N/A')} GB\n"
            output += f"Free Space: {disk_info.get('free_gb', 'N/A')} GB\n"
            output += f"Usage: {disk_info.get('percent_used', 'N/A')}%\n\n"
            
            # Performance Score
            output += "📈 PERFORMANCE SCORE\n"
            output += "=" * 40 + "\n"
            output += f"Score: {perf_score['score']}/100\n"
            output += f"Rating: {perf_score['rating']}\n\n"
            
            if perf_score['recommendations']:
                output += "💡 RECOMMENDATIONS:\n"
                for rec in perf_score['recommendations']:
                    output += f"  • {rec}\n"
            
            self.hw_text.insert(tk.END, output)
            self.status_var.set("Hardware info updated successfully")
            
        except Exception as e:
            self.hw_text.delete(1.0, tk.END)
            self.hw_text.insert(tk.END, f"Error detecting hardware: {str(e)}\n")
            self.status_var.set("Error detecting hardware")
    
    def _apply_boost(self):
        """Apply FPS boost optimizations."""
        self.boost_btn.config(state=tk.DISABLED)
        self.status_var.set("Applying optimizations...")
        
        # Run in separate thread to keep GUI responsive
        def boost_thread():
            try:
                # Reset progress
                self.progress_var.set(0)
                self.results_text.delete(1.0, tk.END)
                
                # Get GPU info for GPU-specific optimizations
                gpu_info = self.hardware_detector.get_system_report().get('gpu', {})
                
                # Apply optimizations with GPU info
                steps = 8
                for i in range(steps):
                    self.optimizer.apply_all_optimizations(gpu_info=gpu_info if gpu_info.get('gpus') else None)
                    progress = ((i + 1) / steps) * 100
                    self.progress_var.set(progress)
                    self.root.update_idletasks()
                
                # Get results
                report = self.optimizer.get_optimization_report()
                
                # Display results
                output = "=" * 60 + "\n"
                output += "OPTIMIZATION RESULTS\n"
                output += "=" * 60 + "\n\n"
                
                output += f"✅ Successfully Applied: {report['total_applied']}\n"
                output += f"❌ Failed: {report['total_failed']}\n\n"
                
                if report['applied']:
                    output += "APPLIED OPTIMIZATIONS:\n"
                    output += "-" * 40 + "\n"
                    for opt in report['applied']:
                        output += f"  ✓ {opt}\n"
                    output += "\n"
                
                if report['failed']:
                    output += "FAILED OPTIMIZATIONS:\n"
                    output += "-" * 40 + "\n"
                    for opt in report['failed']:
                        output += f"  ✗ {opt}\n"
                    output += "\n"
                
                output += "=" * 60 + "\n"
                output += "🚀 NEW FEATURES ADDED:\n"
                output += "-" * 40 + "\n"
                output += "  ⚡ 2 CPU Boosters:\n"
                output += "     • CPU Priority Optimization\n"
                output += "     • CPU Affinity Management\n"
                output += "  🎮 3 GPU Boosters:\n"
                output += "     • Low Latency Mode\n"
                output += "     • Texture Cache Optimization\n"
                output += "     • Shader Cache Enhancement\n"
                output += "=" * 60 + "\n"
                output += "⚠️ NOTE: Some optimizations may require administrator/root privileges.\n"
                output += "⚠️ A system restart is recommended for changes to take full effect.\n"
                output += "=" * 60 + "\n"
                
                self.results_text.insert(tk.END, output)
                self.status_var.set("Optimizations applied successfully!")
                
                messagebox.showinfo(
                    "Boost Complete",
                    f"Successfully applied {report['total_applied']} optimizations!\n\n"
                    "New: 2 CPU Boosters + 3 GPU Boosters added!\n"
                    "A system restart is recommended for best results."
                )
                
            except Exception as e:
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, f"Error applying optimizations: {str(e)}\n")
                self.status_var.set("Error applying optimizations")
                messagebox.showerror("Error", f"Failed to apply optimizations: {str(e)}")
            
            finally:
                self.boost_btn.config(state=tk.NORMAL)
        
        thread = threading.Thread(target=boost_thread, daemon=True)
        thread.start()
    
    def _refresh_ram_info(self):
        """Refresh and display RAM information."""
        self.status_var.set("Reading RAM information...")
        
        try:
            # Re-detect RAM
            self.hardware_detector._detect_hardware()
            hw_info = self.hardware_detector.get_system_report()
            ram_info = hw_info.get("ram", {})
            
            # Clear previous content
            self.ram_text.delete(1.0, tk.END)
            
            # Format and display RAM info
            output = "=" * 60 + "\n"
            output += "RAM MONITOR\n"
            output += "=" * 60 + "\n\n"
            
            total = ram_info.get('total_gb', 0)
            available = ram_info.get('available_gb', 0)
            used = ram_info.get('used_gb', 0)
            percent = ram_info.get('percent_used', 0)
            
            # Visual bar
            bar_length = 40
            filled = int((percent / 100) * bar_length)
            empty = bar_length - filled
            bar = "█" * filled + "░" * empty
            
            output += f"RAM Usage: [{bar}] {percent}%\n\n"
            output += f"Total Memory:     {total:>10.2f} GB\n"
            output += f"Used Memory:      {used:>10.2f} GB\n"
            output += f"Available Memory: {available:>10.2f} GB\n\n"
            
            # Recommendations
            output += "STATUS:\n"
            output += "-" * 40 + "\n"
            if percent < 50:
                output += "✓ RAM usage is healthy\n"
            elif percent < 80:
                output += "⚠ RAM usage is moderate\n"
            else:
                output += "⚠️ HIGH RAM USAGE - Consider closing applications\n"
            
            if total < 8:
                output += "⚠️ System has less than 8GB RAM - upgrade recommended\n"
            elif total >= 16:
                output += "✓ System has adequate RAM for gaming\n"
            
            self.ram_text.insert(tk.END, output)
            self.status_var.set("RAM info updated")
            
        except Exception as e:
            self.ram_text.delete(1.0, tk.END)
            self.ram_text.insert(tk.END, f"Error reading RAM: {str(e)}\n")
            self.status_var.set("Error reading RAM")
    
    def _clear_ram(self):
        """Clear RAM cache."""
        self.status_var.set("Clearing RAM cache...")
        
        try:
            success = self.optimizer.clean_ram()
            
            if success:
                self.status_var.set("RAM cache cleared!")
                messagebox.showinfo("Success", "RAM cache has been cleared!\nNote: Some systems may require administrator privileges for full cache clearing.")
                self._refresh_ram_info()
            else:
                self.status_var.set("Failed to clear RAM cache")
                messagebox.showwarning("Warning", "Could not clear RAM cache. This may require administrator/root privileges.")
        except Exception as e:
            self.status_var.set("Error clearing RAM")
            messagebox.showerror("Error", f"Failed to clear RAM: {str(e)}")
    
    def run(self):
        """Start the GUI application."""
        self.root.mainloop()
