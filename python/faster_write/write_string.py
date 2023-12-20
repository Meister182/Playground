import pathlib as pl

string = "asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd\n"

target = pl.Path("./string.txt")

fd = target.open("a")
for i in range(10000000):
    fd.write(string)


# time
#  real    0m2.591s
#  user    0m1.637s
#  sys     0m0.952s

