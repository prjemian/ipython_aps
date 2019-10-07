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

#from apstools.tools import synApps_ophyd as synApps
from apstools import devices as APS_devices
from apstools import plans as APS_plans
from apstools import utils as APS_utils


class TunableEpicsMotor(APS_devices.AxisTunerMixin, EpicsMotor):
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

# create a mixin for motor record's enable/disable support
# see: https://github.com/BCDA-APS/apstools/pull/152

class EpicsMotorEnableMixin(APS_devices.DeviceMixinBase):
    """
    mixin providing access to motor enable/disable
    """
    enable_disable = Component(EpicsSignal, "_able", kind='omitted')
    MOTOR_ENABLE = 0
    MOTOR_DISABLE = 1
    
    @property
    def enabled(self):
        return self.enable_disable.value in (self.MOTOR_ENABLE, "Enabled")
    
    def enable_motor(self):
        """BLOCKING call to enable motor axis"""
        self.enable_disable.put(self.MOTOR_ENABLE)
    
    def disable_motor(self):
        """BLOCKING call to disable motor axis"""
        self.enable_disable.put(self.MOTOR_DISABLE)

class MyMotor(EpicsMotorEnableMixin, EpicsMotor): ...

skym2 = MyMotor("sky:m2", name="skym2")
