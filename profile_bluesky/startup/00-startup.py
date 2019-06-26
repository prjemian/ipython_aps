print(__file__)

import datetime

class ConsoleTee(object):
	"""
	capture printed output to file

	https://stackoverflow.com/questions/11325019/how-to-output-to-the-console-and-file
	"""
	def __init__(self, *files):
		self.files = files
	def write(self, obj):
		ts = f"# {str(datetime.datetime.now())}\n"
		for f in self.files:
			f.write(ts)
			f.write(obj)
			f.flush() # If you want the output to be visible immediately
	def flush(self) :
		for f in self.files:
			f.flush()

"""
_console_f = open(IPYTHON_CONSOLE_LOG_FILE, 'w')                                                                                              
_stdout_original = sys.stdout                                                                                                               
sys.stdout = ConsoleTee(sys.stdout, _console_f)   

sys.stdout = _stdout_original
_console_f.close()
"""

#-------------------------------------------------------------

from bluesky import RunEngine
from bluesky.utils import get_history
RE = RunEngine(get_history())

# Import matplotlib and put it in interactive mode.
import matplotlib.pyplot as plt
plt.ion()

# Make plots update live while scans run.
from bluesky.utils import install_qt_kicker
install_qt_kicker()

# Optional: set any metadata that rarely changes. in 60-metadata.py

# convenience imports
from bluesky.callbacks import *
from bluesky.plan_tools import print_summary
import bluesky.plans as bp
import bluesky.preprocessors as bpp
from time import sleep
import numpy as np
import bluesky.magics
import bluesky.plan_stubs as bps


def append_wa_motor_list(*motorlist):
    """add motors to report in the `wa` command"""
    BlueskyMagics.positioners += motorlist


# if needed for the EPICS areaDetector SimDetector (12M + 100)
# os.environ["EPICS_CA_MAX_ARRAY_BYTES"] = "12000100"


# diagnostics
from bluesky.utils import ts_msg_hook
#RE.msg_hook = ts_msg_hook
from bluesky.simulators import summarize_plan
