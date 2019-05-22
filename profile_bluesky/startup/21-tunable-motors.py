print(__file__)

"""tunable motors"""

m1.tuner = APS_plans.TuneAxis([synthetic_pseudovoigt], m1)
m1.tuner.width = 0.02
m1.tuner.num = 21
