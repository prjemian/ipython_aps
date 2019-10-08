print(__file__)

"""various detectors and other signals"""

from apstools.signals import SynPseudoVoigt
from apstools.devices import use_EPICS_scaler_channels

noisy = EpicsSignalRO('sky:userCalc1', name='noisy', labels=["detectors",])
scaler = ScalerCH('sky:scaler1', name='scaler', labels=["detectors",])
while not scaler.connected:
    time.sleep(0.1)

if len(scaler.channels.chan01.chname.value) == 0:
    # assume IOC is started fresh from docker image: no configuration
    scaler.channels.chan01.chname.put("clock")
    scaler.channels.chan02.chname.put("I0")
    scaler.channels.chan03.chname.put("I")
    scaler.channels.chan04.chname.put("diode")
    scaler.channels.chan05.chname.put("scint")
    scaler.channels.chan11.chname.put("roi1")

scaler.select_channels(None)

# synthetic_pseudovoigt = SynPseudoVoigt(
#     'synthetic_pseudovoigt', m1, 'm1', 
#     center=-1.5 + 0.5*np.random.uniform(), 
#     eta=0.3 + 0.5*np.random.uniform(), 
#     sigma=0.001 + 0.05*np.random.uniform(), 
#     scale=1e5)
