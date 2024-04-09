"""Visualise availability of metering data for all buildings."""

import os
import re
import numpy as np
import plotly.graph_objects as go

# nice heat map plots showing whether files for each year & building have been created
# can use these to screen out buildings and then manually add into screening during processing

if __name__ == '__main__':
    # get list of building IDs and directories
    data_dir_path = os.path.join('processed_data')
    building_dirs = [f for f in os.listdir(data_dir_path) if os.path.isdir(os.path.join(data_dir_path, f))]
    regex = re.compile(r'\d+')
    building_ids = sorted([int(*regex.findall(f)) for f in building_dirs])

    # find years of available data for each building
    building_years = {
        'elec': {},
        'gas': {}
    }

    for bid in building_ids:

        building_dir = os.path.join(data_dir_path, f'UCam_Building_b{bid}')
        elec_dir = os.path.join(building_dir, 'electricity')
        gas_dir = os.path.join(building_dir, 'gas')

        if os.path.exists(elec_dir):
            year_files = [f for f in os.listdir(elec_dir) if (os.path.isfile(os.path.join(elec_dir, f))) and (f.endswith('.csv'))]
            building_years['elec'][bid] = [int(*regex.findall(f)) for f in year_files]
        else:
            building_years['elec'][bid] = []

        if os.path.exists(gas_dir):
            year_files = [f for f in os.listdir(gas_dir) if (os.path.isfile(os.path.join(gas_dir, f))) and (f.endswith('.csv'))]
            building_years['gas'][bid] = [int(*regex.findall(f)) for f in year_files]
        else:
            building_years['gas'][bid] = []

    # create matrices of data availabilities for plotting
    first_year = min([min(building_years['elec'][bid] + building_years['gas'][bid]) for bid in building_ids])
    last_year = max([max(building_years['elec'][bid] + building_years['gas'][bid]) for bid in building_ids])
    years = list(range(first_year, last_year+1))

    elec_year_matrix = np.array(
        [[1 if y in building_years['elec'][bid] else 0 for y in years] for bid in building_ids],
        dtype=float
    ).T
    gas_year_matrix = np.array(
        [[1 if y in building_years['gas'][bid] else 0 for y in years] for bid in building_ids],
        dtype=float
    ).T
    combined_year_matrix = np.logical_and(elec_year_matrix, gas_year_matrix).astype(float)

    for y in [2020]:
        for n,id in enumerate(building_ids):
            if elec_year_matrix[years.index(y),n] == 1:
                elec_year_matrix[years.index(y),n] = 0.5
            if gas_year_matrix[years.index(y),n] == 1:
                gas_year_matrix[years.index(y),n] = 0.5
            if combined_year_matrix[years.index(y),n] == 1:
                combined_year_matrix[years.index(y),n] = 0.5


    # create heat map plots
    bvals = [0,0.33,0.66,1]
    colors = ['white','gray','black']
    dcolorsc = []
    for k in range(len(colors)):
        dcolorsc.extend([[bvals[k],colors[k]],[bvals[k+1],colors[k]]])
    tickvals = [0.165,0.5,0.835]
    ticktext = ['No','COVID','Yes']

    for type in ['elec','gas','comb']:
        if type == 'elec':
            data_year_matrix = elec_year_matrix
            title_name = 'Electricity'
        elif type == 'gas':
            data_year_matrix = gas_year_matrix
            title_name = 'Gas'
        elif type == 'comb':
            data_year_matrix = combined_year_matrix
            title_name = 'Combined'

        fig = go.Figure(
            data = go.Heatmap(
                z = data_year_matrix,
                x = building_ids,
                y = years,
                hovertemplate =
                    '<i>Building ID</i>: b%{x}'+
                    '<br><i>Year</i>: %{y}<br>'+
                    '<b>Availability</b>: %{z}<extra></extra>',
                colorscale = dcolorsc,
                colorbar = dict(
                    tickvals = tickvals,
                    ticktext = ticktext
                )
            )
        )
        fig.update_layout(
            title = '%s Data Availability'%title_name,
            xaxis_title = 'Building ID',
            yaxis_title = 'Year',
            yaxis = dict(
                tickvals = years
            ),
            xaxis_nticks = len(building_ids)
        )
        fig.show()

        # save plot
        fig.write_html(os.path.join('plots',f'data_availability_{type}.html'))