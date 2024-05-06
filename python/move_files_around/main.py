#!/bin/python3


from pathlib import Path

work_dir = Path(".")

src_glob = "src/file_6"

dst_input = "dst"
dst_input = "dst/file_renamed"
dst_input = "ds*"

# ------------------------------
# glob pattern approach
#   * Cannot perform renames
# ------------------------------
def dst_glob(dst_gblo):
    dst_files = list(work_dir.glob(dst_glob))
    # validate dst
    if len(dst_files) == 0:
        raise Exception("not found")
    elif len(dst_files) > 1:
        raise Exception("too many")
    return dst_files[0]


# ------------------------------
# path approach
#   * Cannot process wild cards
# ------------------------------
def dst_path(dst_input):
    dst = work_dir / dst_input
    if not (dst.is_dir() or dst.parent.is_dir()):
        raise Exception(f"invalid destination {dst_input}")
    return dst

# ------------------------------
# Code
# ------------------------------

# find dst files
#dst = dst_glob(dst_input)
dst = dst_path(dst_input)

# find source files
src_files = work_dir.glob(src_glob)

# Move files
for src_file in src_files:
    # figure out the edstination file
    if dst.is_dir():
        dst_file = dst / src_file.name
    else:
        dst_file = dst
    print(f"moving {src_file} -> {dst}")
   # Move file
    src_file.rename(dst_file)



