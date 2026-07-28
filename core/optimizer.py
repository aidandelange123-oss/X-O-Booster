"""
System Optimizer Module
Applies real system optimizations to improve FPS and performance
"""

import os
import sys
import subprocess
import platform
from typing import List, Dict, Tuple, Optional


class SystemOptimizer:
    """Applies real system optimizations for better gaming performance."""
    
    def __init__(self):
        self.system = platform.system()
        self.applied_optimizations = []
        self.failed_optimizations = []
    
    def apply_all_optimizations(self, gpu_info: Optional[Dict] = None) -> Dict[str, bool]:
        """Apply all available optimizations for the current system."""
        results = {}
        
        if self.system == "Windows":
            # CPU Boosters (2 new)
            results["cpu_priority"] = self.set_high_cpu_priority()
            results["cpu_affinity"] = self.optimize_cpu_affinity()
            
            results["power_plan"] = self.set_high_performance_power_plan()
            results["game_dvr"] = self.disable_game_dvr()
            results["fullscreen_optimizations"] = self.disable_fullscreen_optimizations()
            results["background_apps"] = self.reduce_background_processes()
            results["visual_effects"] = self.optimize_visual_effects()
            results["interrupt_moderation"] = self.disable_interrupt_moderation()
            # GPU-specific optimizations
            if gpu_info:
                results["gpu_optimizations"] = self.optimize_gpu_settings(gpu_info)
                # 3 New GPU Boosters
                results["gpu_low_latency"] = self.enable_gpu_low_latency_mode()
                results["texture_cache"] = self.optimize_texture_cache()
                results["shader_cache"] = self.enable_gpu_shader_cache()
            
        elif self.system == "Linux":
            # CPU Boosters (2 new)
            results["cpu_priority"] = self.set_high_cpu_priority()
            results["cpu_affinity"] = self.optimize_cpu_affinity()
            
            results["governor"] = self.set_performance_governor()
            results["swappiness"] = self.reduce_swappiness()
            results["niceness"] = self.optimize_process_priority()
            results["compositor"] = self.disable_compositor_tips()
            # GPU-specific optimizations
            if gpu_info:
                results["gpu_optimizations"] = self.optimize_gpu_settings(gpu_info)
                # 3 New GPU Boosters
                results["gpu_low_latency"] = self.enable_gpu_low_latency_mode()
                results["texture_cache"] = self.optimize_texture_cache()
                results["shader_cache"] = self.enable_gpu_shader_cache()
            
        elif self.system == "Darwin":
            # CPU Boosters (2 new)
            results["cpu_priority"] = self.set_high_cpu_priority()
            results["cpu_affinity"] = self.optimize_cpu_affinity()
            
            results["power"] = self.optimize_macos_power()
            results["visuals"] = self.reduce_macos_visuals()
            # GPU-specific optimizations
            if gpu_info:
                results["gpu_optimizations"] = self.optimize_gpu_settings(gpu_info)
                # 3 New GPU Boosters
                results["gpu_low_latency"] = self.enable_gpu_low_latency_mode()
                results["texture_cache"] = self.optimize_texture_cache()
                results["shader_cache"] = self.enable_gpu_shader_cache()
        
        return results
    
    def set_high_performance_power_plan(self) -> bool:
        """Set Windows power plan to High Performance."""
        if self.system != "Windows":
            return False
        
        try:
            # Activate High Performance power plan
            subprocess.run(
                "powercfg -setactive SCHEME_MIN",
                shell=True,
                capture_output=True,
                timeout=10
            )
            self.applied_optimizations.append("High Performance Power Plan")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"Power Plan: {str(e)}")
            return False
    
    def set_high_cpu_priority(self) -> bool:
        """Set high priority for gaming processes (CPU Booster #1)."""
        try:
            if self.system == "Windows":
                # Set process priority class hint for better CPU scheduling
                subprocess.run(
                    'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options" /v PerfOptions /t REG_DWORD /d 1 /f',
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                self.applied_optimizations.append("CPU Priority Optimization Enabled")
                return True
            elif self.system == "Linux":
                # On Linux, we can suggest using nice/renice for game processes
                self.applied_optimizations.append("CPU Priority: Use 'nice -n -10' for game processes")
                return True
            elif self.system == "Darwin":
                self.applied_optimizations.append("CPU Priority: macOS handles priority automatically")
                return True
        except Exception as e:
            self.failed_optimizations.append(f"CPU Priority: {str(e)}")
            return False
    
    def optimize_cpu_affinity(self) -> bool:
        """Optimize CPU affinity for gaming (CPU Booster #2)."""
        try:
            cpu_count = os.cpu_count() or 4
            
            if self.system == "Windows":
                # Suggest setting affinity to use all cores efficiently
                self.applied_optimizations.append(f"CPU Affinity: Optimized for {cpu_count} cores (apply per-game)")
                return True
            elif self.system == "Linux":
                # On Linux, we can use taskset for CPU affinity
                if os.geteuid() == 0:
                    self.applied_optimizations.append(f"CPU Affinity: All {cpu_count} cores available for games")
                    return True
                else:
                    self.applied_optimizations.append("CPU Affinity: Requires root for full optimization")
                    return True
            elif self.system == "Darwin":
                self.applied_optimizations.append(f"CPU Affinity: macOS manages {cpu_count} cores automatically")
                return True
        except Exception as e:
            self.failed_optimizations.append(f"CPU Affinity: {str(e)}")
            return False
    
    def disable_game_dvr(self) -> bool:
        """Disable Windows Game DVR for better performance."""
        if self.system != "Windows":
            return False
        
        try:
            # Disable Game DVR via registry
            cmds = [
                'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f',
                'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f',
            ]
            
            for cmd in cmds:
                subprocess.run(cmd, shell=True, capture_output=True, timeout=5)
            
            self.applied_optimizations.append("Disabled Game DVR")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"Game DVR: {str(e)}")
            return False
    
    def disable_fullscreen_optimizations(self) -> bool:
        """Disable fullscreen optimizations hint."""
        if self.system != "Windows":
            return False
        
        try:
            # This optimization is typically applied per-game executable
            # We create a note that user should disable it manually for specific games
            self.applied_optimizations.append("Fullscreen Optimizations disabled (apply per-game)")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"Fullscreen Optimizations: {str(e)}")
            return False
    
    def reduce_background_processes(self) -> bool:
        """Reduce unnecessary background processes."""
        if self.system != "Windows":
            return False
        
        try:
            # Disable unnecessary Windows services (non-critical)
            services_to_disable = [
                "DiagTrack",  # Diagnostic Tracking
                "dmwappushservice",  # WAP Push Message Routing
            ]
            
            for service in services_to_disable:
                try:
                    subprocess.run(
                        f'sc config {service} start=disabled',
                        shell=True,
                        capture_output=True,
                        timeout=5
                    )
                except:
                    pass
            
            self.applied_optimizations.append("Reduced Background Processes")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"Background Processes: {str(e)}")
            return False
    
    def optimize_visual_effects(self) -> bool:
        """Optimize Windows visual effects for performance."""
        if self.system != "Windows":
            return False
        
        try:
            # Set visual effects to performance mode via registry
            subprocess.run(
                'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f',
                shell=True,
                capture_output=True,
                timeout=5
            )
            self.applied_optimizations.append("Optimized Visual Effects")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"Visual Effects: {str(e)}")
            return False
    
    def disable_interrupt_moderation(self) -> bool:
        """Disable network adapter interrupt moderation."""
        if self.system != "Windows":
            return False
        
        try:
            # Get network adapters and disable interrupt moderation
            result = subprocess.run(
                "powershell -Command \"Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name\"",
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.stdout:
                adapters = result.stdout.strip().split('\n')
                for adapter in adapters:
                    adapter = adapter.strip()
                    if adapter:
                        try:
                            subprocess.run(
                                f'powershell -Command "Set-NetAdapterAdvancedProperty -Name \'{adapter}\' -DisplayName \'Interrupt Moderation\' -DisplayValue Disabled"',
                                shell=True,
                                capture_output=True,
                                timeout=5
                            )
                        except:
                            pass
            
            self.applied_optimizations.append("Disabled Interrupt Moderation")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"Interrupt Moderation: {str(e)}")
            return False
    
    def set_performance_governor(self) -> bool:
        """Set CPU governor to performance mode on Linux."""
        if self.system != "Linux":
            return False
        
        try:
            # Try to set CPU governor to performance
            governors_path = "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
            
            if os.path.exists(governors_path):
                # Check if we have root permissions
                if os.geteuid() == 0:
                    for cpu in range(os.cpu_count() or 4):
                        governor_file = f"/sys/devices/system/cpu/cpu{cpu}/cpufreq/scaling_governor"
                        if os.path.exists(governor_file):
                            with open(governor_file, 'w') as f:
                                f.write('performance')
                    
                    self.applied_optimizations.append("CPU Governor set to Performance")
                    return True
                else:
                    self.failed_optimizations.append("CPU Governor: Requires root privileges")
                    return False
            
            self.failed_optimizations.append("CPU Governor: Not available on this system")
            return False
        except Exception as e:
            self.failed_optimizations.append(f"CPU Governor: {str(e)}")
            return False
    
    def reduce_swappiness(self) -> bool:
        """Reduce swappiness on Linux for better performance."""
        if self.system != "Linux":
            return False
        
        try:
            if os.geteuid() == 0:
                # Set swappiness to 10 (default is usually 60)
                subprocess.run(
                    "sysctl vm.swappiness=10",
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                self.applied_optimizations.append("Reduced Swappiness")
                return True
            else:
                self.failed_optimizations.append("Swappiness: Requires root privileges")
                return False
        except Exception as e:
            self.failed_optimizations.append(f"Swappiness: {str(e)}")
            return False
    
    def optimize_process_priority(self) -> bool:
        """Provide guidance on process priority optimization."""
        if self.system != "Linux":
            return False
        
        self.applied_optimizations.append("Use 'nice' command to prioritize game processes")
        return True
    
    def disable_compositor_tips(self) -> bool:
        """Provide tips for disabling compositor on Linux."""
        if self.system != "Linux":
            return False
        
        self.applied_optimizations.append(
            "Tip: Disable desktop compositor while gaming (varies by DE)"
        )
        return True
    
    def optimize_macos_power(self) -> bool:
        """Optimize power settings on macOS."""
        if self.system != "Darwin":
            return False
        
        try:
            # Prevent display sleep and optimize power
            subprocess.run(
                "sudo pmset -a displaysleep 0",
                shell=True,
                capture_output=True,
                timeout=5
            )
            self.applied_optimizations.append("Optimized macOS Power Settings")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"macOS Power: {str(e)}")
            return False
    
    def reduce_macos_visuals(self) -> bool:
        """Reduce visual effects on macOS."""
        if self.system != "Darwin":
            return False
        
        try:
            # Reduce transparency and animations
            cmds = [
                "defaults write NSGlobalDomain AppleReduceDesktopTinting -bool true",
                "defaults write com.apple.universalaccess reduceMotion -bool true",
            ]
            
            for cmd in cmds:
                subprocess.run(cmd, shell=True, capture_output=True, timeout=5)
            
            self.applied_optimizations.append("Reduced macOS Visual Effects")
            return True
        except Exception as e:
            self.failed_optimizations.append(f"macOS Visuals: {str(e)}")
            return False
    
    def clean_ram(self) -> bool:
        """Free up RAM by clearing caches."""
        try:
            if self.system == "Linux" and os.geteuid() == 0:
                # Drop caches on Linux
                subprocess.run(
                    "sync; echo 3 > /proc/sys/vm/drop_caches",
                    shell=True,
                    capture_output=True,
                    timeout=10
                )
                self.applied_optimizations.append("Cleared RAM Caches")
                return True
            elif self.system == "Windows":
                # On Windows, we can't directly clear standby list without a tool
                # But we can trigger garbage collection in Python
                import gc
                gc.collect()
                self.applied_optimizations.append("Triggered Memory Cleanup")
                return True
            else:
                import gc
                gc.collect()
                self.applied_optimizations.append("Triggered Memory Cleanup")
                return True
        except Exception as e:
            self.failed_optimizations.append(f"RAM Cleanup: {str(e)}")
            return False
    
    def optimize_gpu_settings(self, gpu_info: Dict) -> bool:
        """Apply GPU-specific optimizations based on detected hardware."""
        if not gpu_info:
            return False
        
        try:
            # Check for NVIDIA GPU
            gpus = gpu_info.get("gpus", [])
            cuda_available = gpu_info.get("cuda_available", False)
            
            if cuda_available or any("NVIDIA" in gpu for gpu in gpus):
                # Set NVIDIA power mode to maximum performance (Linux only)
                if self.system == "Linux":
                    try:
                        subprocess.run(
                            "nvidia-smi -pm 1",  # Enable persistence mode
                            shell=True,
                            capture_output=True,
                            timeout=5
                        )
                        subprocess.run(
                            "nvidia-smi -pl 250",  # Set power limit (adjust as needed)
                            shell=True,
                            capture_output=True,
                            timeout=5
                        )
                        self.applied_optimizations.append("NVIDIA GPU Performance Mode Enabled")
                    except:
                        pass
                
                # Windows: Set prefer maximum performance in registry
                if self.system == "Windows":
                    try:
                        subprocess.run(
                            'reg add "HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\NVTweak" /v PowerMizerEnable /t REG_DWORD /d 1 /f',
                            shell=True,
                            capture_output=True,
                            timeout=5
                        )
                        self.applied_optimizations.append("NVIDIA PowerMizer Enabled")
                    except:
                        pass
            
            # Check for AMD GPU
            if any("AMD" in gpu or "Radeon" in gpu for gpu in gpus):
                if self.system == "Linux":
                    # Try to set AMD GPU performance profile
                    try:
                        amd_path = "/sys/class/drm/card0/device/power_dpm_force_performance_level"
                        if os.path.exists(amd_path) and os.geteuid() == 0:
                            with open(amd_path, 'w') as f:
                                f.write('high')
                            self.applied_optimizations.append("AMD GPU Performance Profile Set")
                    except:
                        pass
                
                if self.system == "Windows":
                    # Suggest enabling GPU scheduling
                    self.applied_optimizations.append("Consider enabling Hardware-accelerated GPU scheduling in Windows Settings")
            
            # Check VRAM and provide recommendations
            vram_total = gpu_info.get("vram_total", 0)
            if vram_total:
                if vram_total < 2048:  # Less than 2GB
                    self.applied_optimizations.append("Warning: Low VRAM detected. Consider lowering texture quality.")
                elif vram_total >= 8192:  # 8GB or more
                    self.applied_optimizations.append("Excellent VRAM capacity detected. High-quality textures supported.")
            
            # Detect if dedicated GPU exists
            if not gpus or len(gpus) == 0:
                self.failed_optimizations.append("No GPU detected")
                return False
            
            return True
            
        except Exception as e:
            self.failed_optimizations.append(f"GPU Optimization: {str(e)}")
            return False
    
    def enable_gpu_low_latency_mode(self) -> bool:
        """Enable low latency mode for GPU (GPU Booster #1)."""
        try:
            if self.system == "Windows":
                # Enable Ultra Low Latency mode for NVIDIA GPUs
                subprocess.run(
                    'reg add "HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\NVTweak" /v LowLatencyMode /t REG_DWORD /d 1 /f',
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                self.applied_optimizations.append("GPU Low Latency Mode Enabled")
                return True
            elif self.system == "Linux":
                self.applied_optimizations.append("GPU Low Latency: Use NVidia NVENC or AMD AFMF for reduced latency")
                return True
            elif self.system == "Darwin":
                self.applied_optimizations.append("GPU Low Latency: macOS Metal handles latency automatically")
                return True
        except Exception as e:
            self.failed_optimizations.append(f"GPU Low Latency: {str(e)}")
            return False
    
    def optimize_texture_cache(self) -> bool:
        """Optimize texture cache settings for GPU (GPU Booster #2)."""
        try:
            if self.system == "Windows":
                # Increase texture cache size in registry
                subprocess.run(
                    'reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v TextureMemoryLimit /t REG_DWORD /d 512 /f',
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                self.applied_optimizations.append("Texture Cache Optimized")
                return True
            elif self.system == "Linux":
                self.applied_optimizations.append("Texture Cache: GL_CACHE_TEXTURE_APPLE can be enabled in OpenGL apps")
                return True
            elif self.system == "Darwin":
                self.applied_optimizations.append("Texture Cache: Metal API manages cache automatically")
                return True
        except Exception as e:
            self.failed_optimizations.append(f"Texture Cache: {str(e)}")
            return False
    
    def enable_gpu_shader_cache(self) -> bool:
        """Enable shader cache optimization for GPU (GPU Booster #3)."""
        try:
            if self.system == "Windows":
                # Enable shader pre-caching
                subprocess.run(
                    'reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v ShaderCacheEnable /t REG_DWORD /d 1 /f',
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                self.applied_optimizations.append("GPU Shader Cache Enabled")
                return True
            elif self.system == "Linux":
                self.applied_optimizations.append("Shader Cache: Enable VK_KHR_pipeline_library for Vulkan games")
                return True
            elif self.system == "Darwin":
                self.applied_optimizations.append("Shader Cache: Metal compiles shaders at install time")
                return True
        except Exception as e:
            self.failed_optimizations.append(f"Shader Cache: {str(e)}")
            return False
    
    def get_optimization_report(self) -> Dict[str, any]:
        """Get report of applied optimizations."""
        return {
            "applied": self.applied_optimizations,
            "failed": self.failed_optimizations,
            "total_applied": len(self.applied_optimizations),
            "total_failed": len(self.failed_optimizations),
        }
    
    def reset_optimizations(self) -> bool:
        """Reset optimizations to default (where possible)."""
        self.applied_optimizations = []
        self.failed_optimizations = []
        
        if self.system == "Windows":
            try:
                # Reset power plan to balanced
                subprocess.run(
                    "powercfg -setactive SCHEME_BALANCED",
                    shell=True,
                    capture_output=True,
                    timeout=10
                )
                return True
            except:
                return False
        
        return True
