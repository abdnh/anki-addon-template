import os
import sys

from aqt.utils import showInfo

sys.path.append(os.path.join(os.path.dirname(__file__), "vendor"))

from .consts import consts

showInfo(f"Hello from {consts.name}!")
