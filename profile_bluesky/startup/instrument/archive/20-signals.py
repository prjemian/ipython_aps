print(__file__)

"""other signals"""

aps = APS_devices.ApsMachineParametersDevice(name="APS")

# make sure these values are logged by every scan
sd.baseline.append(aps)


# always record current as secondary stream during scans
# name: aps_current_monitor
# db[-1].table("aps_current_monitor")
aps_current = aps.current
sd.monitors.append(aps_current)


scans = APS_devices.SscanDevice("sky:", name="scans")
calcs = APS_devices.UserCalcsDevice("sky:", name="calcs")
calcs.enable.put("Enable")
calc1 = calcs.calc1
