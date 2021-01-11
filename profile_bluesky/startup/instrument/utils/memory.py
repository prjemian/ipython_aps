"""
how much memory is in use
"""

__all__ = [
    "rss_mem",
]

from ..session_logs import logger

logger.info(__file__)

import os
import psutil

pid = os.getpid()
process = psutil.Process(pid)


def rss_mem():
    """return memory used by this process"""
    return process.memory_info()
