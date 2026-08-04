"""
Logging Module for FPS Booster
Provides centralized logging functionality
"""

import logging
import os
import sys
from datetime import datetime
from typing import Optional


class Logger:
    """Centralized logging system for the FPS Booster application."""
    
    _instance: Optional['Logger'] = None
    _initialized: bool = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, log_dir: str = "logs", log_level: int = logging.INFO):
        if Logger._initialized:
            return
            
        self.log_dir = log_dir
        self.log_level = log_level
        self.logger = None
        self._setup_logger()
        Logger._initialized = True
    
    def _setup_logger(self):
        """Setup the logging system."""
        # Create logs directory if it doesn't exist
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        
        # Create logger
        self.logger = logging.getLogger("FPSBooster")
        self.logger.setLevel(self.log_level)
        
        # Clear any existing handlers
        self.logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler
        log_file = os.path.join(
            self.log_dir, 
            f"fps_booster_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
        # Console handler (only for errors and warnings)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        self.info("Logger initialized successfully")
        self.info(f"Log file: {log_file}")
    
    def debug(self, message: str):
        """Log debug message."""
        if self.logger:
            self.logger.debug(message)
    
    def info(self, message: str):
        """Log info message."""
        if self.logger:
            self.logger.info(message)
    
    def warning(self, message: str):
        """Log warning message."""
        if self.logger:
            self.logger.warning(message)
    
    def error(self, message: str, exc_info: bool = False):
        """Log error message."""
        if self.logger:
            self.logger.error(message, exc_info=exc_info)
    
    def critical(self, message: str, exc_info: bool = False):
        """Log critical message."""
        if self.logger:
            self.logger.critical(message, exc_info=exc_info)
    
    def get_log_file(self) -> str:
        """Get the current log file path."""
        if self.logger:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    return handler.baseFilename
        return "Unknown"


# Global logger instance
logger = Logger()


def get_logger() -> Logger:
    """Get the global logger instance."""
    return logger
