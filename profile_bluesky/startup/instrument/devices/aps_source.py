
"""
APS only: connect with facility information
"""

from ..session_logs import logger
logger.info(__file__)

import apstools.devices
from ..startup import sd

__all__ = [
    'aps',
    # 'undulator',
]
aps = apstools.devices.ApsMachineParametersDevice(name="aps")
sd.baseline.append(aps)

# undulator = apstools.devices.ApsUndulator("ID45", name="undulator")
# undulator = apstools.devices.ApsUndulatorDual("ID45", name="undulator")
# sd.baseline.append(undulator)
