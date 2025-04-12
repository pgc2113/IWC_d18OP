import numpy as np
def ueq (ds):
    """
    This calculates the U directio surface wind metrics for the Indian Walker Circulation.
    """
    ds = ds.assign_coords(lon=(((ds.lon+180)%360)-180)).sortby(variables = 'lon',ascending = True)
    
    eraweights = np.cos(np.deg2rad(ds.lat))

    w = ds.sel(lat=slice(-5,5),lon=slice(60,90)).weighted(eraweights).mean(dim=('lat','lon')).groupby('time.month')
    wclim = ds.sel(lat=slice(-5,5),lon=slice(60,90),time=slice('1940','2005')).weighted(eraweights).mean(dim=('lat','lon')).groupby('time.month').mean(dim='time')
    ueqanom = w - wclim
    return ueqanom