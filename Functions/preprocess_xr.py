import xarray as xr
import regionmask
def preprocess_dataset(file_path):
    """
    This function renames the .nc dimensions and recalculates the Longitude to -180 to 180. 
    It also creates a land-sea mask where the xarray returned is just for land values. 
    """
    ds = xr.open_dataset(file_path)
    ds = ds.rename({'lat': 'Latitude', 'lon': 'Longitude'})
    ds = ds.assign_coords(Longitude=((ds.Longitude + 180) % 360) - 180).sortby(variables=['Longitude', 'Latitude'], ascending=True)

    land_110 = regionmask.defined_regions.natural_earth_v5_0_0.land_110
    land_mask = land_110.mask_3D(ds, lon_name='Longitude', lat_name='Latitude').squeeze(drop=True)

    ds = ds.where(land_mask == 1)
    
    return ds