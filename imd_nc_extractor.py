import xarray as xr
import numpy as np
import pandas as pd
import netCDF4 as nc
from day_classify import day_range

class nc_extractor:
    
    def __init__(self, year_nc, leap = None):
        self.year = year_nc
        
        self.data = xr.open_dataset(year_nc)
        
        self.rainfall_data = self.data['RAINFALL']
        
        self.rf_arr = []
        
        if leap == True:
            for days in range(0, 366):
                self.rf_arr.append(self.rainfall_data[days][7][11])
            self.bang_rf = xr.DataArray(np.array(self.rf_arr))
        
        else:
            for days in range(0, 365):
                self.rf_arr.append(self.rainfall_data[days][7][11])
            self.bang_rf = xr.DataArray(np.array(self.rf_arr))

class nc_extractor_025:
    
    def __init__(self, year_nc, leap = None):
        self.year = year_nc
        
        self.data = xr.open_dataset(year_nc)
        
        self.rainfall_data_025 = self.data['RAINFALL']
        
        self.rf_arr_sw = []
        self.rf_arr_south = []
        self.rf_arr_se = []
        self.rf_arr_ne = []
        self.rf_arr_north = []
        self.rf_arr_nw = []
        self.rf_arr_central = []
        self.rf_arr_west = []
        self.rf_arr_east = []
        
    def bang_rain_getter(self, leap = None):  
         
        if leap == True:
            for days in range(0, 366):
                self.rf_arr_sw.append(self.rainfall_data_025[days][25][43])
                self.rf_arr_south.append(self.rainfall_data_025[days][25][44])
                self.rf_arr_se.append(self.rainfall_data_025[days][25][45])
                self.rf_arr_ne.append(self.rainfall_data_025[days][26][45])
                self.rf_arr_north.append(self.rainfall_data_025[days][27][44])
                self.rf_arr_nw.append(self.rainfall_data_025[days][27][43])
                self.rf_arr_central.append(self.rainfall_data_025[days][26][44])
                self.rf_arr_west.append(self.rainfall_data_025[days][26][43])
                self.rf_arr_east.append(self.rainfall_data_025[days][26][46])
                
            self.bang_sw = xr.DataArray(np.array(self.rf_arr_sw))                # Bangalore South-West, Region: 77.25E, 12.75N
            self.bang_south = xr.DataArray(np.array(self.rf_arr_south))          # Bangalore South,      Region: 77.50E, 12.75N
            self.bang_se = xr.DataArray(np.array(self.rf_arr_se))                # Bangalore South-East, Region: 77.75E, 12.75N 
            self.bang_ne = xr.DataArray(np.array(self.rf_arr_ne))                # Bangalore North-East, Region: 77.75E, 13.00N
            self.bang_north = xr.DataArray(np.array(self.rf_arr_north))          # Bangalore North,      Region: 77.50E, 13.25N
            self.bang_nw = xr.DataArray(np.array(self.rf_arr_nw))                # Bangalore North-West, Region: 77.25E, 13.25N
            self.bang_central = xr.DataArray(np.array(self.rf_arr_central))      # Bangalore Central,    Region: 77.50E, 13.00N
            self.bang_west = xr.DataArray(np.array(self.rf_arr_west))            # Bangalore West,       Region: 77.25E, 13.00N
            self.bang_east = xr.DataArray(np.array(self.rf_arr_east))            # Bangalore East,       Region: 78.00E, 13.00N
            
        else:
            for days in range(0, 365):
                self.rf_arr_sw.append(self.rainfall_data_025[days][25][43])
                self.rf_arr_south.append(self.rainfall_data_025[days][25][44])
                self.rf_arr_se.append(self.rainfall_data_025[days][25][45])
                self.rf_arr_ne.append(self.rainfall_data_025[days][26][45])
                self.rf_arr_north.append(self.rainfall_data_025[days][27][44])
                self.rf_arr_nw.append(self.rainfall_data_025[days][27][43])
                self.rf_arr_central.append(self.rainfall_data_025[days][26][44])
                self.rf_arr_west.append(self.rainfall_data_025[days][26][43])
                self.rf_arr_east.append(self.rainfall_data_025[days][26][46])
                
            self.bang_sw = xr.DataArray(np.array(self.rf_arr_sw))
            self.bang_south = xr.DataArray(np.array(self.rf_arr_south))
            self.bang_se = xr.DataArray(np.array(self.rf_arr_se))
            self.bang_ne = xr.DataArray(np.array(self.rf_arr_ne))
            self.bang_north = xr.DataArray(np.array(self.rf_arr_north))
            self.bang_nw = xr.DataArray(np.array(self.rf_arr_nw))
            self.bang_central = xr.DataArray(np.array(self.rf_arr_central))
            self.bang_west = xr.DataArray(np.array(self.rf_arr_west))
            self.bang_east = xr.DataArray(np.array(self.rf_arr_east))