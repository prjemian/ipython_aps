print(__file__)

import datetime
import socket
import getpass
import apstools
import pyRestTable

# Set up default metadata

HOSTNAME = socket.gethostname() or 'localhost' 
USERNAME = getpass.getuser() or 'synApps_xxx_user' 
RE.md['login_id'] = USERNAME + '@' + HOSTNAME
RE.md['beamline_id'] = 'developer'	# TODO: YOUR_BEAMLINE_HERE
RE.md['proposal_id'] = None
RE.md['pid'] = os.getpid()
RE.md["version"] = {}
RE.md["version"]['bluesky'] = bluesky.__version__
RE.md["version"]['ophyd'] = ophyd.__version__
RE.md["version"]['apstools'] = apstools.__version__
RE.md["version"]['epics'] = epics.__version__

print_RE_md()
