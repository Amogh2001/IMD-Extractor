import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import math

import day_classify as dc
from rainfall_sep import Rainfall_Sep
from rain_classify import rain_classifier
from conmat_classify import mat_rain_classifier
from month_classifier import Rainfall_Year
from monthly_mat_classifier import monthly_rain_classifier
import imd_nc_extractor as imd
import rmse_funcs as rmfn



data = imd.nc_extractor_025('IMD_0.25_2001.nc')
data.bang_rain_getter(leap = False)
imd_22_north = np.array(data.bang_north)
imd_22_south = np.array(data.bang_south)
imd_22_east = np.array(data.bang_east)
imd_22_west = np.array(data.bang_west)
imd_22_ne = np.array(data.bang_ne)
imd_22_se = np.array(data.bang_se)
imd_22_nw = np.array(data.bang_nw)
imd_22_sw = np.array(data.bang_sw)
imd_22_central = np.array(data.bang_central)
imd_22_sum = np.zeros(1)

for inc_sum in range(0, 365):
    imd_bang_sum = (imd_22_north[inc_sum] + imd_22_south[inc_sum] + imd_22_east[inc_sum] + imd_22_west[inc_sum] + imd_22_ne[inc_sum] + imd_22_se[inc_sum] + imd_22_nw[inc_sum] + imd_22_sw[inc_sum])/8
    imd_22_sum = np.append(imd_22_sum, imd_bang_sum)    
imd_22_sum = np.delete(imd_22_sum, 0)

r_imd = np.zeros(1)

for i_inc in range(0, 365):
    if imd_22_central[i_inc] > 1.5:
        r_imd = np.append(r_imd, imd_22_se[i_inc])
#df_imd = pd.DataFrame(imd_22_sum)
r_imd = np.delete(r_imd, 0)

#==================================== IMERG Data ==================================

imerg = xr.open_dataset('IMERG_LateRun/IMERG_LR_2001-2023.nc')

imerg_rainfall = imerg['GPM_3IMERGDL_06_precipitationCal']
imerg_yearly = imerg_rainfall.groupby('time.year')

imerg_monthly = imerg_yearly[2001].groupby('time.month')
gpm_22 = []
gpm_22_days = []
for month_gpm in range(1, 13):
    imerg_daily = imerg_monthly[month_gpm].groupby('time.day')
    gpm_22.append(imerg_daily)
            
for i in range(0,12):
    for j in range(1, dc.day_range(i, leap = False)+1):
        gpm_22_days.append(float(xr.DataArray(np.array(gpm_22[i][j]))))
#print(gpm_22_days)
 
r_gpm = np.zeros(1)

for g_inc in range(0, 365):
    if gpm_22_days[g_inc] > 1.5:
        r_gpm = np.append(r_gpm, gpm_22_days[g_inc])
df_gpm = pd.DataFrame(gpm_22_days)
r_gpm = np.delete(r_gpm, 0)

#======================== Finding RMSE =====================================

rmse_arr = np.zeros(1)
rmse_arr_ind = np.zeros(1)
resid_arr = np.zeros(1)
gpm_arr = np.zeros(1)

for inc1 in range(0, 365): 
    resid_arr = np.append(resid_arr, rmfn.residual_finder(imd_22_nw[inc1], gpm_22_days[inc1]))
resid_arr = np.delete(resid_arr, 0)

for inc2 in range(0,365):
    rmse_arr = np.append(rmse_arr, rmfn.rmse_finder(imd_22_nw[inc2], gpm_22_days[inc2]))    
print(max(rmse_arr))
rmse_arr = np.delete(rmse_arr, 0)


for inc3 in range(0, 365):
    rmse_arr_ind = np.append(rmse_arr_ind, rmfn.rmse_finder_ind(imd_22_nw[inc3],gpm_22_days[inc3]))
rmse_arr_ind = np.delete(rmse_arr_ind, 0)
rmse_fin = math.sqrt(sum(rmse_arr_ind)/365)
print(rmse_fin)

#======================= Plotting =========================================
#plt.scatter(r_imd, r_gpm)
#plt.plot(resid_arr)
plt.scatter(gpm_22_days, imd_22_sum) 
plt.title('Residual Plot- 2022 Rainfall over Bangalore')
plt.xlabel('2022 Days')  
plt.ylabel('Bangalore Rainfall Residual (IMD - IMERG) (mm)')
plt.grid()
plt.show()
