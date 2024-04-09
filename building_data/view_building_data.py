"""Visualise electricity and gas data for a selected building."""

import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def fill_missing_times(df):
    """Fill missing times/observations in a dataframe with NaNs."""

    first_time = df['datetime'].min()
    last_time = df['datetime'].max()
    missing_times = pd.date_range(start=first_time, end=last_time).difference(df['datetime'])
    missings_df = pd.DataFrame(data=missing_times, columns=['datetime'])
    missings_df['equipment load [kWh]'] = None
    df = pd.concat([df, missings_df], ignore_index=True)
    df.sort_values(by='datetime', inplace=True) # sort data

    return df

def visualise_building_data(building_id, fpath='temp.html', show=False):

    building_dir = os.path.join('processed_data', f'UCam_Building_b{building_id}')
    elec_dir = os.path.join(building_dir, 'electricity')
    gas_dir = os.path.join(building_dir, 'gas')

    # gather data for plotting
    elec_csvs = [f for f in os.listdir(elec_dir) if (os.path.isfile(os.path.join(elec_dir, f))) and (f.endswith('.csv'))]
    elec_data = pd.concat([pd.read_csv(os.path.join(elec_dir, f)) for f in elec_csvs], ignore_index=True)
    elec_data['datetime'] = pd.to_datetime(elec_data['datetime'])
    elec_data = fill_missing_times(elec_data)

    if os.path.exists(gas_dir):
        gas_csvs = [f for f in os.listdir(gas_dir) if (os.path.isfile(os.path.join(gas_dir, f))) and (f.endswith('.csv'))]
        gas_data = pd.concat([pd.read_csv(os.path.join(gas_dir, f)) for f in gas_csvs], ignore_index=True)
        gas_data['datetime'] = pd.to_datetime(gas_data['datetime'])
        gas_data = fill_missing_times(gas_data)

    else:
        gas_data = None

    # create plot
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=elec_data['datetime'], y=elec_data['equipment load [kWh]'],
        name='Equipment load',
        connectgaps=False
        ),
        secondary_y=False
    )

    if gas_data is not None:
        fig.add_trace(go.Scatter(
            x=gas_data['datetime'],
            y=gas_data['heating load [kWh]'],
            name='Heating load',
            connectgaps=False
            ),
            secondary_y=True
        )

    fig.update_layout(
        xaxis_title='Datetime',
        xaxis=dict(rangeslider=dict(visible=True)),
        title='UCam Building b%s'%building_id,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            )
        )

    fig.update_yaxes(title_text="Equipment load [kWh]", secondary_y=False)
    fig.update_yaxes(title_text="Heating load [kWh]", secondary_y=True)

    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1d", step="day", stepmode="backward"),
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.update_yaxes(fixedrange=False)

    fig.update_layout(title_x=0.5) # center title

    fig.write_html(fpath)

    if show:
        fig.show()


if __name__ == '__main__':
    import time

    # iterable of building ids to visualise data
    ids = range(121)

    for id in ids:
        time.sleep(1)
        building_id = id
        fpath = 'temp.html'
        show = True

        visualise_building_data(building_id,fpath,show)