
"""
configure for data collection in a console session
"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(__file__)

logger.info("prechecks")
from .startup.check_python import *
from .startup.check_bluesky import *

# from .startup.logging_setup import *

logger.info("soft IOCS running?")
from .iocs.check_iocs import *

logger.info("load bluesky framework")
logger.info("bluesky framework")
from .mpl import console

from .startup import *

logger.info("load instrument devices")
from .devices import *

logger.info("load instrument plans")
from .plans import *

from apstools.utils import show_ophyd_symbols, print_RE_md
