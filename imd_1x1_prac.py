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

#--------------------------------------Station 1 Data-----------------------------------------

list01_11 = ['AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ'] #include 'AM' for 2007
list12_22 = ['AR', 'AS','AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']


bang_stat1_df4 = pd.DataFrame()
bang_stat1_df5 = pd.DataFrame()


for m in list01_11:
    bang_stat1_4 = pd.read_excel('DataSheet1.xlsx', usecols=m)
    bang_stat1_df4 = pd.concat([bang_stat1_df4, (bang_stat1_4[1:369])], axis = 0, ignore_index= True)
bang_stat1_df4 = bang_stat1_df4.stack().reset_index()


for n in list12_22:
    bang_stat1_5 = pd.read_excel('DataSheet1.xlsx', usecols=n)
    bang_stat1_df5 = pd.concat([bang_stat1_df5, (bang_stat1_5[1:369])], axis = 0, ignore_index= True)
bang_stat1_df5 = bang_stat1_df5.stack().reset_index()

bang_stat1_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat1_df5.rename(columns = {0: 'Rainfall'}, inplace=True)


bang_stat1_df4['Rainfall'] = pd.to_numeric(bang_stat1_df4['Rainfall'], errors = 'coerce')
df4_rarr = bang_stat1_df4['Rainfall'].array
df4_rarr = np.insert(df4_rarr, 0, 0.0)
#df4_rarr = np.delete(df4_rarr, 4017)   #include when including 2007

bang_stat1_df5['Rainfall'] = pd.to_numeric(bang_stat1_df5['Rainfall'], errors = 'coerce')
df5_rarr = bang_stat1_df5['Rainfall'].array
df5_rarr = np.insert(df5_rarr, 0, 0.0)
df5_rarr = np.delete(df5_rarr, 3288)

bang_stat1_4_month2001 = dc.month_rain_getter(df4_rarr[1:369])
bang_stat1_4_array = np.array(bang_stat1_4_month2001)
bang_stat1_4_array_test = np.array(bang_stat1_4_month2001)

for num1 in range(1, 11):
    num2 = num1 + 1
    if num2/4 ==1 or num2/7 == 1:
        bang_stat1_4_iter = dc.month_rain_getter(df4_rarr[(369*num1):(369*num2)], leap = True)
        bang_stat1_4_array_test = np.append(bang_stat1_4_array_test, bang_stat1_4_iter)
    else:
        bang_stat1_4_iter = dc.month_rain_getter(df4_rarr[(369*num1):(369*num2)])
        bang_stat1_4_array_test = np.append(bang_stat1_4_array_test, bang_stat1_4_iter)



#========================================== Station 2 Data ============================================

list01_11 = ['AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS','AT']
list12_22 = ['AU', 'AV']#, 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_stat2_df4 = pd.DataFrame()
bang_stat2_df5 = pd.DataFrame()

for m in list01_11:
    bang_stat2_4 = pd.read_excel('DataSheet_2.xlsx', usecols=m)
    bang_stat2_df4 = pd.concat([bang_stat2_df4, (bang_stat2_4[1:368])], axis = 0, ignore_index= True)
bang_stat2_df4 = bang_stat2_df4.stack().reset_index()

for n in list12_22:
    bang_stat2_5 = pd.read_excel('DataSheet_2.xlsx', usecols=n)
    bang_stat2_df5 = pd.concat([bang_stat2_df5, (bang_stat2_5[1:368])], axis = 0, ignore_index= True)
bang_stat2_df5 = bang_stat2_df5.stack().reset_index()

bang_stat2_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat2_df5.rename(columns = {0: 'Rainfall'}, inplace=True)

bang_stat2_df4['Rainfall'] = pd.to_numeric(bang_stat2_df4['Rainfall'], errors = 'coerce')
df4_rarr_stat2 = bang_stat2_df4['Rainfall'].array
df4_rarr_stat2 = np.insert(df4_rarr_stat2, 0, 0.0)
#df4_rarr_stat2 = np.delete(df4_rarr_stat2, 4017)

bang_stat2_df5['Rainfall'] = pd.to_numeric(bang_stat2_df5['Rainfall'], errors = 'coerce')
df5_rarr_stat2 = bang_stat2_df5['Rainfall'].array
df5_rarr_stat2 = np.insert(df5_rarr_stat2, 0, 0.0)
#df5_rarr_stat2 = np.delete(df5_rarr_stat2, 3288)

bang_stat2_4_month2001 = dc.month_rain_getter(df4_rarr_stat2[1:368])
bang_stat2_4_array = np.array(bang_stat2_4_month2001)
bang_stat2_4_array_test = np.array(bang_stat2_4_month2001)

for num1_stat2 in range(1, 11):
    num2_stat2 = num1_stat2 + 1
    if num2_stat2 % 4 == 0:
        bang_stat2_4_iter = dc.month_rain_getter(df4_rarr_stat2[(368*num1_stat2):(368*num2_stat2)], leap = True)
        bang_stat2_4_array_test = np.append(bang_stat2_4_array_test, bang_stat2_4_iter)
    else:
        bang_stat2_4_iter = dc.month_rain_getter(df4_rarr_stat2[(368*num1_stat2):(368*num2_stat2)])
        bang_stat2_4_array_test = np.append(bang_stat2_4_array_test, bang_stat2_4_iter)


#==================================== Station 3 Data=============================

list01_11 = [ 'AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS','AT']
list12_22 = ['AU', 'AV']#, 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_stat3_df4 = pd.DataFrame()
bang_stat3_df5 = pd.DataFrame()

for m in list01_11:
    bang_stat3_4 = pd.read_excel('DataSheet_3.xlsx', usecols=m)
    bang_stat3_df4 = pd.concat([bang_stat3_df4, (bang_stat3_4[1:368])], axis = 0, ignore_index= True)
bang_stat3_df4 = bang_stat3_df4.stack().reset_index()


for n in list12_22:
    bang_stat3_5 = pd.read_excel('DataSheet_3.xlsx', usecols=n)
    bang_stat3_df5 = pd.concat([bang_stat3_df5, (bang_stat3_5[1:369])], axis = 0, ignore_index= True)
bang_stat3_df5 = bang_stat3_df5.stack().reset_index()

bang_stat3_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat3_df5.rename(columns = {0: 'Rainfall'}, inplace=True)

bang_stat3_df4['Rainfall'] = pd.to_numeric(bang_stat3_df4['Rainfall'], errors = 'coerce')
df4_rarr_stat3 = bang_stat3_df4['Rainfall'].array
df4_rarr_stat3 = np.insert(df4_rarr_stat3, 0, 0.0)
#df4_rarr = np.delete(df4_rarr, 4017)

bang_stat3_df5['Rainfall'] = pd.to_numeric(bang_stat3_df5['Rainfall'], errors = 'coerce')
df5_rarr_stat3 = bang_stat3_df5['Rainfall'].array
df5_rarr_stat3 = np.insert(df5_rarr_stat3, 0, 0.0)
#df5_rarr_stat3 = np.delete(df5_rarr_stat3, 3288)


bang_stat3_4_month2001 = dc.month_rain_getter(df4_rarr_stat3[1:368])
bang_stat3_4_array = np.array(bang_stat3_4_month2001)
bang_stat3_4_array_test = np.array(bang_stat3_4_month2001)

for num1_stat3 in range(1, 11):
    num2_stat3 = num1_stat3 + 1
    if num2_stat3 % 4 == 0:
        bang_stat3_4_iter = dc.month_rain_getter(df4_rarr_stat3[(368*num1_stat3):(368*num2_stat3)], leap = True)
        bang_stat3_4_array_test = np.append(bang_stat3_4_array_test, bang_stat3_4_iter)
    else:
        bang_stat3_4_iter = dc.month_rain_getter(df4_rarr_stat3[(368*num1_stat3):(368*num2_stat3)])
        bang_stat3_4_array_test = np.append(bang_stat3_4_array_test, bang_stat3_4_iter)

#================================ Mean of 3 stations =======================================


stat1_df1 = pd.DataFrame(bang_stat1_4_array_test)
stat2_df1 = pd.DataFrame(bang_stat2_4_array_test)
stat3_df1 = pd.DataFrame(bang_stat3_4_array_test)


frames_1_mon = [stat1_df1, stat3_df1]
mon_cat_1 = pd.concat(frames_1_mon, axis = 1, join = 'inner')

frames_2_mon = [mon_cat_1, stat2_df1]
mon_cat2 = pd.concat(frames_2_mon, axis = 1, join = 'inner')

mon_sum1 = mon_cat2.sum(axis=1)
df_com_mean = mon_sum1.div(3.0)

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
