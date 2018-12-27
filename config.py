"""
 This is the COSIPY configuration (init) file.
 Please make your changes here.
"""
## Simulation period
time_start = '2014-01-01T06:00'
time_end   = '2014-10-30T23:00'
time_start_str=(time_start[0:10]).replace('-','')
time_end_str=(time_end[0:10]).replace('-','')

##  Input/Output files
data_path = './data'
input_netcdf= 'Hintereisferner_input.nc'
output_netcdf = 'Hintereisferner_output-'+time_start_str+'-'+time_end_str+'.nc'

## Set keyword to true if you want to use the job scheduler Slurm (own configuration file slurm_config.py)
slurm_use = False

## Port for local cluster
local_port = 8786

## Write full fields
full_field = False

## Restart
restart = False

## If total precipitation and snowfall in input data use total precipitation!
force_use_TP = True

## Time step in the input files [s]
dt = 3600                                           # 3600, 7200, 10800 [s] length of time step per iteration in seconds

## Properties for debug
debug_level = 0                                     # DEBUG levels: 0, 10, 20, 30

## Merging level
merging = False
density_threshold_merging = 5                       # If merging is true threshold for layer densities difference two layer
                                                    # try: 5-10 (kg m^-3)
temperature_threshold_merging = 0.05                # If mering is true threshold for layer temperatures to merge
                                                    # try: 0.05-0.1 (K)

## Max. number of layers, just for the restart file
max_layers = 100                 

## CFL criteria
c_stab = 0.5                                        

## Number of workers, if None all cores are used
workers = None
