import os
from math import pi
from fpath import *

nH0_list = [1]        # [cm^-3]
lamobs_list = [1.14, 1.39, 1.54, 0.90, 1.15, 1.5, 2.0, 2.77, 3.56, 4.44]    # micron
theobs_list = [20*pi/180,30*pi/180.]   # radian


for i in range(len(nH0_list)):
    nH0 = nH0_list[i]
    for j in range(len(lamobs_list)):
        lamobs = lamobs_list[j]
        for k in range(len(theobs_list)):
            theobs = theobs_list[k]
            os.system('python ' + codedir + 'Ldnu_obs.py ' +
                      '%.1e ' % nH0 + '%.2f ' % lamobs + '%.3f ' % theobs)
