print(__file__)

"""Set up default complex devices"""

import time
import uuid

from ophyd import Component, Device, DeviceStatus
from ophyd.status import Status
from ophyd import EpicsMotor, EpicsScaler
from ophyd.scaler import ScalerCH
from ophyd import EpicsSignal, EpicsSignalRO, EpicsSignalWithRBV
from ophyd import PVPositioner, PVPositionerPC
from ophyd import AreaDetector, PcoDetectorCam
from ophyd import SingleTrigger, ImagePlugin, HDF5Plugin
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from apstools.devices import *
#from APS_BlueSky_tools.synApps_ophyd import *
from apstools import *
from apstools.plans import *


class TunableEpicsMotor(AxisTunerMixin, EpicsMotor):
    """
    Example::
    
        def a2r_pretune_hook():
            # set the counting time for *this* tune
            yield from bps.abs_set(scaler.preset_time, 0.2)
            
        a2r = TunableEpicsMotor("xxx:m1", name="a2r")
        a2r.tuner = TuneAxis([scaler], a2r, signal_name=scaler.channels.chan2.name)
        a2r.tuner.width = 0.02
        a2r.tuner.num = 21
        a2r.pre_tune_method = a2r_pretune_hook
        RE(a2r.tune())

    """
