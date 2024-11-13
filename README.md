# Cambridge University Estates building energy usage archive (2000-2023)

[![DOI](https://zenodo.org/badge/668225188.svg)](https://zenodo.org/doi/10.5281/zenodo.10708693)

This repository hosts a dataset of historic building energy usage (electricity and gas) from buildings across the Cambridge University Estates covering the period 2000 to 2023. The electricity usage data includes lighting, plug loads, and plant equipment electricity consumption. It is assumed that for the period covered, none of the buildings have heat pumps installed, and so the gas usage data corresponds to the total heating energy usage for the buildings.

An interactive visualisation of the available data can be found at [EECi.github.io/Cambridge-Estates-Building-Energy-Archive/building_data_summary.html](https://EECi.github.io/Cambridge-Estates-Building-Energy-Archive/building_data_summary.html).

Tools are provided for identifying and constructing building energy datasets that are in a format compatible with the CityLearn environment for building energy control simulation. Detail on this formatting can be found in the [CityLearn documentation](https://www.citylearn.net/overview/dataset.html). All predicted variables are perfect predictions copied from the true data measurements.

`DataSources.md` provides details of the source of the data variables within the datasets, and any pre-processing performed.

## Updates for Version 2

Version 2 of this dataset provides two major updates:
  1. Gas usage data is provided for all buildings where it is available.
  2. The dataset is expanded to include more buildings and more years of data. Some buildings from Version 1 are removed.

NOTE: the annonymised building IDs in Version 2 *do not* correspond to the building IDs in Version 1.

## Version 2.1

Solar panel model parameters for Renewables.Ninja API call adjusted to make solar generation data more realistic (defaults from web portal used). Previously solar generation data was overly optimistic with excessively high capacity factors due to use of optimal tracking & tilt option.

## Note on Data Processing

Very lightweight pre-processing is performed on the energy usage data obtained from the Cambridge University Estates building monitoring systems.

There are two key steps:
  1. The data is screened for years with sufficient data availability and visually inspected data quality.
  2. Missing data is replaced with zeros (for compatibility with the CityLearn environment).

Further detail on pre-processing is available in `DataSources.md`.

As a result, the provided data contains substantial real-world 'messiness'. These data quality and availability issues are common in practical building monitoring systems. Hence, this dataset provides opportunity for the study of data quality issues in building energy management. The following studies are suggested:
  - Data missingness/validity detection and data imputation
  - Change-point detection for building/occupant behaviour changes
  - Building control scheme robustness (i.e. stability under unreliable input data)

## Directory Structure

- `building_data`
  - `processed_data`; pre-processed electricity and gas data for each building (csv files for each available year of data)
  - `find_cont_datasets.ipynb`; script of identifying sets of buildings with data available over continuous time periods
  - `summarise_building_data.ipynb`; script for reporting and visualising summary data on building data availability
  - `view_building_data.py`; script for visualising building data time series
  - `viz_data_availability.py`; script for visualising data availability across buildings
- `aux_data`; pre-processed data for weather, solar, electricity pricing, and grid carbon intensity (csv files for each available year of data) + scripts for gathering and processing data
- `DataSources.md`; documentation on the source of the data variables within the datasets, and any pre-processing performed
- `prep_dataset.ipynb`; script for preparing datasets for CityLearn environment
- `resources`; resources for generating datasets
- `datasets`; output directory for generated datasets

## Citation

If you use any data provided in this repository please cite it using the following,

```
@misc{langtry2024CambridgeUniversityEstates,
  author = {Langtry, Max and Choudhary, Ruchi},
  month = may,
  title = {Cambridge University Estates building energy usage archive},
  version = {2.1},
  year = 2024,
  doi = {10.5281/zenodo.10955332},
  url = {https://github.com/EECi/Cambridge-Estates-Building-Energy-Archive},
}
```

## Acknowledgements

We would like to thank the Cambridge University Estates division for their help making this data publicly accessible.
