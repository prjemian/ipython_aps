print(__file__)

"""various detectors and other signals"""

from apstools.signals import SynPseudoVoigt
from apstools.devices import use_EPICS_scaler_channels


class MyScalerCH(ScalerCH):

    def select_channels(self, chan_names=[]):
        '''Select channels based on the EPICS name PV

        Parameters
        ----------
        chan_names : Iterable[str] or None

            The names (as reported by the channel.chname signal)
            of the channels to select.
            If *None*, select all channels named in the EPICS scaler.
        '''
        self.match_names()  # name channels by EPICS names
        name_map = {}
        for i, s in enumerate(self.channels.component_names):
            nm = getattr(self.channels, s).s.name  # as defined in scaler.match_names()
            if i == 0 and len(nm) == 0:
                nm = "clock"        # ALWAYS get the clock channel
            if len(nm) > 0:
                name_map[nm] = s

        # previous argument was chan_names=None to select all
        # include logic here that allows backwards-compatibility
        if len(chan_names or []) == 0:    # default setting
            chan_names = name_map.keys()

        read_attrs = []
        for ch in chan_names:
            try:
                read_attrs.append(name_map[ch])
            except KeyError:
                raise RuntimeError("The channel {} is not configured "
                                    "on the scaler.  The named channels are "
                                    "{}".format(ch, tuple(name_map)))

        self.channels.kind = Kind.normal
        self.channels.read_attrs = list(read_attrs)
        self.channels.configuration_attrs = list(read_attrs)

        for i, s in enumerate(self.channels.component_names):
            channel = getattr(self.channels, s)
            if s in read_attrs:
                channel.s.kind = Kind.hinted
            else:
                channel.s.kind = Kind.normal


noisy = EpicsSignalRO('sky:userCalc1', name='noisy', labels=["detectors",])
scaler = MyScalerCH('sky:scaler1', name='scaler', labels=["detectors",])
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

clock = scaler.channels.chan01
I0 = scaler.channels.chan02
I = scaler.channels.chan03
diode = scaler.channels.chan04
scint = scaler.channels.chan05
roi1 = scaler.channels.chan10
roi2 = scaler.channels.chan11

for item in (clock, I0, I, diode, scint, roi1, roi2):
    item._ophyd_labels_ = set(["channel", "counter",])

def show_scaler_configuration(scaler):
    t = pyRestTable.Table()
    t.labels = "name channel value kind".split()
    for i, component in enumerate(scaler.channels.component_names):
        channel = getattr(scaler.channels, component)
        t.addRow((channel.chname.value, i+1, channel.s.value, channel.s.kind))
    print(f"EPICS {scaler.name} configuration\n{t}")

scaler.select_channels()
show_scaler_configuration(scaler)


synthetic_pseudovoigt = SynPseudoVoigt(
    'synthetic_pseudovoigt', m1, 'm1', 
    center=2*np.random.uniform() - 1, 
    eta=0.3 + 0.5*np.random.uniform(), 
    sigma=0.001 + 0.05*np.random.uniform(), 
    scale=1e5)
