
 
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import datetime
import pandas as pd
import matplotlib.pyplot as plt

SAR=Dataset('GW_L2P_SAR_ENVI_GDR_20060101_000335_20060101_000935_0043_0474.nc','r')

#print SAR.variables.keys()

#print SAR.variables['swh']


swh= np.array(SAR.variables['swh'][:])
swh_part_calibrated= np.array(SAR.variables['swh_part_calibrated'][:])
ddr_part_calibrated= np.array(SAR.variables['ddr_part_calibrated'][:])
lat= np.array(SAR.variables['lat'][:])
lon= np.array(SAR.variables['lon'][:])
time= np.array(SAR.variables['time'][:]).astype(np.float)


ddr_part_calibrated[ddr_part_calibrated==-32767]=np.nan
fecha = np.array([datetime.datetime(1985,01,01)+\
datetime.timedelta(seconds = time[i]) for i in range(len(time))])


