# IMD-Extractor
Extracts rainfall data from IMD (Indian Meteorological Department) .nc file and an example usage 

Can extract IMD 1 deg X 1 Deg data using nc_extractor.

Lat/Long data is specified using:

self.rf_arr.append(self.rainfall_data[days][7][11])

where [7] and [11] represent lat and long respectively (Bangalore Coordinates). Refer imd_1x1_prac

Used for 0.25 deg X 0.25 deg data, one can get the desired coordinate by changing the numbers in bang_rain_getter

For example:

self.rf_arr_sw.append(self.rainfall_data_025[days][25][43])

returns the values for Bangalore South-West, Region: 77.25E, 12.75N

Incrementing Latitude by one (25 to 26) gives:

self.rf_arr_sw.append(self.rainfall_data_025[days][26][43])

which returns values for the region 77.25E, 13.00N
