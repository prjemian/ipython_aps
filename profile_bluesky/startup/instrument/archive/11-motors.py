print(__file__)

"""motors, stages, positioners, ..."""

m1 = TunableEpicsMotor("sky:m1", name="m1", labels=("motor", "tunable"))
m2 = EpicsMotor('sky:m2', name='m2', labels=("motor", "general"))
m3 = EpicsMotor('sky:m3', name='m3', labels=("motor", "general"))
m4 = EpicsMotor('sky:m4', name='m4', labels=("motor", "general", "demo"))
m5 = EpicsMotor('sky:m5', name='m5', labels=("motor", "demo"))
m6 = EpicsMotor('sky:m6', name='m6', labels=("motor", "utility"))
m7 = EpicsMotor('sky:m7', name='m7', labels=("motor", "utility"))
m8 = EpicsMotor('sky:m8', name='m8', labels=("motor", "utility"))

shutter = APS_devices.EpicsMotorShutter("sky:m9", name="shutter", labels=("shutter", "motor"))
shutter.closed_position = 0.0
shutter.open_position = 3.0
