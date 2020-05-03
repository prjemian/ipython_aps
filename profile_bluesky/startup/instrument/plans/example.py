"""
example custom scan plan

Find the peak of noisy v. m1 in the range of +/- 2.
"""

__all__ = [
    "example_peakfind",
]

from ..session_logs import logger
logger.info(__file__)

from ..framework import RE, peaks, bp
from ..devices import m1, noisy

def example_peakfind():
    """
    implement these commands

    ::

        RE(bp.scan([noisy], m1, -2.1, 2.1, 23))
        sig = peaks["fwhm"]["noisy"]; m1.move(peaks["cen"]["noisy"]); RE(bp.rel_scan([noisy], m1, -sig, +sig, 23))
    
    1. replace ``RE()`` with ``yield from ``
    2. break lines at ``;``
    3. import objects as needed
    4. add this plan's name to ``__all__`` list at top
    """
    yield from bp.scan([noisy], m1, -2.1, 2.1, 23)

    # FIXME: KeyError: 'noisy'
    sig = peaks["fwhm"]["noisy"]
    m1.move(peaks["cen"]["noisy"])
    yield from bp.rel_scan([noisy], m1, -sig, +sig, 23)
