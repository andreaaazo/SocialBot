from .dashboard import Dashboard
from .screen_manager import ScreensManager

from kivy.lang import Builder

# Load Dashboard design
Builder.load_file("lib/home/screens/dashboard/dashboard.kv")

# Load ScreenManager design
Builder.load_file("lib/home/screens/screen_manager/screen_manager.kv")
