"""
example custom scan plan

Find the peak of noisy v. m1 in the range of +/- 2.
"""

__all__ = [
    "example1",
    "example_findpeak",
    "change_peak",
    "repeat_findpeak",
]

from ..session_logs import logger
logger.info(__file__)

import apstools.utils
import numpy.random
import pyRestTable
from bluesky import preprocessors as bpp
from ..framework import bec, RE, peaks, bp, sd
from ..devices import m1, noisy, calcs, calcouts


def example1():
    """
    Find the peak of noisy v. m1 in the range of +/- 2.

    We know the peak of the simulated noisy detector is
    positioned somewhere between -1 to +1.  Overscan that
    range to find both sides of the peak.

    This is a 2 scan procedure.  First scan passes through 
    the full range.  Second scan is centered on the peak
    and width of the first scan.

    ::

        RE(bp.scan([noisy], m1, -2.1, 2.1, 23))
        sig = peaks["fwhm"]["noisy"]; m1.move(peaks["cen"]["noisy"]); RE(bp.rel_scan([noisy], m1, -sig, +sig, 23))
    
    1. replace ``RE()`` with ``yield from ``
    2. break lines at ``;``
    3. import objects as needed
    4. add this plan's name to ``__all__`` list at top
    5. changed bp.scan to bp.rel_scan
    """
    sig = 2
    m1.move(0)
    yield from bp.rel_scan([noisy], m1, -sig, +sig, 23)
    sig = peaks["fwhm"]["noisy"]
    m1.move(peaks["cen"]["noisy"])

    yield from bp.rel_scan([noisy], m1, -sig, +sig, 23)
    sig = peaks["fwhm"]["noisy"]
    m1.move(peaks["cen"]["noisy"])


def example_findpeak(number_of_scans=4, number_of_points=23):
    """
    find peak of noisy v. m1 by repeated scans with refinement

    basically::
        RE(bp.scan([noisy], m1, -2.1, 2.1, 23))
        fwhm=peaks["fwhm"]["noisy"]
        m1.move(peaks["cen"]["noisy"])
        RE(bp.rel_scan([noisy], m1, -fwhm, fwhm, 23))
        fwhm=peaks["fwhm"]["noisy"]
        m1.move(peaks["cen"]["noisy"])
        RE(bp.rel_scan([noisy], m1, -fwhm, fwhm, 23))
    """
    k = 1.5     # range expansion factor
    fwhm = 2.1 / k
    cen = 0
    results = []
    for _again in range(number_of_scans):
        m1.move(cen)
        yield from bp.rel_scan([noisy], m1, -k*fwhm, k*fwhm, number_of_points)
        if "noisy" not in peaks["fwhm"]:
            logger.error("no data in `peaks`, end of these scans")
            break
        fwhm = peaks["fwhm"]["noisy"]
        cen = peaks["cen"]["noisy"]
        results.append((RE.md["scan_id"], cen, fwhm))
    
    tbl = pyRestTable.Table()
    tbl.labels = "scan_id center FWHM".split()
    for row in results:
        tbl.addRow(row)
    logger.info("iterative results:\n%s", str(tbl))


def change_peak():
    apstools.devices.setup_lorentzian_swait(
        calcs.calc1,
        m1.user_readback,
        center = 2*numpy.random.random() - 1,
        width = 0.015 * numpy.random.random(),
        scale = 10000 * (9 + numpy.random.random()),
        noise=0.05,
    )


sd.baseline.append(calcs)
sd.baseline.append(calcouts)


def repeat_findpeak(iters=1):
    # bec.disable_plots()
    # If plots are disabled, then the peak stats are not run
    # so peak finding fails.
    for _i in range(iters):
        apstools.utils.trim_plot_lines(bec, 4, m1, noisy)
        change_peak()
        yield from example_findpeak()
        logger.info("Finished #%d of %d iterations", _i+1, iters)
    # bec.enable_plots()
