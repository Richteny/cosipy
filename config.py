"""
 This is the COSIPY configuration (init) file.
 Please make your changes here.
"""

#-----------------------------------
# SIMULATION PERIOD 
#-----------------------------------
# Abramov
time_start = '2016-01-01T00:00'
time_end   = '2016-03-31T23:59'

# Hintereisferner
#time_start = '2018-09-17T08:00'
#time_end   = '2019-07-03T13:00'

#-----------------------------------
# FILENAMES AND PATHS 
#-----------------------------------
time_start_str=(time_start[0:10]).replace('-','')
time_end_str=(time_end[0:10]).replace('-','')

data_path = './data/'

# Zhadang example
# n_agg version -> 'Abramov/Abramov_n_agg_ERA5L_06_09_2016.nc'
# agg version ->  'Abramov/Abramov_ERA5L_1981_2019.nc'
input_netcdf= 'Abramov/Abramov_n_agg_ERA5L__2016.nc'
output_netcdf = 'Abramov_n_agg_ERA5L_'+time_start_str+'-'+time_end_str+'.nc'

# Hintereisferner example
#input_netcdf = 'HEF/HEF_input.nc'
#output_netcdf = 'hef.nc'

#-----------------------------------
# RESTART 
#-----------------------------------
restart = False                                             # set to true if you want to start from restart file

#-----------------------------------
# STAKE DATA 
#-----------------------------------
stake_evaluation = False 
stakes_loc_file = './data/input/HEF/loc_stakes.csv'         # path to stake location file
stakes_data_file = './data/input/HEF/data_stakes_hef.csv'   # path to stake data file
eval_method = 'rmse'                                        # how to evaluate the simulations ('rmse')
obs_type = 'snowheight'                                     # What kind of stake data is used 'mb' or 'snowheight'

#-----------------------------------
# STANDARD LAT/LON or WRF INPUT 
#-----------------------------------
# Dimensions
WRF = False                                                 # Set to True if you use WRF as input

northing = 'lat'	                                    # name of dimension	in in- and -output
easting = 'lon'					                        # name of dimension in in- and -output
if WRF:
    northing = 'south_north'                                # name of dimension in WRF in- and output
    easting = 'west_east'                                   # name of dimension in WRF in- and output

# Interactive simulation with WRF
WRF_X_CSPY = False

#-----------------------------------
# COMPRESSION of output netCDF
#-----------------------------------
compression_level = 2                                       # Choose value between 1 and 9 (highest compression)
                                                            # Recommendation: choose 1, 2 or 3 (higher not worthwhile, because of needed time for writing output)
#-----------------------------------
# PARALLELIZATION 
#-----------------------------------
slurm_use = True                                          # use SLURM
workers = None                                              # number of workers, if local cluster is used
local_port = 8786                                           # port for local cluster

#-----------------------------------
# WRITE FULL FIELDS 
#-----------------------------------    
full_field = False                                          # write full fields (2D data) to file
if WRF_X_CSPY:
    full_field = True
    
#-----------------------------------
# TOTAL PRECIPITATION  
#-----------------------------------
force_use_TP = True                                        # If total precipitation and snowfall in input data;
                                                            # use total precipitation

#-----------------------------------
# CLOUD COVER FRACTION  
#-----------------------------------
force_use_N = False                                         # If cloud cover fraction and incoming longwave radiation
                                                            # in input data use cloud cover fraction

#-----------------------------------
# SUBSET  (provide pixel values) 
#-----------------------------------
tile = False
xstart = 20
xend = 40
ystart = 20
yend = 40
