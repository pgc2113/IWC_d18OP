import hashlib
import urllib.request
import shutil
import os
import glob
from urllib.parse import urlparse
import sys
from platform import python_version
import xarray as xr
import numpy as np
import pandas as pd
import cftime

from dask.diagnostics import ProgressBar
from datetime import datetime
from amount_weighted_ann_mean import amount_weighted_ann_mean
from weighted_temporal_mean import weighted_temporal_mean
from dslp_pwc import dslp_PWC
from extract_regional_data import extract_region_data
from preprocess_xr import preprocess_dataset
from ueq import ueq

pathr = '/Users/pat/Library/CloudStorage/GoogleDrive-pcho@nd.edu/Shared drives/PhD Research/IWC Precipitation Isotopes/01_Scripts/iCESM_iLME_SST/'

outdir = '/Users/pat/Library/CloudStorage/GoogleDrive-pcho@nd.edu/Shared drives/PhD Research/IWC Precipitation Isotopes/03_ProcessedData/'

prefixes = ['b.e11.BLMTRC5CN.f19_g16.001', 
            'b.e11.BLMTRC5CN.f19_g16.002', 
            'b.e11.BLMTRC5CN.f19_g16.003']

for pre in prefixes:
    file_pattern = os.path.join(pathr, f"{pre}.pop.h.SST.*.nc")
    file_list = sorted(glob.glob(file_pattern))

    # Open each file and store them in a list
    ds_list = [xr.open_dataset(file) for file in file_list]

    # Merge the datasets
    with ProgressBar():
        ds = xr.merge(ds_list)

    # Define output file paths
    output_file = os.path.join(outdir, f"{pre}_mon_850_2005.nc")
    output_fileAnn = os.path.join(outdir, f"{pre}_ann_850_2005.nc")
    output_fileond = os.path.join(outdir, f"{pre}_ond_850_2005.nc")

    # Add metadata
    ds.attrs = {'creation_date': str(datetime.now()), 'author': 'Patrick G. Cho'}

    # Resample data
    ds_sstmon = ds.SST
    ds_sstann = ds.SST.resample(time='Y').mean()
    ds_sstond = ds.SST.sel(time=(ds.time.dt.month >= 10) & (ds.time.dt.month <= 12)).resample(time='Y').mean()
    ds_sstond = ds_sstond.groupby('time.month') - ds_sstond.groupby('time.month').mean(dim='time')  # Anomalies
    ds_sstond = ds_sstond.resample(time='Y').mean()

    with ProgressBar():
        ds_sstmon.to_netcdf(output_file)
        ds_sstann.to_netcdf(output_fileAnn)
        ds_sstond.to_netcdf(output_fileond)

    print(f"Saved files for {pre}")