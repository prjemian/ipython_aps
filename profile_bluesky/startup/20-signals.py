print(__file__)

"""other signals"""

APS = ApsMachineParametersDevice(name="APS")

# make sure these values are logged by every scan
sd.baseline.append(APS)


# always record current as secondary stream during scans
# name: aps_current_monitor
# db[-1].table("aps_current_monitor")
aps_current = APS.current
sd.monitors.append(aps_current)


scans = sscanDevice("gov:", name="scans")
calcs = userCalcsDevice("gov:", name="calcs")
calcs.enable.put("Enable")
calc1 = calcs.calc1
