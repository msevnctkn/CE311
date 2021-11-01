import library
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as p
# arrow for single load
#plt.text(18.5, 13, "20 kN", size=15)
plt.xlim(left=-10, right=50), plt.ylim(bottom=-10, top=30)
tool = library.Tool()


#tool.pinned_support(x=10, y=10, r=0.3, color="blue")
tool.simple_beam(x1=0, y1=12, x2=27, y2=12, color="purple", linewidth=4)
tool.simple_beam(x1=8, y1=0, x2=8, y2=12, color="purple", linewidth=4)
tool.simple_beam(x1=27, y1=12, x2=35, y2=0, color="purple", linewidth=4)
# pinned ekle
# tool.roller_support(x=35, y=-.5, r=0.5, color="blue")


tool.uniform_distributed_load(x1=12, y1=13, x2=30, y2=13, color="blue")
tool.single_load(x=37, y=6, dx=-5, dy=0, color="blue")
tool.triangular_distributed_load(x1=8, y1=12, x2=8, y2=0, color="blue")
tool.single_load(x=0, y=17, dx=0, dy=-3, color="blue")

plt.show()



