"""
details of the sky IOC
"""

__all__ = [
    "iocsky",
]

from ophyd import Component, Device, EpicsSignalRO


class IocInfoDevice(Device):

    iso8601 = Component(EpicsSignalRO, "iso8601")
    uptime = Component(EpicsSignalRO, ":UPTIME")


iocsky = IocInfoDevice("sky:", name="iocsky")
