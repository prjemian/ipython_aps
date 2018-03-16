print(__file__)

"""various detectors and other signals"""

from APS_BlueSky_tools.examples import SynPseudoVoigt


def use_EPICS_scaler_channels(scaler):
    """
    configure scaler for only the channels with names assigned in EPICS 
    """
    read_attrs = []
    for ch in scaler.channels.component_names:
        _nam = epics.caget("{}.NM{}".format(scaler.prefix, int(ch[4:])))
        if len(_nam.strip()) > 0:
            read_attrs.append(ch)
    scaler.channels.read_attrs = read_attrs


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
