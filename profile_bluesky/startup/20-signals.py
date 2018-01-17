print(__file__)

"""other signals"""

scans = sscanDevice("gov:", name="scans")
calcs = userCalcsDevice("gov:", name="calcs")
calcs.enable.put("Enable")
calc1 = calcs.calc1
