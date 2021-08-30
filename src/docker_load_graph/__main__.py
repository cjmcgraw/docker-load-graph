import pandas as pd
import numpy as np
import argparse
import math

from docker_load_graph import docker_helper as d
from docker_load_graph import plotting

p = argparse.ArgumentParser()
args = p.parse_args()


ordered_valid_keys = [
    'block_io_mb_write',
    'block_io_mb_read',
    'mem_used_mb',
    'cpu_used',
    'cores_used',
    'pids',
    'mem_used_%',
    'mem_cache_mb',
    'mem_total_used_mb',
]

df = pd.DataFrame()
try:
    for record in d.stream_docker_stats(d.get_all_containers()):
        record['timestamp'] = pd.to_datetime(record['timestamp'])
        df = df.append(record, ignore_index=True)
        plotting.plot(
            df, 
            ordered_keys=ordered_valid_keys, 
            max_rows=3,
            max_cols=2
        )
except KeyboardInterrupt as err:
    ...


