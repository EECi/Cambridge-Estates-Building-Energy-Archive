# Cambridge University Estates building energy usage archive (2000-2023)

This repository hosts a dataset of historic building energy usage (electricity and gas) from buildings across the Cambridge University Estates covering the period 2000 to 2023. ... more info ...

... tool provided for creating datasets ... that are in a format compatible with the CityLearn [[1]](#1) environment for building energy control simulation. Detail on this formatting can be found in the [CityLearn documentation](https://www.citylearn.net/overview/dataset.html). All predicted variables are perfect predictions copied from the true data measurements.

... `DataSources.md` ... provides information on the source of the data variables within the datasets, and any pre-processing performed.

## Updates for Version 2

...

## Note on Data Processing

... pre-processing and screening very light, lots of messiness remaining in data, suggest good pickings for data quality research (imputation, change-point detection, etc.) ...

## Directory Structure

- `building_data`
  - `processed_data`; pre-processed electricity and gas data for each building (csv files for each available year of data)
  - `find_cont_datasets.ipynb`; script of identifying sets of buildings with data available over continuous time periods
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
  month = apr,
  title = {Cambridge University Estates building energy usage archive},
  version = {2.0},
  year = 2024,
  doi = {10.5281/zenodo.10708694},
  url = {https://github.com/EECi/Cambridge-Estates-Building-Energy-Archive},
}
```

## Acknowledgements

We would like to thank the Cambridge University Estates division for their help making this data publicly accessible.
