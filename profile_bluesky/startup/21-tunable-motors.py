print(__file__)

"""tunable motors"""

try:
    m1.tuner = TuneAxis([synthetic_pseudovoigt], m1, signal_name=scaler.channels.chan2.name)
except AttributeError:
    m1.tuner = TuneAxis([synthetic_pseudovoigt], m1, signal_name=scaler.channels.chan02.name)
m1.tuner.width = 0.02
m1.tuner.num = 21
