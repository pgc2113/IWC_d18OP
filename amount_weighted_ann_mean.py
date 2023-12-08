# Amount-Weighted Annual Mean Calculation Function
def amount_weighted_ann_mean (ds, var1, var2):
    """"
    This is for data that is already in monthly resolution following the methodology of Vachon et al., 2007. 
    
    Weights are calculated by monthly precipitation amount.
    
    Amount Weighted Annual Isotope Mean = Sum(Each Month Isotope * Month Precipitation/Total Annual Precipitation)
    
    These will need input of the Isotope variable d18O_P, d2H_P, and Precipitation 
    
    ds : xarray dataset; var1: Precipitation; var2: Precipitation Isotopes
    
    Calculations will be done using Mean Monthly Precipitation of that Year and Total Annual Precipitation of that Year
    
    """
    # Monthly Precipitation 
    ds_monthly = ds[var1].groupby('time.year')
    
    # Calculate Total Annual Precipitation
    ds_ann = ds[var1].groupby('time.year').sum()
    
    # Determine Weighting Factor
    weights = ds_monthly / ds_ann
    
    # Subset our dataset for our variable
    obs = ds[var2]
    
    # Return the Amount-Weighted Annual Mean 
    return (obs * weights).resample(time='Y').sum()