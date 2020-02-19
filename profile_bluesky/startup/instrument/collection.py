
"""
configure for data collection in a console session
"""

from .session_logs import logger
logger.info(__file__)

from . import mpl

logger.info("are our soft IOCS running?")
from .iocs import check_iocs

logger.info("bluesky framework")

from .framework import *

logger.info("configure instrument")
from .devices import *
from .plans import *
# from .utils import *

from apstools.utils import *

# ensure we get our own logger
from .session_logs import logger
