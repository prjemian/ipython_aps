print(__file__)

import datetime
import socket
import getpass
from apstools import __version__ as aps_version
from databroker import __version__ as db_version
import pyRestTable

# Set up default metadata

HOSTNAME = socket.gethostname() or 'localhost' 
USERNAME = getpass.getuser() or 'synApps_xxx_user' 
RE.md['login_id'] = USERNAME + '@' + HOSTNAME
RE.md['beamline_id'] = 'developer'	# TODO: YOUR_BEAMLINE_HERE
RE.md['proposal_id'] = None
RE.md['pid'] = os.getpid()
RE.md["versions"] = {}
RE.md["versions"]['bluesky'] = bluesky.__version__
RE.md["versions"]['ophyd'] = ophyd.__version__
RE.md["versions"]['databroker'] = db_version
RE.md["versions"]['apstools'] = aps_version
RE.md["versions"]['epics'] = epics.__version__
del db_version, aps_version

print_RE_md()
