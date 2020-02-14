
"""
calculations
"""

__all__ = ["calcs", "calcouts"]

from ..session_logs import logger
logger.info(__file__)

import apstools.synApps
from ophyd import EpicsSignalRO

calcs = apstools.synApps.UserCalcsDevice("sky:", name="calcs")
calcouts = apstools.synApps.UserCalcoutDevice("sky:", name="calcouts")

calcs.enable.put(1)
