import pathlib as pl

target_dir = pl.Path("./test_dir")

for i in target_dir.iterdir():
    if i.is_dir():
        print("dir :", i)
    else:
        print("file:", i)

