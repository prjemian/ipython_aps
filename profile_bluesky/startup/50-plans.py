print(__file__)


# Bluesky plans (scans)
from APS_BlueSky_tools.plans import run_blocker_in_plan


def sleeper(t=1.0):
    print(datetime.datetime.now())
    t0 = time.time()
    time.sleep(t)
    dt = time.time() - t0 - t
    print(datetime.datetime.now(), dt)

# summarize_plan(run_blocker_in_plan(sleeper, 2.5))
# RE(run_blocker_in_plan(sleeper, 2.5))


def doo_dad(*args, **kwargs):
    print("doo_dad", args)
    print("doo_dad", kwargs)

# summarize_plan(run_blocker_in_plan(doo_dad, 2.5, "doo_dad"))
# RE(run_blocker_in_plan(doo_dad, 2.5, "doo_dad"))


def my_plan(t=1.0):
    yield from run_blocker_in_plan(sleeper, t)

# summarize_plan(my_plan(0.5))
# RE(my_plan(0.5))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def darks_flats_images(det, shutter, stage, pos_in, pos_out, n_darks=3, n_flats=4, n_images=5, count_time=0.2, md=None):
    """
    (demo only) take a sequence of area detector frames and store them all in one file
    
    dark frames are stored into one dataset
    flat frames are stored into another dataset
    image frames are stored into a third dataset
    
    The area detector HDF5 file plugin has a feature that diverts the image stream
    based on a specific global variable defined in the layout file.
    """
    det.cam.stage_sigs["acquire_time"] = count_time

    yield from bps.mv(
        shutter, "close", 
        det.cam.frame_type, 1,   # Background
        det.hdf1.num_capture, n_darks + n_flats + n_images,
        )
    yield from bp.count([det], num=n_darks, md=md)

    yield from bps.mv(
        shutter, "open", 
        stage, pos_out,
        det.cam.frame_type, 2)   # FlatField
    yield from bp.count([det], num=n_flats, md=md)

    yield from bps.mv(
        shutter, "open", 
        stage, pos_in,
        det.cam.frame_type, 0)   # images
    yield from bp.count([det], num=n_images, md=md)

    yield from bps.mv(shutter, "close")
