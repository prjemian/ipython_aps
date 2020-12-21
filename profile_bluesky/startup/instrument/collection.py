"""
configure for data collection in a console session
"""

from .session_logs import logger

logger.info(__file__)

from . import mpl

logger.info("Start soft IOC dockers if PVs not available")
from .iocs import check_iocs

logger.info("bluesky framework")
from .utils import rss_mem

logger.info("rss_mem: %.6f MB", rss_mem().rss / 1024.0 / 1024.0)

from .framework import *

logger.info("rss_mem: %.6f MB", rss_mem().rss / 1024.0 / 1024.0)

logger.info("configure instrument")
from .devices import *

logger.info("rss_mem: %.6f MB", rss_mem().rss / 1024.0 / 1024.0)
from .plans import *

logger.info("rss_mem: %.6f MB", rss_mem().rss / 1024.0 / 1024.0)
from .utils import *

from apstools.utils import *

logger.info("rss_mem: %.6f MB", rss_mem().rss / 1024.0 / 1024.0)

# ensure we get our own logger
from .session_logs import logger
