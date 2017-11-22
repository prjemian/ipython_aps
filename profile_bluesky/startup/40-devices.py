print(__file__)

from APS_BlueSky_tools.devices import *


calscanscs = sscanDevice("gov:", name="scans")
calcs = userCalcsDevice("gov:", name="calcs")
calcs.enable.put("Enable")
calc1 = calcs.calc1

# Set up default complex devices

# FIXME: how to get the PVs to the inner parts?
# TODO: How to build this up from previously-configured motors?

#class SlitAxis(Device):
#	lo = Cpt(EpicsMotor, '')
#	hi = Cpt(EpicsMotor, '')

#class XY_Slit(Device):
#	h = Cpt(SlitAxis, '')
#	v = Cpt(SlitAxis, '')

#slit1 = XY_Slit()
