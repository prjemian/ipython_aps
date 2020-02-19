
"""
ensure BlueSky is available
"""

__all__ = []

from ..session_logs import logger
logger.info(__file__)

try:
    import bluesky
except ImportError:
    msg = 'No module named "bluesky"\n'
    msg += 'This python is from directory: ' + sys.prefix
    msg += '\n'*2
    msg += 'You should type `exit` now and find the ipython with bluesky'
    raise ImportError(msg)


req_version = (1, 1)
cur_version = tuple(map(int, bluesky.__version__.split(".")[:2]))
if cur_version < req_version:
   ver_str = '.'.join((map(str,req_version)))
   msg = "Need at least sluesky %s+, " % ver_str
   msg += ' you have ' + bluesky.__version__
   raise ValueError(msg)
