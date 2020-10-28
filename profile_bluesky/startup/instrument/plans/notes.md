# notes
2020-10-28

After thousands of scans,

    uids = RE(repeat_findpeak(3000))

finding and centering on a randomly-placed peak while
collecting lots of additional baseline data,

```
Transient Scan ID: 8853     Time: 2020-10-28 16:03:59
Persistent Unique Scan ID: '9a9f454e-37e5-4ab3-a89f-cd9a0c6475ea'
New stream: 'baseline'
New stream: 'primary'
+-----------+------------+------------+------------+
|   seq_num |       time |         m1 |      noisy |
+-----------+------------+------------+------------+
|         1 | 16:04:00.1 |   -0.35700 | 4447.00323 |
|         2 | 16:04:00.2 |   -0.35625 | 5353.43701 |
|         3 | 16:04:00.3 |   -0.35550 | 6378.52984 |
|         4 | 16:04:00.4 |   -0.35500 | 7226.64458 |
|         5 | 16:04:00.5 |   -0.35425 | 9492.65719 |
|         6 | 16:04:00.6 |   -0.35350 | 11706.09034 |
|         7 | 16:04:00.7 |   -0.35275 | 15526.28397 |
|         8 | 16:04:00.8 |   -0.35200 | 21915.13272 |
|         9 | 16:04:00.9 |   -0.35125 | 31022.00995 |
|        10 | 16:04:01.0 |   -0.35075 | 40357.26221 |
|        11 | 16:04:01.1 |   -0.35000 | 57593.83192 |
|        12 | 16:04:01.2 |   -0.34925 | 79854.42891 |
|        13 | 16:04:01.3 |   -0.34850 | 88595.85971 |
|        14 | 16:04:01.4 |   -0.34775 | 74375.27605 |
|        15 | 16:04:01.5 |   -0.34725 | 58190.71913 |
|        16 | 16:04:01.6 |   -0.34650 | 40297.97902 |
|        17 | 16:04:01.7 |   -0.34575 | 27674.26146 |
|        18 | 16:04:01.8 |   -0.34500 | 19006.74644 |
|        19 | 16:04:01.9 |   -0.34425 | 14395.89209 |
|        20 | 16:04:02.0 |   -0.34350 | 10720.32409 |
|        21 | 16:04:02.1 |   -0.34300 | 9506.82766 |
|        22 | 16:04:02.2 |   -0.34225 | 7460.32206 |
|        23 | 16:04:02.3 |   -0.34150 | 6042.27221 |
E Wed-16:04:02 - no data in `peaks`, end of these scans
I Wed-16:04:02 - iterative results:
======= ==================== ====================
scan_id center               FWHM                
======= ==================== ====================
8850    -0.38059867113736223 0.19760960824277923 
8851    -0.35330198146781255 0.02811840189162501 
8852    -0.3491724166338197  0.005185638119912628
======= ==================== ====================

I Wed-16:04:02 - Finished #766 of 3000 iterations
+-----------+------------+------------+------------+
generator rel_scan ['9a9f454e'] (scan num: 8853)
```

one scan started

```
Transient Scan ID: 8854     Time: 2020-10-28 16:04:03
Persistent Unique Scan ID: '924b5d73-727c-404e-8c43-530155ee1bf8'
New stream: 'baseline'
New stream: 'primary'                                                                                                                                             
+-----------+------------+------------+------------+
|   seq_num |       time |         m1 |      noisy |
+-----------+------------+------------+------------+
|         1 | 16:04:06.3 |   -2.10000 |    0.43754 |
|         2 | 16:04:06.8 |   -1.90900 |    0.51906 |                                                                                                              
|         3 | 16:04:07.3 |   -1.71825 |    0.63082 |                                                                                                              
|         4 | 16:04:07.8 |   -1.52725 |    0.77017 |                                                                                                              
|         5 | 16:04:08.3 |   -1.33625 |    0.98712 |                                                                                                              
|         6 | 16:04:08.8 |   -1.14550 |    1.31004 |                                                                                                              
|         7 | 16:04:09.3 |   -0.95450 |    1.74882 |                                                                                                              
|         8 | 16:04:09.8 |   -0.76375 |    2.48313 |                                                                                                              
|         9 | 16:04:10.3 |   -0.57275 |    3.95213 |                                                                                                              
|        10 | 16:04:10.8 |   -0.38175 |    6.95915 |                                                                                                              
|        11 | 16:04:11.3 |   -0.19100 |   16.55696 |                                                                                                              
|        12 | 16:04:11.8 |    0.00000 |   70.42530 |                                                                                                              
|        13 | 16:04:12.3 |    0.19100 | 13755.87188 |                                                                                                             
|        14 | 16:04:12.8 |    0.38175 |   55.43604 |                                                                                                              
|        15 | 16:04:13.3 |    0.57275 |   14.16108 |                                                                                                              
|        16 | 16:04:13.8 |    0.76375 |    6.47230 |                                                                                                              
|        17 | 16:04:14.3 |    0.95450 |    3.74920 |                                                                                                              
|        18 | 16:04:14.8 |    1.14550 |    2.34491 |                                                                                                              
|        19 | 16:04:15.3 |    1.33625 |    1.64712 |                                                                                                              
|        20 | 16:04:15.8 |    1.52725 |    1.20580 |                                                                                                              
|        21 | 16:04:16.3 |    1.71825 |    0.92989 |                                                                                                              
|        22 | 16:04:16.8 |    1.90900 |    0.73870 |                                                                                                              
|        23 | 16:04:17.3 |    2.10000 |    0.60145 |                                                                                                              
```

but failed (at the end) with this console trace:

```
/home/beams/JEMIAN/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/epics/ca.py:1524: UserWarning: ca.get('sky:userCalcOut3.STAT') timed out after 10.00 seconds.
  warnings.warn(msg % (name(chid), timeout))
+-----------+------------+------------+------------+                                                                                                              
generator rel_scan ['924b5d73'] (scan num: 8854)
---------------------------------------------------------------------------
ReadTimeoutError                          Traceback (most recent call last)
<ipython-input-1-041856b82ed5> in <module>
----> 1 uids = RE(repeat_findpeak(3000))

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/run_engine.py in __call__(self, *args, **metadata_kw)
    805             self._task_fut.add_done_callback(set_blocking_event)
    806 
--> 807         self._resume_task(init_func=_build_task)
    808 
    809         if self._interrupted:

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/run_engine.py in _resume_task(self, init_func)
    929                     if (exc is not None
    930                             and not isinstance(exc, _RunEnginePanic)):
--> 931                         raise exc
    932 
    933     def install_suspender(self, suspender):

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/run_engine.py in _run(self)
   1498             exit_reason = str(err)
   1499             self.log.exception("Run aborted")
-> 1500             raise err
   1501         finally:
   1502             if not exit_reason:

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/run_engine.py in _run(self)
   1363                     else:
   1364                         try:
-> 1365                             msg = self._plan_stack[-1].send(resp)
   1366                         # We have exhausted the top generator
   1367                         except StopIteration:

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in __call__(self, plan)
   1305         plan = monitor_during_wrapper(plan, self.monitors)
   1306         plan = baseline_wrapper(plan, self.baseline)
-> 1307         return (yield from plan)
   1308 
   1309 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in baseline_wrapper(plan, devices, name)
   1160         return (yield from plan)
   1161     else:
-> 1162         return (yield from plan_mutator(plan, insert_baseline))
   1163 
   1164 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    168                     continue
    169                 else:
--> 170                     raise ex
    171         # if inserting / mutating, put new generator on the stack
    172         # and replace the current msg with the first element from the

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    121             ret = result_stack.pop()
    122             try:
--> 123                 msg = plan_stack[-1].send(ret)
    124             except StopIteration as e:
    125                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in monitor_during_wrapper(plan, signals)
    801     plan1 = plan_mutator(plan, insert_after_open)
    802     plan2 = plan_mutator(plan1, insert_before_close)
--> 803     return (yield from plan2)
    804 
    805 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    168                     continue
    169                 else:
--> 170                     raise ex
    171         # if inserting / mutating, put new generator on the stack
    172         # and replace the current msg with the first element from the

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    121             ret = result_stack.pop()
    122             try:
--> 123                 msg = plan_stack[-1].send(ret)
    124             except StopIteration as e:
    125                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    168                     continue
    169                 else:
--> 170                     raise ex
    171         # if inserting / mutating, put new generator on the stack
    172         # and replace the current msg with the first element from the

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    121             ret = result_stack.pop()
    122             try:
--> 123                 msg = plan_stack[-1].send(ret)
    124             except StopIteration as e:
    125                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in fly_during_wrapper(plan, flyers)
    859     plan1 = plan_mutator(plan, insert_after_open)
    860     plan2 = plan_mutator(plan1, insert_before_close)
--> 861     return (yield from plan2)
    862 
    863 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    168                     continue
    169                 else:
--> 170                     raise ex
    171         # if inserting / mutating, put new generator on the stack
    172         # and replace the current msg with the first element from the

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    121             ret = result_stack.pop()
    122             try:
--> 123                 msg = plan_stack[-1].send(ret)
    124             except StopIteration as e:
    125                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    168                     continue
    169                 else:
--> 170                     raise ex
    171         # if inserting / mutating, put new generator on the stack
    172         # and replace the current msg with the first element from the

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    121             ret = result_stack.pop()
    122             try:
--> 123                 msg = plan_stack[-1].send(ret)
    124             except StopIteration as e:
    125                 # discard the exhausted generator

~/.ipython/profile_bluesky/startup/instrument/plans/example.py in repeat_findpeak(iters)
    111     # so peak finding fails.
    112     for _i in range(iters):
--> 113         apstools.utils.trim_plot_lines(bec, 4, m1, noisy)
    114         change_peak()
    115         yield from example_findpeak()

~/.ipython/profile_bluesky/startup/instrument/plans/example.py in example_findpeak(number_of_scans, number_of_points)
     76     for _again in range(number_of_scans):
     77         m1.move(cen)
---> 78         yield from bp.rel_scan([noisy], m1, -k*fwhm, k*fwhm, number_of_points)
     79         if "noisy" not in peaks["fwhm"]:
     80             logger.error("no data in `peaks`, end of these scans")

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/plans.py in rel_scan(detectors, num, per_step, md, *args)
   1388                                 per_step=per_step, md=_md))
   1389 
-> 1390     return (yield from inner_rel_scan())
   1391 
   1392 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/utils.py in dec_inner(*inner_args, **inner_kwargs)
   1112                 plan = gen_func(*inner_args, **inner_kwargs)
   1113                 plan = wrapper(plan, *args, **kwargs)
-> 1114                 return (yield from plan)
   1115             return dec_inner
   1116         return dec

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in reset_positions_wrapper(plan, devices)
   1117         yield Msg('wait', None, group=blk_grp)
   1118 
-> 1119     return (yield from finalize_wrapper(plan_mutator(plan, insert_reads),
   1120                                         reset()))
   1121 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in finalize_wrapper(plan, final_plan, pause_for_debug)
    507     cleanup = True
    508     try:
--> 509         ret = yield from plan
    510     except GeneratorExit:
    511         cleanup = False

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
     76             # if we have a stashed exception, pass it along
     77             try:
---> 78                 msg = plan_stack[-1].throw(exception)
     79             except StopIteration as e:
     80                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/utils.py in dec_inner(*inner_args, **inner_kwargs)
   1112                 plan = gen_func(*inner_args, **inner_kwargs)
   1113                 plan = wrapper(plan, *args, **kwargs)
-> 1114                 return (yield from plan)
   1115             return dec_inner
   1116         return dec

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in relative_set_wrapper(plan, devices)
   1073     plan = plan_mutator(plan, insert_reads)
   1074     plan = msg_mutator(plan, rewrite_pos)
-> 1075     return (yield from plan)
   1076 
   1077 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in msg_mutator(plan, msg_proc)
    243                 ret = None
    244                 continue
--> 245             ret = yield msg
    246         except StopIteration as e:
    247             return e.value

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    193         try:
    194             # yield out the 'current message' and collect the return
--> 195             inner_ret = yield msg
    196         except GeneratorExit:
    197             # special case GeneratorExit.  We must clean up all of our plans

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    193         try:
    194             # yield out the 'current message' and collect the return
--> 195             inner_ret = yield msg
    196         except GeneratorExit:
    197             # special case GeneratorExit.  We must clean up all of our plans

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
     76             # if we have a stashed exception, pass it along
     77             try:
---> 78                 msg = plan_stack[-1].throw(exception)
     79             except StopIteration as e:
     80                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in new_gen()
    851                 yield from ensure_generator(complete_msgs)
    852                 yield from ensure_generator(collect_msgs)
--> 853                 yield msg
    854             return new_gen(), None
    855         else:

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    193         try:
    194             # yield out the 'current message' and collect the return
--> 195             inner_ret = yield msg
    196         except GeneratorExit:
    197             # special case GeneratorExit.  We must clean up all of our plans

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    193         try:
    194             # yield out the 'current message' and collect the return
--> 195             inner_ret = yield msg
    196         except GeneratorExit:
    197             # special case GeneratorExit.  We must clean up all of our plans

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
     76             # if we have a stashed exception, pass it along
     77             try:
---> 78                 msg = plan_stack[-1].throw(exception)
     79             except StopIteration as e:
     80                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in new_gen()
    793             def new_gen():
    794                 yield from ensure_generator(unmonitor_msgs)
--> 795                 yield msg
    796             return new_gen(), None
    797         else:

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    193         try:
    194             # yield out the 'current message' and collect the return
--> 195             inner_ret = yield msg
    196         except GeneratorExit:
    197             # special case GeneratorExit.  We must clean up all of our plans

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
     76             # if we have a stashed exception, pass it along
     77             try:
---> 78                 msg = plan_stack[-1].throw(exception)
     79             except StopIteration as e:
     80                 # discard the exhausted generator

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in post_baseline()
   1149         elif msg.command == 'close_run':
   1150             def post_baseline():
-> 1151                 yield from trigger_and_read(devices, name=name)
   1152                 return (yield msg)
   1153 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/plan_stubs.py in trigger_and_read(devices, name)
    909         return ret
    910     from .preprocessors import rewindable_wrapper
--> 911     return (yield from rewindable_wrapper(inner_trigger_and_read(),
    912                                           rewindable))
    913 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in rewindable_wrapper(plan, rewindable)
    691                                             restore_rewindable()))
    692     else:
--> 693         return (yield from plan)
    694 
    695 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/plan_stubs.py in inner_trigger_and_read()
    903         ret = {}  # collect and return readings to give plan access to them
    904         for obj in devices:
--> 905             reading = (yield from read(obj))
    906             if reading is not None:
    907                 ret.update(reading)

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/plan_stubs.py in read(obj)
     93         Msg('read', obj)
     94     """
---> 95     return (yield Msg('read', obj))
     96 
     97 

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/preprocessors.py in plan_mutator(plan, msg_proc)
    193         try:
    194             # yield out the 'current message' and collect the return
--> 195             inner_ret = yield msg
    196         except GeneratorExit:
    197             # special case GeneratorExit.  We must clean up all of our plans

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/run_engine.py in _run(self)
   1423                         # exceptions (coming in via throw) can be
   1424                         # raised
-> 1425                         new_response = await coro(msg)
   1426 
   1427                     # special case `CancelledError` and let the outer

~/.conda/envs/bluesky_2020_9/lib/python3.8/site-packages/bluesky/run_engine.py in _read(self, msg)
   1668         obj = msg.obj
   1669         # actually _read_ the object
-> 1670         ret = obj.read(*msg.args, **msg.kwargs)
   1671 
   1672         if ret is None:

/home/beams1/JEMIAN/Documents/projects/Bluesky/ophyd/ophyd/device.py in read(self)
   1235 
   1236         for _, component in self._get_components_of_kind(Kind.normal):
-> 1237             res.update(component.read())
   1238         return res
   1239 

/home/beams1/JEMIAN/Documents/projects/Bluesky/ophyd/ophyd/device.py in read(self)
   1235 
   1236         for _, component in self._get_components_of_kind(Kind.normal):
-> 1237             res.update(component.read())
   1238         return res
   1239 

/home/beams1/JEMIAN/Documents/projects/Bluesky/ophyd/ophyd/utils/epics_pvs.py in wrapper(self, *args, **kwargs)
    196     def wrapper(self, *args, **kwargs):
    197         if self.connected:
--> 198             return fcn(self, *args, **kwargs)
    199         else:
    200             raise DisconnectedError('{} is not connected'.format(self.name))

/home/beams1/JEMIAN/Documents/projects/Bluesky/ophyd/ophyd/signal.py in read(self)
    385             dict
    386         '''
--> 387         value = self.get()
    388         return {self.name: {'value': value,
    389                             'timestamp': self.timestamp}}

/home/beams1/JEMIAN/Documents/projects/Bluesky/ophyd/ophyd/signal.py in get(self, as_string, timeout, connection_timeout, form, use_monitor, **kwargs)
   1142             use_monitor = self._auto_monitor
   1143 
-> 1144         info = self._get_with_timeout(
   1145             self._read_pv, timeout, connection_timeout, as_string, form, use_monitor
   1146         )

/home/beams1/JEMIAN/Documents/projects/Bluesky/ophyd/ophyd/signal.py in _get_with_timeout(self, pv, timeout, connection_timeout, as_string, form, use_monitor)
   1096 
   1097         if info is None:
-> 1098             raise ReadTimeoutError(
   1099                 f"Failed to read {pv.pvname} "
   1100                 f"within {timeout:.2f} sec")

ReadTimeoutError: Failed to read sky:userCalcOut3.STAT within 10.00 sec

In [2]: 
```
