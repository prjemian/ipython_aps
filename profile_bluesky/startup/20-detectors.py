print(__file__)

"""various detectors and other signals"""

from apstools.signals import SynPseudoVoigt
from apstools.devices import use_EPICS_scaler_channels

noisy = EpicsSignalRO('sky:userCalc1', name='noisy', labels=["detectors",])
scaler = ScalerCH('sky:scaler1', name='scaler', labels=["detectors",])
while not scaler.connected:
    time.sleep(0.1)
scaler.select_channels(None)


# synthetic_pseudovoigt = SynPseudoVoigt(
#     'synthetic_pseudovoigt', m1, 'm1', 
#     center=-1.5 + 0.5*np.random.uniform(), 
#     eta=0.3 + 0.5*np.random.uniform(), 
#     sigma=0.001 + 0.05*np.random.uniform(), 
#     scale=1e5)
