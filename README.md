# IWC-δ¹⁸Oₚ Analysis
These series of notebooks provide foundational code to recreate the main six figures and analyses in "Influence of the Indian Walker Circulation on δ¹⁸Oₚ and precipitation variability in the Indian Ocean Basin".
## Repository Structure
### Conda Environment and Directories
The provided IWC_Isotopes.yml file will set up the necessary conda environment to execute the series of python notebooks. "Scripts" directory has all the foundational python notebooks to recreate the main figures of the manuscript. Some of these scripts use custom functions that I created which can all be found within the "Functions" directory. All data used for this study can be found via the citations in the references. 
## Analyses and Figures
### Indian Ocean Basin Map
This code establishes the foundation for the Indian Ocean Basin maps used in generating Figure 1. The resulting output was imported into Affinity Designer to craft schematics illustrating the Indian Walker Circulation. 
### Grid-Cell Wise Analysis
This notebook can be used to recreate Figure 2 of the manuscript. 
### Non-Stationary Analysis
The non-stationary analysis involves exploring the role of Pacific and Indian SSTs. This notebook can be used to recreate this figures. The differences between figures 3/5 and 6 is just the data used. 
### Coherence Analysis
The coherence analysis portion of the research product includes a notebook that create the foundational figures (i.e Figure 4) for the results of the Coherence analysis using ECHAM5-wiso and iCESM-iLME. 
One thing to note is that the Weighted-Wavelet Z-Transform can be quite computationally intensive. 
### References
Copernicus Climate Change Service. (2023). Complete ERA5 global atmospheric reanalyis [dataset]. ECMWF. https://doi.org/10.24381/CDS.143582CF

Otto-Bliesner, B. L., Brady, E. C., Fasullo, J., Jahn, A., Landrum, L., Stevenson, S., Rosenbloom, N., Mai, A., & Strand, G. (2016). Climate Variability and Change since 850 CE: An Ensemble Approach with the Community Earth System Model. Bulletin of the American Meteorological Society, 97(5), 735–754. https://doi.org/10.1175/BAMS-D-14-00233.1

Prediction, H. C. F. C. (2000). Met Office Hadley Centre Mean Sea Level Pressure Dataset (p. 34.291 Mbytes) [Proprietary ASCII]. UCAR/NCAR - Research Data Archive. https://doi.org/10.5065/DTT6-BX64

Rayner, N. A., Parker, D. E., Horton, E. B., Folland, C. K., Alexander, L. V., Rowell, D. P., Kent, E. C., & Kaplan, A. (2003). Global analyses of sea surface temperature, sea ice, and night marine air temperature since the late nineteenth century. Journal of Geophysical Research: Atmospheres, 108(D14), 2002JD002670. https://doi.org/10.1029/2002JD002670

Saji, N., & Yamagata, T. (2003). Possible impacts of Indian Ocean dipole mode events on global climate. Climate Research, 25(2), 151–169. https://doi.org/10.3354/cr025151

Werner, M., Langebroek, P. M., Carlsen, T., Herold, M., & Lohmann, G. (2011). Stable water isotopes in the ECHAM5 general circulation model: Toward high-resolution isotope modeling on a global scale. Journal of Geophysical Research: Atmospheres, 116(D15). https://doi.org/10.1029/2011JD015681

[![DOI](https://zenodo.org/badge/728345352.svg)](https://zenodo.org/doi/10.5281/zenodo.10293603)


