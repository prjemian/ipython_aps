from collections import OrderedDict
from instrument.session_logs import logger
import numpy as np
from ophyd.utils import set_and_wait
import time as ttime

logger.info(__file__)

from instrument.devices import adsimdet


def ad_plugin_primed(plugin):
    """
    Is the area detector 'det' plugin primed?

    PARAMETERS
    ----------
    plugin
        obj :
        ophyd AreaDetector plugin instance

    PARAMETERS
    ----------
    bool :
        True if plugin is primed
    """
    cam = plugin.parent.cam
    tests = []

    for obj in (cam, plugin):
        test = np.array(obj.array_size.get()).sum() != 0
        tests.append(test)
        if not test:
            logger.debug("'%s' image size is zero", obj.name)

    checks = dict(
        array_size = False,
        color_mode = True,
        data_type = True,
    )
    for key, as_string in checks.items():
        c = getattr(cam, key).get(as_string=as_string)
        p = getattr(plugin, key).get(as_string=as_string)
        test = c == p
        tests.append(test)
        if not test:
            logger.debug("%s does not match", key)

    return False not in tests


def ad_prime_plugin(plugin):
    """
    A convenience method for 'priming' the area detector plugin.

    The plugin has to 'see' one acquisition before it is ready to capture.
    This sets the array size, data type, color mode, etc.

    PARAMETERS
    ----------
    plugin
        obj :
        ophyd AreaDetector plugin instance
    """
    if ad_plugin_primed(plugin):
        logger.debug("'%s' plugin is already primed", plugin.name)
        return

    # set_and_wait(plugin.enable, 1)
    sigs = OrderedDict(
        [
            (plugin.enable, 1),
            (plugin.parent.cam.array_callbacks, 1),
            (plugin.parent.cam.image_mode, "Single"),
            (plugin.parent.cam.trigger_mode, "Internal"),
            # just in case the acquisition time is set very long...
            (plugin.parent.cam.acquire_time, 1),
            (plugin.parent.cam.acquire_period, 1),
            (plugin.parent.cam.acquire, 1),
        ]
    )

    original_vals = {sig: sig.get() for sig in sigs}

    for sig, val in sigs.items():
        ttime.sleep(0.1)  # abundance of caution
        set_and_wait(sig, val)

    ttime.sleep(2)  # wait for acquisition

    for sig, val in reversed(list(original_vals.items())):
        ttime.sleep(0.1)
        set_and_wait(sig, val)
