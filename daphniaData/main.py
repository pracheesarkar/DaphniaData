from typing import Any

import rpy2
import rpy2.robjects as robjects
from pandas import Series, DataFrame
from rpy2.robjects.packages import importr
from geojson import MultiPoint, Feature, FeatureCollection, dumps
import matplotlib.pyplot as plt
import pandas as pd
from calculations import Calculations

# suppress R warnings
from rpy2.rinterface_lib.callbacks import logger as rpy2_logger
import logging

base = importr('base')
utils = importr('utils')
stats = importr('stats')

rpy2_logger.setLevel(logging.ERROR)

# utils.install_packages('neonUtilities', repos='https://cran.rstudio.com/')
neonUtilities = importr('neonUtilities')

if __name__ == "__main__":
    # read and merge zoo_taxonomyProcessed.csv and zoo_fieldData.csv
    # edit this base_url variable to the folder where your csv files are.
    # best practice would be to store the files in this repo/folder. just ignore them when we push to git
    def get_data(daphnia=False):
        # base_url = '/mnt/c/Users/nebul/Downloads/NEON_zooplankton 2/NEON_zooplankton/stackedFiles'
        base_url = '/Users/pracheesarkar/Documents/AlvaradoLab/NEON_zooplankton/stackedFiles'
        data = pd.read_csv("./data/zoo_taxonomyProcessed.csv")
        data2 = pd.read_csv("./data/zoo_fieldData.csv")
        data_merged = pd.merge(data, data2, on='sampleID')
        data_daphnia = data_merged[data_merged.subfamily == 'Daphniidae']

        # filter data to only show Daphnia
        if daphnia:
            df = pd.DataFrame(data_daphnia)
            df.to_csv("../data/daphnia.csv")
        return data_daphnia

    # create dataframe with year and month separated for calculations
    data_daphnia = get_data()
    df = pd.DataFrame(data_daphnia)
    df['collectDate_x'] = pd.to_datetime(df['collectDate_x'])
    df['year'] = df['collectDate_x'].dt.year
    df['month'] = df['collectDate_x'].dt.month
    sites = ['BARC', 'CRAM', 'LIRO', 'PRLA', 'PRPO', 'SUGG', 'TOOK']
    years =[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    desiredFolder = './figures'

    Calculations.site_count(df)
    for i in range(len(sites)):
        Calculations.yearly_count(sites[i], df)
        for j in range(len(years)):
            Calculations.daphnia_size_monthly(sites[i], years[j], df)
            Calculations.daphnia_count_yearly(sites[i], years[j], df)





