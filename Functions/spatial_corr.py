import numpy as np
from scipy.stats import pearsonr
def compute_correlations(data, metrics, index, map):
    """
    This function calculates the spatial correlations between ECHAM5-wiso and WC Metrics
    """
    cor_map = map.precip.isel(time=0) * 0
    cor_map_p = map.precip.isel(time=0) * 0

    for j in np.arange(len(data.Latitude)):
        for i in np.arange(len(data.Longitude)):
            valid_indices = np.isfinite(data.d18O_P.values[:, j, i])

            if np.sum(valid_indices) >= 2:
                correlation, p_value = pearsonr(data.d18O_P.values[:, j, i][valid_indices],metrics[index].values[valid_indices])
                if p_value < 0.05:
                    cor_map.values[j, i] = correlation
                    cor_map_p.values[j, i] = p_value

    return cor_map, cor_map_p