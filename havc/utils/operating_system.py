from enum import Enum
import sys


class OperatingSystemEnum(Enum):
    LINUX = 1
    WINDOWS = 2

class OperatingSystem:

    def __init__(self):
        if sys.platform.startswith('linux'):
            self.operating_system = OperatingSystemEnum.LINUX
        elif sys.platform.startswith('win'):
            self.operating_system = OperatingSystemEnum.WINDOWS

    def get_current(self):
        return self.operating_system
    
    def get_correct_slash_symbol(self):
        operating_system = self.get_current()
        
        if operating_system == OperatingSystemEnum.LINUX:
            return '/'
        
        return '\\'