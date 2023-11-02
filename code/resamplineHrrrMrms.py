import xarray as xr
from scipy.interpolate import griddata

# Load HRRR and MRMS data
hrrr_data = xr.open_dataset('hrrr_data.nc')
mrms_data = xr.open_dataset('mrms_data.nc')

# Identify area of overlap
lon_range = slice(max(hrrr_data.longitude.min(), mrms_data.longitude.min()),
                  min(hrrr_data.longitude.max(), mrms_data.longitude.max()))
lat_range = slice(max(hrrr_data.latitude.min(), mrms_data.latitude.min()),
                  min(hrrr_data.latitude.max(), mrms_data.latitude.max()))

# Resample MRMS data to HRRR grid
mrms_data_interp = griddata((mrms_data.latitude.values.ravel(), mrms_data.longitude.values.ravel()),
                            mrms_data.variable.values.ravel(),
                            (hrrr_data.latitude.values[lat_range, lon_range].ravel(),
                             hrrr_data.longitude.values[lat_range, lon_range].ravel()),
                            method='linear').reshape(hrrr_data.latitude[lat_range, lon_range].shape)

# Create combined dataset
combined_data = xr.Dataset({
    'hrrr_variable': hrrr_data.variable[lat_range, lon_range],
    'mrms_variable': (['latitude', 'longitude'], mrms_data_interp)
}, coords={
    'latitude': hrrr_data.latitude[lat_range, lon_range],
    'longitude': hrrr_data.longitude[lat_range, lon_range]
}) 