import numpy as np
def dslp_PWC (ds):
    """
    This function Calculates the Sea Level Pressure Gradient for the Pacific Walker Circulation. 
    """
    # Clean Longitude
    ds = ds.assign_coords(lon=(((ds.lon+180)%360)-180))

    ds = ds.sortby(variables='lon',ascending=True)
    
    # Create Weights
    weights = np.cos(np.deg2rad(ds.lat))
    
    # Calculate Western Pacific Anomalies
    wslpP = ds.sel(lat=slice(-5,5),lon=slice(80,160)).weighted(weights).mean(dim=('lat','lon')).groupby('time.month')
    wslpclimP = ds.sel(lat=slice(-5,5),lon=slice(80,160),time=slice('1940','2005')).weighted(weights).mean(dim=('lat','lon')).groupby('time.month').mean(dim='time')
    wslpanomP = wslpP-wslpclimP
    
    # Calculate Eastern Pacific Anomalies; -160 to -80 E is the same as 160-80W
    eslpP = ds.sel(lat=slice(-5,5),lon=slice(-160,-80)).weighted(weights).mean(dim=('lat','lon')).groupby('time.month')
    eslpclimP = ds.sel(lat=slice(-5,5),lon=slice(-160,-80),time=slice('1940','2005')).weighted(weights).mean(dim=('lat','lon')).groupby('time.month').mean(dim='time') 
    eslpanomP = eslpP-eslpclimP
    
    # Calculate dSLP_PWC
    dslpP = eslpanomP - wslpanomP
    return dslpP