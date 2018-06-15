print(__file__)

from ophyd import SingleTrigger, AreaDetector, SimDetector
from ophyd import HDF5Plugin, ImagePlugin
from ophyd.areadetector.trigger_mixins import SingleTrigger
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd import Component, Device, EpicsSignalWithRBV
from ophyd.areadetector import ADComponent


# MUST, must, MUST have trailing "/"!!!
image_file_path = "/tmp/simdet/%Y/%m/%d/"


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
