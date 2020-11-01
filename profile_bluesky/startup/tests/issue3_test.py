#!/usr/bin/env python

"""
issue3_test.py

https://github.com/prjemian/ipython-aps/issues/3#issuecomment-720042520
"""

import os
import pprint
import psutil
import pyRestTable
import sys
import time
import tracemalloc

from bluesky import RunEngine
from bluesky import plans as bp
from ophyd.sim import motor, noisy_det

RE = RunEngine({})
pid = os.getpid()
process = psutil.Process(pid)


def rss_mem():
    """return memory used by this process"""
    return process.memory_info()


def snap_report(s0, s1, title=None, threshhold = 1000, key_type="lineno"):
    # key_type = [filename,  lineno,  traceback]
    if title is None:
        title = f"tracemalloc {key_type} differences > {threshhold} bytes"
    top_stats = s1.compare_to(s0, key_type)
    print(f"{title}:")
    tbl = pyRestTable.Table()
    tbl.labels = "item diff value".split()
    for i, stat in enumerate(top_stats):
        if stat.size_diff > threshhold:
            tbl.addRow((i+1, stat.size_diff, stat))
    print(tbl)


def example(iters=1):
    tracemalloc.start()
    mem_start = rss_mem().rss
    snap_start = tracemalloc.take_snapshot()
    for _i in range(iters):
        t0 = time.time()
        mem0 = rss_mem().rss
        snap0 = tracemalloc.take_snapshot()
        # yield from bp.count([noisy_det])
        yield from bp.scan([noisy_det], motor, -2.1, 2.1, 23)
        mem = rss_mem().rss
        snap = tracemalloc.take_snapshot()
        print(
            f"Finished #{_i+1} of {iters} iterations"
            f", dt={time.time() - t0:.3f} s"
            f", bytes={mem}, bytes_changed={mem - mem0}"
            )
        snap_report(snap0, snap, threshhold=10000)

    mem_end = rss_mem().rss
    snap_end = tracemalloc.take_snapshot()
    print(f"changed: {mem_end - mem_start}")
    snap_report(snap_start, snap_end, threshhold=10000)
    tracemalloc.stop()


uids = RE(example(5))
