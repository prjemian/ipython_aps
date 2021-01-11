"""
Configure matplotlib in interactive mode for Jupyter notebook
"""

__all__ = []

from ..session_logs import logger

logger.info(__file__)

from IPython import get_ipython

# %matplotlib notebook
get_ipython().magic("matplotlib notebook")
import matplotlib.pyplot as plt

plt.ion()
