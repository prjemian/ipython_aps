
"""
APS only: connect with facility information
"""

__all__ = [
    'aps',
    # 'undulator',
    ]

from ..session_logs import logger
logger.info(__file__)

import apstools.devices
from ..framework import sd


aps = apstools.devices.ApsMachineParametersDevice(name="aps")
sd.baseline.append(aps)

# undulator = apstools.devices.ApsUndulator("ID09", name="undulator")
# undulator = apstools.devices.ApsUndulatorDual("ID09", name="undulator")
# sd.baseline.append(undulator)
