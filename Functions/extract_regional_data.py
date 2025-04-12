def extract_region_data(ds, latitude_range, longitude_range, weights, variable_name, suffix):
    """
    This extracts specific regions from xarray datasets and transforms into Pandas DataFrames for easy manipulation with other csv datasets.
    """
    region_data = ds.sel(Latitude=slice(*latitude_range), Longitude=slice(*longitude_range))[variable_name].weighted(weights).mean(dim=('Latitude', 'Longitude')).to_dataframe().reset_index()
    region_data = region_data.rename(columns={variable_name: f'{suffix}_{variable_name}'})
    return region_data