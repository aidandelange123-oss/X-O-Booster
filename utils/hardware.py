"""
Hardware Information Module
Detects and reports system hardware specifications
"""

import platform
import subprocess
import re
import os
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
        """Get GPU information including VRAM details."""
        gpu_info = {
            "gpus": [],
            "gpu_details": [],
            "vram_total": None,
            "vram_used": None,
            "vram_free": None,
            "driver_version": None,
            "cuda_available": False,
            "directx_version": None,
        }
        
        if platform.system() == "Windows":
            gpu_info = self._get_windows_gpu_info(gpu_info)
        
        elif platform.system() == "Linux":
            gpu_info = self._get_linux_gpu_info(gpu_info)
        
        elif platform.system() == "Darwin":
            gpu_info = self._get_macos_gpu_info(gpu_info)
        
        # Try to detect CUDA availability
        gpu_info["cuda_available"] = self._detect_cuda()
        
        # Detect DirectX version on Windows
        if platform.system() == "Windows":
            gpu_info["directx_version"] = self._detect_directx()
        
        return gpu_info
    
    def _get_windows_gpu_info(self, gpu_info: Dict[str, Any]) -> Dict[str, Any]:
        """Get detailed GPU information on Windows."""
        try:
            # Get GPU names
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
            
            # Get detailed GPU information
            result = subprocess.run(
                "wmic path win32_videocontroller get name,AdapterRAM,DriverVersion,VideoProcessor",
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            lines = result.stdout.strip().split('\n')[1:]
            vram_list = []
            gpu_details = []
            
            for line in lines:
                if not line.strip():
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    # Parse the output - format varies
                    gpu_detail = {}
                    
                    # Extract VRAM (AdapterRAM is in bytes)
                    for part in parts:
                        if part.isdigit() and len(part) > 6:  # VRAM in bytes
                            vram_bytes = int(part)
                            vram_mb = vram_bytes / (1024 * 1024)
                            gpu_detail["vram_mb"] = round(vram_mb, 2)
                            gpu_detail["vram_gb"] = round(vram_mb / 1024, 2)
                            vram_list.append(vram_mb)
                            break
                    
                    gpu_details.append(gpu_detail)
            
            gpu_info["gpu_details"] = gpu_details
            if vram_list:
                gpu_info["vram_total"] = sum(vram_list)
            
            # Try PowerShell for more detailed GPU info including usage
            try:
                ps_cmd = """
                Get-WmiObject Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion, CurrentHorizontalResolution, CurrentVerticalResolution | Format-List
                """
                result = subprocess.run(
                    f"powershell -Command \"{ps_cmd}\"",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout:
                    # Parse PowerShell output for additional details
                    pass
            except:
                pass
                
        except Exception as e:
            gpu_info["error"] = str(e)
        
        return gpu_info
    
    def _get_linux_gpu_info(self, gpu_info: Dict[str, Any]) -> Dict[str, Any]:
        """Get detailed GPU information on Linux."""
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
            
            # Try nvidia-smi for NVIDIA GPUs with full details
            result = subprocess.run(
                "nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free,driver_version --format=csv,noheader",
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                gpus = []
                vram_total_list = []
                vram_used_list = []
                vram_free_list = []
                gpu_details = []
                driver_version = None
                
                for line in lines:
                    parts = line.split(",")
                    if len(parts) >= 5:
                        gpu_name = parts[0].strip()
                        vram_total = float(parts[1].strip().replace(" MiB", ""))
                        vram_used = float(parts[2].strip().replace(" MiB", ""))
                        vram_free = float(parts[3].strip().replace(" MiB", ""))
                        driver = parts[4].strip()
                        
                        gpus.append(gpu_name)
                        vram_total_list.append(vram_total)
                        vram_used_list.append(vram_used)
                        vram_free_list.append(vram_free)
                        
                        gpu_details.append({
                            "name": gpu_name,
                            "vram_total_mb": vram_total,
                            "vram_used_mb": vram_used,
                            "vram_free_mb": vram_free,
                            "vram_total_gb": round(vram_total / 1024, 2),
                            "vram_used_gb": round(vram_used / 1024, 2),
                            "vram_free_gb": round(vram_free / 1024, 2),
                            "utilization": round((vram_used / vram_total) * 100, 2) if vram_total > 0 else 0
                        })
                        
                        if driver_version is None:
                            driver_version = driver
                
                gpu_info["gpus"] = gpus
                gpu_info["gpu_details"] = gpu_details
                gpu_info["driver_version"] = driver_version
                
                if vram_total_list:
                    gpu_info["vram_total"] = sum(vram_total_list)
                    gpu_info["vram_used"] = sum(vram_used_list)
                    gpu_info["vram_free"] = sum(vram_free_list)
            
            # Try AMD ROCm if available
            if not gpu_info.get("gpu_details"):
                try:
                    result = subprocess.run(
                        "rocm-smi --showproductname",
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.stdout:
                        # Parse ROCm output
                        pass
                except:
                    pass
            
            # Try intel_gpu_top for Intel GPUs
            if not gpu_info.get("gpu_details"):
                try:
                    result = subprocess.run(
                        "intel_gpu_top -L",
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.stdout:
                        # Parse Intel GPU output
                        pass
                except:
                    pass
                        
        except Exception as e:
            gpu_info["error"] = str(e)
        
        return gpu_info
    
    def _get_macos_gpu_info(self, gpu_info: Dict[str, Any]) -> Dict[str, Any]:
        """Get detailed GPU information on macOS."""
        try:
            result = subprocess.run(
                "system_profiler SPDisplaysDataType",
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.stdout:
                lines = result.stdout.split('\n')
                current_gpu = None
                current_detail = {}
                gpu_details = []
                
                for line in lines:
                    if "Chipset Model:" in line:
                        if current_gpu:
                            gpu_details.append(current_detail)
                        current_gpu = line.split(":")[1].strip()
                        gpu_info["gpus"].append(current_gpu)
                        current_detail = {"name": current_gpu}
                    elif "Total Number of Cores:" in line:
                        cores = line.split(":")[1].strip()
                        current_detail["cores"] = cores
                    elif "VRAM" in line or "vRAM" in line:
                        vram = line.split(":")[1].strip()
                        current_detail["vram"] = vram
                        # Try to extract numeric value
                        import re
                        match = re.search(r'(\d+)\s*(MB|GB)', vram, re.IGNORECASE)
                        if match:
                            value = int(match.group(1))
                            unit = match.group(2).upper()
                            if unit == "GB":
                                value *= 1024
                            current_detail["vram_mb"] = value
                
                if current_detail:
                    gpu_details.append(current_detail)
                
                gpu_info["gpu_details"] = gpu_details
                
                # Calculate total VRAM
                vram_total = sum(d.get("vram_mb", 0) for d in gpu_details)
                if vram_total > 0:
                    gpu_info["vram_total"] = vram_total
                    
        except Exception as e:
            gpu_info["error"] = str(e)
        
        return gpu_info
    
    def _detect_cuda(self) -> bool:
        """Detect if CUDA is available."""
        # Method 1: Check via nvidia-smi
        try:
            result = subprocess.run(
                "nvidia-smi",
                shell=True,
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                return True
        except:
            pass
        
        # Method 2: Try importing torch with CUDA
        try:
            import torch
            if torch.cuda.is_available():
                return True
        except:
            pass
        
        # Method 3: Check for CUDA toolkit
        cuda_paths = [
            "/usr/local/cuda/bin/nvcc",
            "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\nvcc.exe",
        ]
        for path in cuda_paths:
            if os.path.exists(path):
                return True
        
        return False
    
    def _detect_directx(self) -> Optional[str]:
        """Detect DirectX version on Windows."""
        if platform.system() != "Windows":
            return None
        
        try:
            # Check registry for DirectX version
            result = subprocess.run(
                'reg query "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v Version',
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if "Version" in line:
                        parts = line.split()
                        if parts:
                            return parts[-1]
        except:
            pass
        
        # Default assumption for modern Windows
        if platform.version() and "10" in platform.version():
            return "12"
        
        return None
    
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
