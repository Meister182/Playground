import pathlib as pl

bytes = b"asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd_asd_dsa_asd\n"

target = pl.Path("./bytes.txt")

fd = target.open("ab")
for i in range(10000000):
    fd.write(bytes)


# time
#  real    0m2.722s
#  user    0m1.730s
#  sys     0m0.991s
  
