import pathlib as pl

bytes = b"asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd\n"

target = pl.Path("./bytes_decoded.txt")

fd = target.open("a")
for i in range(10000000):
    fd.write(bytes.decode("utf-8"))


# time
#  real    0m3.360s
#  user    0m2.633s
#  sys     0m0.725s

