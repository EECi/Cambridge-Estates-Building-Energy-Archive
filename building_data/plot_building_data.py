"""Visualise electricity and gas data for a selected building."""

import os
from tqdm import tqdm
from utils import visualise_building_data


if __name__ == '__main__':

    # iterable of building ids to visualise data
    ids = range(121)
    show = False

    for bid in tqdm(ids):
        fpath = os.path.join('docs','building_plots',f'UCam_Building_b{bid}.html')

        visualise_building_data(bid,fpath,show)