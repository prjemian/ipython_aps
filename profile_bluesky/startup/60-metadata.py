print(__file__)

import datetime

# Set up default metadata

RE.md['beamline_id'] = 'developer__MAKE_SURE_TO_CHANGE_THIS_FOR_USERS__'
RE.md['proposal_id'] = None
RE.md['pid'] = os.getpid()

# Add a callback that prints scan IDs at the start of each scan.

def print_scan_ids(name, start_doc):
    msg = "Transient Scan ID: "
    msg += str(start_doc['scan_id'])
    msg += " @ "
    msg += str(datetime.datetime.isoformat(datetime.datetime.now()))
    print(msg)
    print("Persistent Unique Scan ID: '{0}'".format(start_doc['uid']))

RE.subscribe(print_scan_ids, 'start')

import socket 
import getpass 
HOSTNAME = socket.gethostname() or 'localhost' 
USERNAME = getpass.getuser() or 'synApps_xxx_user' 
RE.md['login_id'] = USERNAME + '@' + HOSTNAME

import os
for key, value in os.environ.items():
    if key.startswith("EPICS"):
        RE.md[key] = value
