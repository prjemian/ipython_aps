
"""
check that our EPICS soft IOCs are running
"""

import epics
import logging
import os


__all__ = []

logger = logging.getLogger(__name__)
logger.info(__file__)

start_ioc_script = "/home/beams/JEMIAN/bin/start_iocs.sh"

up = epics.caget("sky:UPTIME", timeout=1)
if up is None:
    logger.info("EPICS IOCs not running.  Starting them now...")
    start_ioc_script = "/home/beams/JEMIAN/bin/start_iocs.sh"
    os.system(start_ioc_script)
    logger.debug("IOCs started")
else:
    logger.info("EPICS IOCs ready...")
