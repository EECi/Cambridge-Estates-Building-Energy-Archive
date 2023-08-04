# Cambridge University Estates building electricity usage 2010-2019

This repository hosts a series of datasets of historic building electricity usage from buildings across the Cambridge University Estates, found in the `datasets` directory. These datasets are formatted to be compatiable with the CityLearn [[1]](#1) environment for building energy control simulation. Detail on this formatting can be found in the [CityLearn documentation](https://www.citylearn.net/overview/dataset.html). All predicted variables are perfect predictions copied from the true data measurements.

The following sections provide information on the source of the data variables within the datasets, and any pre-processing performed.

## Building Electrical Demand

Variables: `Equipment Electric Power [kWh]`



The following processing steps are performed on the raw half-hourly metering measurements:
  - duplicate entries removed (first observation only taken)
  - missing or invalid readings replaced with 0 readings
  - measurements clipped to range of 0-10x mean of the unclipped values
  - aggregated to hourly load values
  - rounded to 1 d.p.

## Outdoor Weather Variables

Variables: `Outdoor Drybulb Temperature [C]`, `Relative Humidity [%]` (+ predictions)

## Solar Weather Variables

Variables: `Diffuse Solar Radiation [W/m2]`, `Direct Solar Radiation [W/m2]`, `Solar Generation [W/kW]`

## Electricity Pricing

Variables: `Electricity Pricing [£/kWh]` (+ predictions)

## Grid Carbon intensity

Variables: `kg_CO2/kWh`

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
