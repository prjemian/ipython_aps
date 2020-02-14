
"""
configure for data collection in a console session
"""

from .session_logs import logger
logger.info(__file__)

from .mpl import *

logger.info("are our soft IOCS running?")
from .iocs.check_iocs import *

logger.info("bluesky framework")

from .framework import *

logger.info("configure instrument")
from .devices import *
from .plans import *
# from .utils import *

from apstools.utils import show_ophyd_symbols, print_RE_md
