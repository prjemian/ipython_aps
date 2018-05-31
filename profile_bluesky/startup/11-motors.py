print(__file__)

"""motors, stages, positioners, ..."""

# m1 = MyEpicsMotorWithDial('gov:m1', name='m1')

m1 = TunableEpicsMotor("gov:m1", name="m1", labels=("motor", "tunable"))
m2 = EpicsMotor('gov:m2', name='m2', labels=("motor", ))
m3 = EpicsMotor('gov:m3', name='m3', labels=("motor", ))
m4 = EpicsMotor('gov:m4', name='m4', labels=("motor", ))
m5 = EpicsMotor('gov:m5', name='m5', labels=("motor", ))
m6 = EpicsMotor('gov:m6', name='m6', labels=("motor", ))
m7 = EpicsMotor('gov:m7', name='m7', labels=("motor", ))
m8 = EpicsMotor('gov:m8', name='m8', labels=("motor", ))
