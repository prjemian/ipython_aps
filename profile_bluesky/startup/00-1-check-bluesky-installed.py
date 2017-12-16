print(__file__)
import sys

# ensure BlueSky is available
try:
    import bluesky
except ImportError:
    msg = 'No module named "bluesky"\n'
    msg += 'This python is from directory: ' + sys.prefix
    msg += '\n'*2
    msg += 'You should type `exit` now and find the ipython with BlueSky'
    raise ImportError(msg)

#req_version = (1.0)
#if bluesky.__version__ < req_version:
#    msg += bluesky.__version__
#    raise ValueError(msg)
