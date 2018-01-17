print(__file__)

"""motors, stages, positioners, ..."""

# m1 = MyEpicsMotorWithDial('gov:m1', name='m1')

m1 = EpicsMotor('gov:m1', name='m1')
m2 = EpicsMotor('gov:m2', name='m2')
m3 = EpicsMotor('gov:m3', name='m3')
m4 = EpicsMotor('gov:m4', name='m4')
m5 = EpicsMotor('gov:m5', name='m5')
m6 = EpicsMotor('gov:m6', name='m6')
m7 = EpicsMotor('gov:m7', name='m7')
m8 = EpicsMotor('gov:m8', name='m8')

append_wa_motor_list(m1, m2, m3, m4, m5, m6, m7, m8)
