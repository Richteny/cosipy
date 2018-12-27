"""
    Declaration of constants
    Do not modify unless you are absolutely sure what you are doing.
"""
' Inital constants'
initial_snowheight = 0.1
initial_snow_layer_heights = 0.1        # Initial snow layer heights
initial_glacier_layer_heights = 1.0     # Initial glacier layer heights
initial_glacier_height = 20.0           # total domain height (snow+glacier)

initial_top_density_snowpack = 400.     # Top density for inital snowpack
initial_botton_density_snowpack = 600.  # Botton density for inital snowpack

temperature_top = 273.16                # Upper boudary conditation for inital temperature profile (K)
temperature_bottom = 268                # Lower boundary condition for inital tempeature profile (K)
const_init_temp = 0.1                   # constant for init temperature profile used in exponential function (exponential decay)

merge_snow_threshold = 0.01             # (m) minimum height of layer, is used if fresh fallen snow is added as a new
                                        # layer or merged to the underlying layer

minimum_snow_height = 0.01              # (m) minimum height of last snowlayer on glacier
                                        # If there is only one snow layer layer left this one is only merged if the height
                                        # is lower than the minimum_snow_height even is merge_new_snow_threshold is greater

density_fresh_snow = 250.               # density of freshly fallen snow [kg m-3]

albedo_fresh_snow = 0.90                # albedo of fresh snow [-] (Moelg etal. 2012, TC)
albedo_firn = 0.55                      # albedo of firn [-] (Moelg etal. 2012, TC)
albedo_ice = 0.3                        # albedo of ice [-] (Moelg etal. 2012, TC)
albedo_mod_snow_aging = 22              # effect of ageing on snow albedo [days] (Moelg etal. 2012, TC)
albedo_mod_snow_depth = 3               # effect of snow depth on albedo [cm] (Moelg etal. 2012, TC)
roughness_fresh_snow = 0.24             # surface roughness length for fresh snow [mm] (Moelg etal. 2012, TC)
roughness_ice = 1.7                     # surface roughness length for ice [mm] (Moelg etal. 2012, TC)
roughness_firn = 4.0                    # surface roughness length for aged snow [mm] (Moelg etal. 2012, TC)
aging_factor_roughness = 0.0026         # effect of ageing on roughness lenght (hours) 60 days from 0.24 to 4.0 => 0.0026

surface_emission_coeff = 0.97           # surface emision coefficient [-]

snow_ice_threshold = 900.0              # pore close of density [kg m^(-3)]
snow_firn_threshold = 555.0               #
threshold_for_snowheight = 800.0        # density threshold when layer is classified as snow


liquid_water_fraction = 0.05            # irreducible water content of a snow layer;
                                        # fraction of total mass of the layer [%/100]
percolation_velocity = 0.0006           # percolation velocity for unsaturated layers [m s-1] (0.06 cm s-1)
                                        # how does it change with density?
                                        # Martinec, J.: Meltwater percolation through an alpine snowpack, Avalanche
                                        # Formation, Movement and Effects, Proceedings of the Davos Symposium, 162, 1987.


'SOIL CONTENT AND RATIOS'
water_content = 0.18
water_thermal_conductivity = 0.57

mineral_content = 0.4
mineral_thermal_conductivity = 2.9

air_content = 0.42
air_thermal_conductivity = 0.0025

' PHYSICAL CONSTANTS '

lat_heat_melting = 3.34e5               # latent heat for melting [J kg-1]
lat_heat_vaporize = 2.5e6               # latent heat for vaporization [J kg-1]
lat_heat_sublimation = 2.834e6          # latent heat for sublimation [J kg-1]
spec_heat_air = 1004.67                 # specific heat of air [J kg-1 K-1]
spec_heat_ice = 2050.00                 # specific heat of ice [J Kg-1 K-1]
sigma = 5.67e-8                         # Stefan-Bolzmann constant [W m-2 K-4]
gravity_acceleration = 9.81            # acceleration of gravity (Braithwaite 1995) [m s-1]

' SOIL CONSTANTS'
volumetric_heat_soil = 2000000.          # Hillel 2004: Environmental Soil Physics: Fundamentals, Applications, and Environmental Considerations
                                        # page 230

' MODEL CONSTANTS '
water_density = 1000.0                  # density of water [kg m^(-3)]
ice_density = 917.                      # density of ice [kg m^(-3)]
soil_density = 1350.                    # density of ice [kg m^(-3)]

zero_temperature = 273.16               # Kelvin [K]

' Densification constants '
K0   = 11                               # rate factors [-]
K1   = 575
E0   = 10260                            # activation energy
E1   = 21400
R    = 8.3144                           # universal gas constant [J K-1 mol-1]

