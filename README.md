# Cambridge University Estates building electricity usage 2010-2019

This repository hosts a series of datasets of historic building electricity usage from buildings across the Cambridge University Estates covering the period 2010 to 2019 (found in the `datasets` directory). These datasets are formatted to be compatiable with the CityLearn [[1]](#1) environment for building energy control simulation. Detail on this formatting can be found in the [CityLearn documentation](https://www.citylearn.net/overview/dataset.html). All predicted variables are perfect predictions copied from the true data measurements.

The following sections provide information on the source of the data variables within the datasets, and any pre-processing performed.

## Building Electrical Demand

Variables: `Equipment Electric Power [kWh]`

Source: Cambridge University Estates building monitoring systems.

Info: Electrical metering data from annonymised buildings across Cambridge University estate. Measurements record the total electrical load at a given meter-
ing point in the building, which includes lighting, plug loads, and plant equipment electricity consumption. Data provided at hourly resolution, aggregated from raw half-hourly readings.

The following processing steps are performed on the raw half-hourly metering measurements:
  - duplicate entries removed (first observation only taken)
  - missing or invalid readings replaced with 0 readings
  - measurements clipped to range of 0-10x mean of the unclipped values
  - aggregated to hourly load values
  - rounded to 1 d.p.

## Outdoor Weather Variables

Variables: `Outdoor Drybulb Temperature [C]`, `Relative Humidity [%]` (+ predictions)

Source: Met Office MIADS dataset [[2]](#2)

Info: Data taken from Bedford measurement station (closest Met Office location with complete data availability over period). Pre-processed version of dataset used.

## Solar Weather Variables

Variables: `Diffuse Solar Radiation [W/m2]`, `Direct Solar Radiation [W/m2]`, `Solar Generation [W/kW]`

Source: [renewables.ninja](https://www.renewables.ninja/) [[3]](#2) & [[4]](#2)

Info:

## Electricity Pricing

Variables: `Electricity Pricing [£/kWh]` (+ predictions)

Source:

Info:

## Grid Carbon intensity

Variables: `kg_CO2/kWh`

Source:

## Citation

```
@misc{Langtry_Cambridge_University_Estates_2023,
  author = {Langtry, Max and Choudhary, Ruchi},
  month = jul,
  title = {{Cambridge University Estates building electricity usage 2010-2019}},
  version = {1.1},
  year = {2023},
  url = {https://github.com/EECi/Cambridge-Estates-Building-Energy-Archive},
}
```

## References
<a id="1">[1]</a>
José R. Vázquez-Canteli, Jérôme Kämpf, Gregor Henze, and Zoltan Nagy. 2019. CityLearn v1.0: An OpenAI Gym Environment for Demand Response with Deep Reinforcement Learning. In Proceedings of the 6th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys '19). Association for Computing Machinery, New York, NY, USA, 356–357. https://doi.org/10.1145/3360322.3360998

<a id="2">[2]</a>
Met Office. MIDAS Open: UK hourly weather observation data, v202207, NERC EDS Centre for Environmental Data Analysis. https://catalogue.ceda.ac.uk/uuid/6180fb7ed76a442eb1b8f3f152fd08d7, September 2022.

<a id="3">[3]</a>
Stefan Pfenninger and Iain Staffell. Long-term patterns of european pv output using 30 years of validated hourly reanalysis and satellite data. Energy, 114:1251–1265, 2016.

<a id="4">[4]</a>
Iain Staffell and Stefan Pfenninger. Using bias-corrected reanalysis to simulate current and future wind power output. Energy, 114:1224–1239, 2016.

<a id="5">[5]</a>
Energy Stats UK. Historical Pricing Data – Octopus Agile Eastern England. https://energy-stats.uk/download-historical-pricing-data/, July 2023.

<a id="6">[6]</a>
National Grid ESO. Historic Generation Mix Carbon Intensity. https://data.nationalgrideso.com/carbon-intensity1/historic-generation-mix, March 2020.
