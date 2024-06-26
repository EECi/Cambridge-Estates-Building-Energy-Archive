# Data Source Documentation

This document provides details of the sources of the data variables provided in the generated CityLearn compatible datasets.

## Building Electrical Demand

Variables: `Equipment Electric Power [kWh]`, `Heating Load [kWh]`

Source: Cambridge University Estates building monitoring systems.

Info: Electricity and gas metering data from annonymised buildings across Cambridge University estate. Measurements record the total electrical load (includes lighting, plug loads, and plant equipment electricity consumption) and total gas usage at a given metering point in the building. Data provided at hourly resolution, aggregated from raw half-hourly readings.

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

Source: [renewables.ninja](https://www.renewables.ninja/) [[3]](#3) & [[4]](#4)

Info: Data retrieved from API for location in central Cambridge with default solar panel model parameters. The renewables.ninja data is generated using reanalysis models of global weather and technology models of solar panels. For more information refer to the provided [documentation](https://www.renewables.ninja/about).

## Electricity Pricing

Variables: `Electricity Pricing [£/kWh]` (+ predictions)

Source: [Energy Stats UK](https://energy-stats.uk/) [[5]](#5)

Info: "Energy Stats is [a] hobby website that ... uses the Octopus Energy open API calls to summarise both historical and daily energy tariff data". All available historic data for the Agile Octopus import tariff for the Eastern England region (containing Cambridge) was accessed. Of this, the data for 2019 to 2022 was extended through cyclic repetition to produce the required no. of years of electricity pricing data for each dataset. The Agile Octopus tariff data was used as it is the most readily accessible realtime electricity pricing dataset in the UK, and provides a reasonable estimate of the price a building level energy user would pay for electricity.

## Grid Carbon intensity

Variables: `kg_CO2/kWh`

Source: National Grid ESO Data Portal [[6]](#6)

Info: Data records (estimates of) carbon dioxide emissions of UK electrical grid per kilowatt hour of electricity consumed. Data available at hourly resolution. From source - the data "has seasonal decomposition applied to correct missing or irregular data points", and "is subject to change due to a data cleansing process taking place to provide the most accurate figures".

## Timestamps

Variables: `Timestamp (UTC)`

Info: Timestamp for observations at the given index, in UTC timezone, using `%Y-%m-%d %H:%M:%S` format (see [datetime docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)). Note, observations for all data variables within a dataset are assumed to be taken simultaneously. A single timestamp is provided for all variables, giving the observation time for the measurements at the same index in the observation lists.

<br>

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
