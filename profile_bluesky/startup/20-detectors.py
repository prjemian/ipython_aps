print(__file__)

"""various detectors and other signals"""

from APS_BlueSky_tools.signals import SynPseudoVoigt
from APS_BlueSky_tools.devices import use_EPICS_scaler_channels


noisy = EpicsSignalRO('gov:userCalc1', name='noisy')
#scaler = EpicsScaler('gov:scaler1', name='scaler')
scaler = ScalerCH('gov:scaler1', name='scaler')
use_EPICS_scaler_channels(scaler)


synthetic_pseudovoigt = SynPseudoVoigt(
    'synthetic_pseudovoigt', m1, 'm1', 
    center=-1.5 + 0.5*np.random.uniform(), 
    eta=0.3 + 0.5*np.random.uniform(), 
    sigma=0.001 + 0.05*np.random.uniform(), 
    scale=1e5)
