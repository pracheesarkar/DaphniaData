import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from geojson import MultiPoint, Feature, FeatureCollection, dumps
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

base = importr('base')
utils = importr('utils')
stats = importr('stats')

# suppress R warnings
from rpy2.rinterface_lib.callbacks import logger as rpy2_logger
import logging

rpy2_logger.setLevel(logging.ERROR)

# utils.install_packages('neonUtilities', repos='https://cran.rstudio.com/')
neonUtilities = importr('neonUtilities')

# read and merge zoo_taxonomyProcessed.csv and zoo_fieldData.csv
# edit this base_url variable to the folder where your csv files are. 
# best practice would be to store the files in this repo/folder. just ignore them when we push to git
def get_data(daphnia=False):
    # base_url = '/mnt/c/Users/nebul/Downloads/NEON_zooplankton 2/NEON_zooplankton/stackedFiles'
    data = pd.read_csv("./data/zoo_taxonomyProcessed.csv")
    data2 = pd.read_csv("./data/zoo_fieldData.csv")
    dataMerged = pd.merge(data, data2, on='sampleID')
    dataDaphnia = dataMerged[dataMerged.subfamily == 'Daphniidae']

    # filter data to only show Daphnia
    if daphnia:
        df = pd.DataFrame(dataDaphnia)
        df.to_csv("../data/daphnia.csv")
    return dataMerged, dataDaphnia
# count total Daphnia collected in a site

#TODO: refactor this code into modules/functions

agg_functions = {'siteID_x': 'first', 'adjCountPerBottle': 'sum', }
df, dataDaphnia = get_data()

df_count = df.groupby(df['siteID_x']).aggregate(agg_functions)

sites = ['BARC', 'CRAM', 'LIRO', 'PRLA', 'PRPO', 'SUGG', 'TOOK']
site = df_count['siteID_x']
count = df_count['adjCountPerBottle']

desiredFolder = './figures'

# plot Daphnia count per site
fig0 = plt.figure()
plt.bar(site, count, color='lightblue')
plt.xlabel("Sites")
plt.ylabel("Count")
plt.title("Daphnia Count Per Site ")

plotpath = os.path.join(desiredFolder, "DataPerSite/CountPerSite.png")
fig0.savefig(plotpath)
plt.close()

# plot Daphnia count and size per year in each site
for i in range(len(sites)):
    dataSite = dataDaphnia[dataDaphnia.siteID_x == sites[i]]
    df2 = pd.DataFrame(dataSite)
    df2['collectDate_x'] = pd.to_datetime(df2['collectDate_x'])
    df2['year'] = df2['collectDate_x'].dt.year

    #agg_samples = {'sampleID': 'first', 'adjCountPerBottle': 'sum'}
    #total = {'sampleID': 'first', 'towerCountPerBottle': 'sum'}
    agg_function = {'year': 'first', 'adjCountPerBottle': 'sum'}
    agg_function2 = {'year': 'first', 'zooMeanLength': 'mean'}
    df_count = df2.groupby(df2['year']).aggregate(agg_function)
    df_size = df2.groupby(df2['year']).aggregate(agg_function2)

    fig1 = plt.figure()
    plt.bar(df_count['year'], df_count['adjCountPerBottle'], color='blue')
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.title("Daphnia Count Per Year in Site " + sites[i])

    plotpath = os.path.join(desiredFolder, "Count/{}.png".format(sites[i]))
    fig1.savefig(plotpath)
    plt.close()

    fig2 = plt.figure()
    plt.bar(df_size['year'], df_size['zooMeanLength'], color='lightgreen')
    plt.xlabel("Year")
    plt.ylabel("Size")
    plt.ylim(0.00, 2.20)
    plt.title("Daphnia Size Per Year in Site " + sites[i])

    plotpath = os.path.join(desiredFolder, "Size/{}.png".format(sites[i]))
    fig2.savefig(plotpath)
    plt.close()
