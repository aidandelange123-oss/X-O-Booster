"""
Hardware Information Module
Detects and reports system hardware specifications
"""

import platform
import subprocess
import re
from typing import Dict, Any, Optional


class HardwareDetector:
    """Detects and provides information about system hardware."""
    
    def __init__(self):
        self.system_info = {}
        self._detect_hardware()
    
    def _detect_hardware(self):
        """Gather all hardware information."""
        self.system_info = {
            "os": self._get_os_info(),
            "cpu": self._get_cpu_info(),
            "ram": self._get_ram_info(),
            "gpu": self._get_gpu_info(),
            "disk": self._get_disk_info(),
        }
    
    def _get_os_info(self) -> Dict[str, Any]:
        """Get operating system information."""
        return {
            "system": platform.system(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
        }
    
    def _get_cpu_info(self) -> Dict[str, Any]:
        """Get CPU information."""
        cpu_info = {
            "cores": None,
            "physical_cores": None,
            "frequency": None,
            "model": None,
        }
        
        try:
            # Get CPU count
            cpu_info["cores"] = self._get_logical_cores()
            cpu_info["physical_cores"] = self._get_physical_cores()
            
            # Try to get CPU frequency
            if hasattr(__import__("psutil"), "cpu_freq"):
                import psutil
                freq = psutil.cpu_freq()
                if freq:
                    cpu_info["frequency"] = f"{freq.current:.2f} MHz"
            
            # Get CPU model/name
            cpu_info["model"] = self._get_cpu_model()
            
        except Exception as e:
            cpu_info["error"] = str(e)
        
        return cpu_info
    
    def _get_logical_cores(self) -> int:
        """Get number of logical CPU cores."""
        try:
            import psutil
            return psutil.cpu_count(logical=True) or 0
        except ImportError:
            # Fallback method
            if platform.system() == "Windows":
                cmd = "wmic cpu get NumberOfLogicalProcessors"
            else:
                cmd = "nproc"
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
                if result.stdout:
                    lines = result.stdout.strip().split('\n')
                    for line in lines:
                        if line.isdigit():
                            return int(line)
            except:
                pass
            return 0
    
    def _get_physical_cores(self) -> int:
        """Get number of physical CPU cores."""
        try:
            import psutil
            return psutil.cpu_count(logical=False) or 0
        except ImportError:
            # Fallback - estimate (usually half of logical for hyperthreading)
            logical = self._get_logical_cores()
            return max(1, logical // 2) if logical > 0 else 0
    
    def _get_cpu_model(self) -> Optional[str]:
        """Get CPU model name."""
        try:
            import psutil
            # psutil doesn't provide CPU model directly on all platforms
            pass
        except ImportError:
            pass
        
        # Platform-specific methods
        if platform.system() == "Windows":
            try:
                result = subprocess.run(
                    "wmic cpu get name",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    return lines[1].strip()
            except:
                pass
        elif platform.system() == "Linux":
            try:
                with open("/proc/cpuinfo", "r") as f:
                    for line in f:
                        if line.startswith("model name"):
                            return line.split(":")[1].strip()
            except:
                pass
        elif platform.system() == "Darwin":
            try:
                result = subprocess.run(
                    "sysctl -n machdep.cpu.brand_string",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout:
                    return result.stdout.strip()
            except:
                pass
        
        return "Unknown"
    
    def _get_ram_info(self) -> Dict[str, Any]:
        """Get RAM information."""
        ram_info = {
            "total_gb": None,
            "available_gb": None,
            "used_gb": None,
            "percent_used": None,
        }
        
        try:
            import psutil
            mem = psutil.virtual_memory()
            ram_info["total_gb"] = round(mem.total / (1024 ** 3), 2)
            ram_info["available_gb"] = round(mem.available / (1024 ** 3), 2)
            ram_info["used_gb"] = round(mem.used / (1024 ** 3), 2)
            ram_info["percent_used"] = mem.percent
        except ImportError:
            # Fallback methods
            if platform.system() == "Windows":
                try:
                    result = subprocess.run(
                        "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize",
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    lines = result.stdout.strip().split('\n')
                    if len(lines) > 1:
                        parts = lines[1].split()
                        total_kb = int(parts[1])
                        free_kb = int(parts[0])
                        ram_info["total_gb"] = round(total_kb / (1024 * 1024), 2)
                        ram_info["available_gb"] = round(free_kb / (1024 * 1024), 2)
                        ram_info["used_gb"] = round((total_kb - free_kb) / (1024 * 1024), 2)
                        ram_info["percent_used"] = round(((total_kb - free_kb) / total_kb) * 100, 2)
                except:
                    pass
            elif platform.system() == "Linux":
                try:
                    with open("/proc/meminfo", "r") as f:
                        mem_data = {}
                        for line in f:
                            parts = line.split(":")
                            if len(parts) == 2:
                                key = parts[0].strip()
                                value = int(parts[1].strip().split()[0])
                                mem_data[key] = value
                        
                        if "MemTotal" in mem_data and "MemAvailable" in mem_data:
                            total_kb = mem_data["MemTotal"]
                            available_kb = mem_data["MemAvailable"]
                            ram_info["total_gb"] = round(total_kb / (1024 * 1024), 2)
                            ram_info["available_gb"] = round(available_kb / (1024 * 1024), 2)
                            ram_info["used_gb"] = round((total_kb - available_kb) / (1024 * 1024), 2)
                            ram_info["percent_used"] = round(((total_kb - available_kb) / total_kb) * 100, 2)
                except:
                    pass
        
        return ram_info
    
    def _get_gpu_info(self) -> Dict[str, Any]:
        """Get GPU information."""
        gpu_info = {
            "gpus": [],
            "vram_total": None,
            "vram_used": None,
        }
        
        if platform.system() == "Windows":
            try:
                result = subprocess.run(
                    "wmic path win32_videocontroller get name",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                lines = result.stdout.strip().split('\n')[1:]  # Skip header
                gpus = [line.strip() for line in lines if line.strip()]
                gpu_info["gpus"] = gpus
                
                # Try to get VRAM info
                result = subprocess.run(
                    "wmic path win32_videocontroller get AdapterRAM",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                lines = result.stdout.strip().split('\n')[1:]
                vram_list = []
                for line in lines:
                    if line.strip().isdigit():
                        vram_bytes = int(line.strip())
                        vram_mb = vram_bytes / (1024 * 1024)
                        vram_list.append(round(vram_mb, 2))
                
                if vram_list:
                    gpu_info["vram_total"] = sum(vram_list)
                    
            except Exception as e:
                gpu_info["error"] = str(e)
        
        elif platform.system() == "Linux":
            try:
                # Try lspci for GPU detection
                result = subprocess.run(
                    "lspci | grep -i vga",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout:
                    gpus = [line.split(":")[-1].strip() for line in result.stdout.strip().split('\n')]
                    gpu_info["gpus"] = gpus
                
                # Try nvidia-smi for NVIDIA GPUs
                result = subprocess.run(
                    "nvidia-smi --query-gpu=name,memory.total --format=csv,noheader",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout:
                    lines = result.stdout.strip().split('\n')
                    gpus = []
                    vram_list = []
                    for line in lines:
                        parts = line.split(",")
                        if len(parts) >= 2:
                            gpus.append(parts[0].strip())
                            vram_mb = float(parts[1].strip().replace(" MiB", ""))
                            vram_list.append(vram_mb)
                    
                    gpu_info["gpus"] = gpus
                    if vram_list:
                        gpu_info["vram_total"] = sum(vram_list)
                        
            except Exception as e:
                gpu_info["error"] = str(e)
        
        elif platform.system() == "Darwin":
            try:
                result = subprocess.run(
                    "system_profiler SPDisplaysDataType",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout:
                    # Parse output for GPU names
                    lines = result.stdout.split('\n')
                    current_gpu = None
                    for line in lines:
                        if "Chipset Model:" in line:
                            current_gpu = line.split(":")[1].strip()
                            gpu_info["gpus"].append(current_gpu)
            except Exception as e:
                gpu_info["error"] = str(e)
        
        return gpu_info
    
    def _get_disk_info(self) -> Dict[str, Any]:
        """Get disk/storage information."""
        disk_info = {
            "total_gb": None,
            "used_gb": None,
            "free_gb": None,
            "percent_used": None,
        }
        
        try:
            import psutil
            disk = psutil.disk_usage('/')
            disk_info["total_gb"] = round(disk.total / (1024 ** 3), 2)
            disk_info["used_gb"] = round(disk.used / (1024 ** 3), 2)
            disk_info["free_gb"] = round(disk.free / (1024 ** 3), 2)
            disk_info["percent_used"] = disk.percent
        except ImportError:
            # Fallback using shutil
            import shutil
            total, used, free = shutil.disk_usage('/')
            disk_info["total_gb"] = round(total / (1024 ** 3), 2)
            disk_info["used_gb"] = round(used / (1024 ** 3), 2)
            disk_info["free_gb"] = round(free / (1024 ** 3), 2)
            disk_info["percent_used"] = round((used / total) * 100, 2)
        
        return disk_info
    
    def get_system_report(self) -> Dict[str, Any]:
        """Get complete system hardware report."""
        return self.system_info
    
    def get_performance_score(self) -> Dict[str, Any]:
        """Calculate a simple performance score based on hardware."""
        score = 0
        recommendations = []
        
        cpu_info = self.system_info.get("cpu", {})
        ram_info = self.system_info.get("ram", {})
        gpu_info = self.system_info.get("gpu", {})
        
        # CPU scoring
        physical_cores = cpu_info.get("physical_cores", 0)
        if physical_cores >= 8:
            score += 30
        elif physical_cores >= 4:
            score += 20
        else:
            score += 10
            recommendations.append("Consider upgrading CPU for better performance")
        
        # RAM scoring
        total_ram = ram_info.get("total_gb", 0)
        if total_ram >= 16:
            score += 30
        elif total_ram >= 8:
            score += 20
        else:
            score += 10
            recommendations.append(f"Only {total_ram}GB RAM detected. Consider upgrading to at least 8GB")
        
        # GPU scoring
        gpu_count = len(gpu_info.get("gpus", []))
        vram = gpu_info.get("vram_total", 0)
        if gpu_count > 0:
            if vram >= 4096:  # 4GB+
                score += 30
            elif vram >= 2048:  # 2GB+
                score += 20
            else:
                score += 15
        else:
            score += 5
            recommendations.append("No dedicated GPU detected. Consider adding one for gaming")
        
        # Normalize score to 0-100
        score = min(100, score)
        
        return {
            "score": score,
            "rating": self._get_rating(score),
            "recommendations": recommendations,
        }
    
    def _get_rating(self, score: int) -> str:
        """Convert score to rating string."""
        if score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Fair"
        else:
            return "Needs Upgrade"
