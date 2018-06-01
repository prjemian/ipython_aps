print(__file__)

from ophyd import SingleTrigger, AreaDetector, SimDetector
from ophyd import HDF5Plugin, ImagePlugin
from ophyd.areadetector.trigger_mixins import SingleTrigger
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd import Component, Device, EpicsSignalWithRBV
from ophyd.areadetector import ADComponent


image_file_path = "/tmp/simdet"


class MyHDF5Plugin(HDF5Plugin, FileStoreHDF5IterativeWrite):
    
    file_number_sync = None
    
    def get_frames_per_point(self):    # AD 2.5
        return self.parent.cam.num_images.get()
    

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
    #
    # define these so something appears in the event stream
    #adsimdet.hdf1.read_attrs.append("file_name")
    #adsimdet.hdf1.read_attrs.append("file_path")
    adsimdet.hdf1.read_attrs.append("full_file_name")
    adsimdet.read_attrs.append("hdf1")

except TimeoutError:
    print(f"Could not connect {_ad_prefix} sim detector")


def demo_count_simdet(count_time=0.2):
    adsimdet.cam.stage_sigs["acquire_time"] = count_time
    adsimdet.describe_configuration()
    RE(bp.count([adsimdet]))
    cfg = adsimdet.hdf1.read_configuration()
    file_name = cfg["adsimdet_hdf1_full_file_name"]['value']
    # print(file_name)
    for i, ev in enumerate(db[-1].events()):
        print(i, ev["data"][adsimdet.hdf1.name+"_full_file_name"])


def ad_continuous_setup(det, acq_time=0.1, acq_period=0.005):
    det.cam.acquire_time.put(acq_time)
    det.cam.acquire_period.put(acq_period)
    det.cam.image_mode.put("Continuous")
