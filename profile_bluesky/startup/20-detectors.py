print(__file__)

"""various detectors and other signals"""

from APS_BlueSky_tools.examples import SynPseudoVoigt

noisy = EpicsSignalRO('gov:userCalc1', name='noisy')
scaler = EpicsScaler('gov:scaler1', name='scaler')
# but only read a few of the many channels
scaler.channels.read_attrs = "chan1 chan2 chan3 chan6".split()

synthetic_pseudovoigt = SynPseudoVoigt(
    'synthetic_pseudovoigt', m1, 'm1', 
    center=-1.5 + 0.5*np.random.uniform(), 
    eta=0.3 + 0.5*np.random.uniform(), 
    sigma=0.001 + 0.05*np.random.uniform(), 
    scale=1e5)
