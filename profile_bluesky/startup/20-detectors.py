print(__file__)

"""various detectors and other signals"""

from apstools.signals import SynPseudoVoigt
from apstools.devices import use_EPICS_scaler_channels

from ophyd.ophydobj import Kind
def mySelectChannels(scaler, chan_names):
        scaler.match_names()
        name_map = {}
        for s in scaler.channels.component_names:
            scaler_channel = getattr(scaler.channels, s)
            nm = scaler_channel.s.name  # as defined in self.match_names()
            if len(nm) > 0:
                name_map[nm] = s

        if chan_names is None:
            chan_names = name_map.keys()

        read_attrs = ['chan01']  # always include time
        for ch in chan_names:
            try:
                read_attrs.append(name_map[ch])
            except KeyError:
                raise RuntimeError("The channel {} is not configured "
                                   "on the scaler.  The named channels are "
                                   "{}".format(ch, tuple(name_map)))
        scaler.channels.kind = Kind.normal
        scaler.channels.read_attrs = list(read_attrs)
        scaler.channels.configuration_attrs = list(read_attrs)
        for ch in read_attrs[1:]:
            getattr(scaler.channels, ch).s.kind = Kind.hinted


noisy = EpicsSignalRO('sky:userCalc1', name='noisy')
#scaler = EpicsScaler('sky:scaler1', name='scaler')
scaler = ScalerCH('sky:scaler1', name='scaler')
while not scaler.connected:
	time.sleep(0.1)
#scaler.select_channels(None)
mySelectChannels(scaler, None)
# use_EPICS_scaler_channels(scaler)


# synthetic_pseudovoigt = SynPseudoVoigt(
#     'synthetic_pseudovoigt', m1, 'm1', 
#     center=-1.5 + 0.5*np.random.uniform(), 
#     eta=0.3 + 0.5*np.random.uniform(), 
#     sigma=0.001 + 0.05*np.random.uniform(), 
#     scale=1e5)
