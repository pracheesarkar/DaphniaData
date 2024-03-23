import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import pandas as pd

# suppress R warnings
from rpy2.rinterface_lib.callbacks import logger as rpy2_logger
import logging

rpy2_logger.setLevel(logging.ERROR)
neonUtilities = importr('neonUtilities')


# neonUtilities.stackByTable(filepath='/Users/pracheesarkar/Documents/AlvaradoLab/NEON_site-mgt-and-event-report')
# neonUtilities.stackByTable(filepath='/Users/pracheesarkar/Documents/AlvaradoLab/NEON_depth-profiles')

def get_data(site=False):
    base_url = '/Users/pracheesarkar/Documents/AlvaradoLab/NEON_zooplankton/stackedFiles'
    data = pd.read_csv("./data_sites/dep_profileData.csv")

    # filter data to only show Daphnia
    if site:
        df = pd.DataFrame(data)
        df.to_csv("../data_sites/sites.csv")
    return data


# create modified dataframe for water temp of a given site and year
def site_stats(siteName: str, siteYear: int):
    data = get_data()
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    site_data = df[df.siteID == siteName]
    site_data = site_data[site_data.year == siteYear]
    agg_function = {'month': 'first', 'waterTemp': 'mean'}
    df_count = site_data.groupby(site_data['month']).aggregate(agg_function)
    return df_count


