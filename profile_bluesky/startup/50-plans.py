print(__file__)


# Bluesky plans (scans)


def darks_flats_images(det, shutter, stage, pos_in, pos_out, n_darks=3, n_flats=4, n_images=5, count_time=0.2, md=None):
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
