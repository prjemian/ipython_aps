print(__file__)

"""
configure logging
"""

os.makedirs(".logs", exist_ok=True)
CONSOLE_IO_FILE = ".logs/.ipython_console.log"

# start logging console to file
# https://ipython.org/ipython-doc/3/interactive/magics.html#magic-logstart
from IPython import get_ipython
_ipython = get_ipython()
# %logstart -o -t .ipython_console.log "rotate"
_ipython.magic(f"logstart -o -t {CONSOLE_IO_FILE} rotate")

import stdlogpj
logger = stdlogpj.standard_logging_setup("ipython_logger")

logger.warning('logging started')

logger.debug('example Debug message')
logger.info('example Info message')
logger.warning(f'logging level = {logger.level}')
logger.warning('example Warning message')
logger.error('example Error message')
