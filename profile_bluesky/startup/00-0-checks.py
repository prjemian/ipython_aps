print(__file__)

import sys
import os

# ensure Python 3.6+

req_version = (3,6)
cur_version = sys.version_info
if cur_version < req_version:
    ver_str = '.'.join((map(str,req_version)))
    msg = 'Requires Python %s+' % ver_str
    msg += ' with Bluesky packages, '
    msg += ' you have ' + sys.version
    msg += '\nfrom directory: ' + sys.prefix
    msg += '\n'*2
    msg += 'You should type `exit` now and find the ipython with Bluesky'
    raise RuntimeError(msg)


# ensure Bluesky is available
try:
    import bluesky
except ImportError:
    msg = 'No module named "bluesky"\n'
    msg += 'This python is from directory: ' + sys.prefix
    msg += '\n'*2
    msg += 'You should type `exit` now and find the ipython with BlueSky'
    raise ImportError(msg)


req_version = (1, 1)
cur_version = tuple(map(int, bluesky.__version__.split(".")[:2]))
if cur_version < req_version:
   ver_str = '.'.join((map(str,req_version)))
   msg = "Need at least Bluesky %s+, " % ver_str
   msg += ' you have ' + bluesky.__version__
   raise ValueError(msg)
print("Bluesky version:", bluesky.__version__)

import ophyd
print("Ophyd version:", ophyd.__version__)
