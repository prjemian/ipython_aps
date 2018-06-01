print(__file__)

"""other signals"""

aps_sr_current = EpicsSignalRO("S:SRcurrentAI", name="aps_sr_current")

# always record this as secondary stream during scans
# name: aps_sr_current_monitor
# db[-1].table("aps_sr_current_monitor")
sd.monitors.append(aps_sr_current)


scans = sscanDevice("gov:", name="scans")
calcs = userCalcsDevice("gov:", name="calcs")
calcs.enable.put("Enable")
calc1 = calcs.calc1
