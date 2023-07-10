# IMD-Extractor
Extracts rainfall data from IMD (Indian Meteorological Department) .nc file

Used for 0.25 deg X 0.25 deg data, one can get the desired coordinate by changing the numbers in bang_rain_getter

For example:

self.rf_arr_sw.append(self.rainfall_data_025[days][25][43])

returns the values for Bangalore South-West, Region: 77.25E, 12.75N

Incrementing Latitude by one (25 to 26) gives:

self.rf_arr_sw.append(self.rainfall_data_025[days][26][43])

which returns values for the region 77.25E, 13.00N
