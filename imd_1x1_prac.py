import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import math

import day_classify as dc
#from rainfall_sep import Rainfall_Sep
#from rain_classify import rain_classifier
from conmat_classify import mat_rain_classifier
from month_classifier import Rainfall_Year
from monthly_mat_classifier import monthly_rain_classifier
import imd_nc_extractor as imd
import rmse_funcs as rmfn

imd_2001 = imd.nc_extractor('IMD_rain/RF_1x1_2001.nc')
imd_arr01 = np.array(imd_2001.bang_rf)
imd_arr = np.array(imd_arr01)

list_year = (2002, 2003, 2004, 2005, 2006, 2008, 2009, 2010, 2011)

for inc_imd in list_year:
    if inc_imd % 4 == 0:
        imd_mid = imd.nc_extractor('IMD_rain/RF_1x1_'+str(inc_imd)+'.nc', leap = True)
        imd_year = np.array(imd_mid.bang_rf)
        imd_arr = np.append(imd_arr, imd_year)
    else:
        imd_mid = imd.nc_extractor('IMD_rain/RF_1x1_'+str(inc_imd)+'.nc')
        imd_year = np.array(imd_mid.bang_rf)
        imd_arr = np.append(imd_arr, imd_year)
#print(imd_arr[3630:])

#--------------------------------------GKVK Data-----------------------------------------

list01_11 = ['AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ'] #include 'AM' for 2007
list12_22 = ['AR', 'AS','AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_gkvk_df4 = pd.DataFrame()
bang_gkvk_df5 = pd.DataFrame()


for m in list01_11:
    bang_gkvk4 = pd.read_excel('GKVK_DailyRainfall_1.1972-2022.xlsx', usecols=m)
    bang_gkvk_df4 = pd.concat([bang_gkvk_df4, (bang_gkvk4[1:369])], axis = 0, ignore_index= True)
bang_gkvk_df4 = bang_gkvk_df4.stack().reset_index()
#print(bang_gkvk_df3.loc[110:130])

for n in list12_22:
    bang_gkvk5 = pd.read_excel('GKVK_DailyRainfall_1.1972-2022.xlsx', usecols=n)
    bang_gkvk_df5 = pd.concat([bang_gkvk_df5, (bang_gkvk5[1:369])], axis = 0, ignore_index= True)
bang_gkvk_df5 = bang_gkvk_df5.stack().reset_index()

bang_gkvk_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_gkvk_df5.rename(columns = {0: 'Rainfall'}, inplace=True)

bang_gkvk_df4['Rainfall'] = pd.to_numeric(bang_gkvk_df4['Rainfall'], errors = 'coerce')
df4_rarr = bang_gkvk_df4['Rainfall'].array
df4_rarr = np.insert(df4_rarr, 0, 0.0)
#df4_rarr = np.delete(df4_rarr, 4017)   #include when including 2007

bang_gkvk_df5['Rainfall'] = pd.to_numeric(bang_gkvk_df5['Rainfall'], errors = 'coerce')
df5_rarr = bang_gkvk_df5['Rainfall'].array
df5_rarr = np.insert(df5_rarr, 0, 0.0)
#df5_rarr = np.delete(df5_rarr, 3288)
#print(df1_rarr[730:740])

#--------------------------------------HAL Airport Data-----------------------------------------

list01_11 = [ 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS','AT']  #2007 is 'AP'
list12_22 = ['AU', 'AV']#, 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_hal_df4 = pd.DataFrame()
bang_hal_df5 = pd.DataFrame()

for m in list01_11:
    bang_hal4 = pd.read_excel('HAL_Revised_1969.xlsx', usecols=m)
    bang_hal_df4 = pd.concat([bang_hal_df4, (bang_hal4[1:369])], axis = 0, ignore_index= True)
bang_hal_df4 = bang_hal_df4.stack().reset_index()
#print(bang_hal_df3.loc[110:130])

for n in list12_22:
    bang_hal5 = pd.read_excel('HAL_Revised_1969.xlsx', usecols=n)
    bang_hal_df5 = pd.concat([bang_hal_df5, (bang_hal5[1:368])], axis = 0, ignore_index= True)
bang_hal_df5 = bang_hal_df5.stack().reset_index()

bang_hal_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_hal_df5.rename(columns = {0: 'Rainfall'}, inplace=True)


bang_hal_df4['Rainfall'] = pd.to_numeric(bang_hal_df4['Rainfall'], errors = 'coerce')
df4_rarr_hal = bang_hal_df4['Rainfall'].array
df4_rarr_hal = np.insert(df4_rarr_hal, 0, 0.0)
#df4_rarr_hal = np.delete(df4_rarr_hal, 4017)

bang_hal_df5['Rainfall'] = pd.to_numeric(bang_hal_df5['Rainfall'], errors = 'coerce')
df5_rarr_hal = bang_hal_df5['Rainfall'].array
df5_rarr_hal = np.insert(df5_rarr_hal, 0, 0.0)
#df5_rarr_hal = np.delete(df5_rarr_hal, 3288)

#--------------------------------------City Central College Data-----------------------------------------

list01_11 = [ 'AJ', 'AK', 'AL','AM', 'AN', 'AO', 'AQ', 'AR', 'AS','AT']
list12_22 = ['AU', 'AV']#, 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_ccc_df4 = pd.DataFrame()
bang_ccc_df5 = pd.DataFrame()


for m in list01_11:
    bang_ccc4 = pd.read_excel('/media/amogh01/One Touch/prac/City_Central_College_Revised_69-14.xlsx', usecols=m)
    bang_ccc_df4 = pd.concat([bang_ccc_df4, (bang_ccc4[1:368])], axis = 0, ignore_index= True)
bang_ccc_df4 = bang_ccc_df4.stack().reset_index()
#print(bang_ccc_df4[340:370])

for n in list12_22:
    bang_ccc5 = pd.read_excel('/media/amogh01/One Touch/prac/City_Central_College_Revised_69-14.xlsx', usecols=n)
    bang_ccc_df5 = pd.concat([bang_ccc_df5, (bang_ccc5[1:368])], axis = 0, ignore_index= True)
bang_ccc_df5 = bang_ccc_df5.stack().reset_index()

bang_ccc_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_ccc_df5.rename(columns = {0: 'Rainfall'}, inplace=True)


bang_ccc_df4['Rainfall'] = pd.to_numeric(bang_ccc_df4['Rainfall'], errors = 'coerce')
df4_rarr_ccc = bang_ccc_df4['Rainfall'].array
df4_rarr_ccc = np.insert(df4_rarr_ccc, 0, 0.0)
#df4_rarr_ccc = np.delete(df4_rarr_ccc, 4017)   #include when including 2007

bang_ccc_df5['Rainfall'] = pd.to_numeric(bang_ccc_df5['Rainfall'], errors = 'coerce')
df5_rarr_ccc = bang_ccc_df5['Rainfall'].array
df5_rarr_ccc = np.insert(df5_rarr_ccc, 0, 0.0)
#df5_rarr_ccc = np.delete(df5_rarr_ccc, 3288)

#===============================================  Finding Mean of 3 Stations ====================================

df4_gkvk = pd.DataFrame(df4_rarr)
df4_hal = pd.DataFrame(df4_rarr_hal)
df4_ccc = pd.DataFrame(df4_rarr_ccc)

comb_1 = [df4_gkvk, df4_hal]
df_com1 = pd.concat(comb_1, axis = 1, join = 'inner')

comb_2 = [df_com1, df4_ccc]
df_com2 = pd.concat(comb_2, axis = 1, join = 'inner')

df_com_sum = df_com2.sum(axis = 1)
df_com_mean = df_com_sum.div(3.0)

#============================================== Plotting ===============================================

imd_df = pd.DataFrame(imd_arr)
df_com = pd.DataFrame(df_com_mean)
df_com = df_com.iloc[:3651, :] 

imd_df = imd_df.iloc[1:, :]
imd_df = imd_df.stack().reset_index()
imd_df = imd_df.drop('level_0', axis = 1)
imd_df = imd_df.drop('level_1', axis = 1)

imd_df.rename(columns = {0: 'Rainfall'}, inplace = True)
df_com.rename(columns = {0: 'Rainfall'}, inplace = True)

com_mon = np.zeros(1)
imd_mon = np.zeros(1)

for num1 in range(0, 10):                
    num2 = num1 + 1
    if (num2/4 == 1 or num2/7 == 1):
        arr_com = dc.month_rain_getter(df_com['Rainfall'][(366*num1):(366*num2)], leap = True)
        com_mon = np.append(com_mon, arr_com)
        imd_arr = dc.month_rain_getter(imd_df['Rainfall'][(366*num1):(366*num2)], leap = True)
        imd_mon = np.append(imd_mon, imd_arr)
    else:
        arr_com = dc.month_rain_getter(df_com['Rainfall'][(365*num1):(365*num2)])
        com_mon = np.append(com_mon, arr_com)
        imd_arr = dc.month_rain_getter(imd_df['Rainfall'][(365*num1):(365*num2)])
        imd_mon = np.append(imd_mon, imd_arr)



com_mon = np.delete(com_mon, 0)
imd_mon = np.delete(imd_mon, 0)

plt.scatter(imd_mon, com_mon, color = 'hotpink')
plt.title("Scatter Plot- IMD 1x1 Degree Data v/s 3 Station Mean of Bangalore")
plt.xlabel('1x1 Deg Monthly Rainfall (mm)')
plt.ylabel('Bangalore Monthly Mean using 3 Stations (mm)')
plt.grid()
plt.show()


#======================== Finding RMSE =====================================

rmse_arr = np.zeros(1)
rmse_arr_ind = np.zeros(1)
resid_arr = np.zeros(1)


for inc1 in range(0, 120):
    resid_arr = np.append(resid_arr, rmfn.residual_finder(imd_mon[inc1], com_mon[inc1]))
resid_arr = np.delete(resid_arr, 0)
print(resid_arr)

for inc2 in range(0,120):
    rmse_arr = np.append(rmse_arr, rmfn.rmse_finder(imd_mon[inc2], com_mon[inc2]))    
print(max(rmse_arr))
rmse_arr = np.delete(rmse_arr, 0)

for inc3 in range(0, 120):
    rmse_arr_ind = np.append(rmse_arr_ind, rmfn.rmse_finder_ind(imd_mon[inc3], com_mon[inc3]))
rmse_arr_ind = np.delete(rmse_arr_ind, 0)
rmse_fin = math.sqrt(sum(rmse_arr_ind)/120)
print(rmse_fin)