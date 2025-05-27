#!/usr/bin/env python3.11

from contextlib import nullcontext
import json
import multiprocessing
import time
from pathlib import Path

TARGET_FILE = "output_*.json"
PROCESSES = 3
REPETITIONS = 5
DELAY = 0

MP_LOCK = nullcontext()

def dummy_function(args):
    id = args[0]
    file_path = args[1]
    def msg(*args, **kwargs):
        print(f"Process {id}:", *args, **kwargs)

    msg("Sarted")
    with MP_LOCK:
        msg("Inside lock")
        try:
            with file_path.open("r") as f:
                content = json.load(f)
            #msg("Read file:", file_path)
        except FileNotFoundError:
            #msg("Could not find file:", file_path)
            content = []
        # except json.JSONDecodeError:
        # except json.decoder.JSONDecodeError:
            # msg("FAILED TO READ FILE:", file_path)
            # content = []

        #msg("Appending to content")
        for _ in range(REPETITIONS):
            content.append(f"Process {id}: Writing line at {time.time()}")
            time.sleep(DELAY)

        with file_path.open("w") as f:
            #msg("Writing to file:", file_path)
            json.dump(content, f, indent=4)
    msg("Release lock")


if __name__ == "__main__":
    # Rotate target file just in case
    print("Selecting file...")
    existing_files = list(Path('.').glob("output_*json"))
    if existing_files:
        last_file = max(existing_files, key=lambda x: int(x.stem.split('_')[1]))
        last_number = int(last_file.stem.split('_')[1])
        dir = Path(f"./output_{last_number + 1:02}.json")
    else:
        dir = Path("./output_00.json")
    print("Using:", dir)


    print("Launching processes..")
    processes = []
    lock = multiprocessing.Lock()
    def init_worker():
        global MP_LOCK
        MP_LOCK = lock
    with multiprocessing.Pool(PROCESSES, initializer=init_worker) as pool:
        pool.map(dummy_function, [(id, dir) for id in range(PROCESSES)])

