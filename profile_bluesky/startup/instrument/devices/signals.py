
"""
various signals
"""

__all__ = [
    "shutter",
    "noisy",
]

from ..session_logs import logger
logger.info(__file__)

import apstools.devices
from ophyd import EpicsSignalRO

shutter = apstools.devices.SimulatedApsPssShutterWithStatus(
    name="shutter", labels=("shutters",))
shutter.delay_s = 0.05 # shutter needs short recovery time after moving

# demo: use swait records to make "noisy" detector signals
noisy = EpicsSignalRO('sky:userCalc1', name='noisy', labels=("detectors",))
