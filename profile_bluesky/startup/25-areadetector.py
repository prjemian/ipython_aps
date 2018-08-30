print(__file__)

from ophyd import SingleTrigger, AreaDetector, SimDetector
from ophyd import HDF5Plugin, ImagePlugin
from ophyd.areadetector.trigger_mixins import SingleTrigger
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd import Component, Device, EpicsSignalWithRBV
from ophyd.areadetector import ADComponent


# MUST, must, MUST have trailing "/"!!!
image_file_path = "/tmp/simdet/%Y/%m/%d/"


def ad_warmed_up(detector):
    """
    Has area detector pushed an NDarray to the HDF5 plugin?  True or False
    
    Works around an observed issue: #598
    https://github.com/NSLS-II/ophyd/issues/598#issuecomment-414311372
    
    If detector IOC has just been started and has not yet taken an image
    with the HDF5 plugin, then a TimeoutError will occur as the
    HDF5 plugin "Capture" is set to 1 (Start).  In such case,
    first acquire at least one image with the HDF5 plugin enabled.
    """
    old_capture = detector.hdf1.capture.value
    old_file_write_mode = detector.hdf1.file_write_mode.value
    if old_capture == 1:
        return True
    
    detector.hdf1.file_write_mode.put(1)
    detector.hdf1.capture.put(1)
    verdict = detector.hdf1.capture.get() == 1
    detector.hdf1.capture.put(old_capture)
    detector.hdf1.file_write_mode.put(old_file_write_mode)
    return verdict


class MyHDF5Plugin(HDF5Plugin, FileStoreHDF5IterativeWrite):
    """
    """


class MySingleTriggerHdf5SimDetector(SingleTrigger, SimDetector): 
       
    image = Component(ImagePlugin, suffix="image1:")
    hdf1 = Component(
        MyHDF5Plugin,
        suffix='HDF1:', 
        root='/',                               # for databroker
        write_path_template=image_file_path,    # for EPICS AD
    )

try:
    _ad_prefix = "otzSIM1:"
    adsimdet = MySingleTriggerHdf5SimDetector(_ad_prefix, name='adsimdet')
    adsimdet.read_attrs.append("hdf1")


except TimeoutError:
    print(f"Could not connect {_ad_prefix} sim detector")


def count_AD(det, count_time=0.2, num=1, delay=None, *, md=None):
    det.cam.stage_sigs["acquire_time"] = count_time
    yield from bp.count([det], num=num, delay=delay, md=md)


def ad_continuous_setup(det, acq_time=0.1, acq_period=0.005):
    det.cam.acquire_time.put(acq_time)
    det.cam.acquire_period.put(acq_period)
    det.cam.image_mode.put("Continuous")
