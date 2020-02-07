
"""
APS only: connect with facility information
"""

import apstools.devices
import logging
from ..startup.framework import sd

logger = logging.getLogger(__name__)
logger.info(__file__)

aps = apstools.devices.ApsMachineParametersDevice(name="aps")
sd.baseline.append(aps)

# undulator = apstools.devices.ApsUndulator("ID09", name="undulator")
# undulator = apstools.devices.ApsUndulatorDual("ID09", name="undulator")
# sd.baseline.append(undulator)
