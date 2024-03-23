
import matplotlib.pyplot as plt
import pandas as pd
import os
from main import dataDaphnia
from main import desiredFolder

class Daphnia:

    def __init__(self, site):
        dataSite = dataDaphnia[dataDaphnia.siteID_x == site]
        df = pd.DataFrame(dataSite)
        df['collectDate_x'] = pd.to_datetime(df['collectDate_x'])
        df['year'] = df['collectDate_x'].dt.year

    def plotDaphnia(self):
        plt.style.use('seaborn-whitegrid')



    def tally():
        sites = ['BARC', 'CRAM', 'LIRO', 'PRLA', 'PRPO', 'SUGG', 'TOOK']
        # plot Daphnia count and size per year in each site
        for i in range(len(sites)):
            dataSite = dataDaphnia[dataDaphnia.siteID_x == sites[i]]
            df2 = pd.DataFrame(dataSite)
            df2['collectDate_x'] = pd.to_datetime(df2['collectDate_x'])
            df2['year'] = df2['collectDate_x'].dt.year

            # agg_samples = {'sampleID': 'first', 'adjCountPerBottle': 'sum'}
            # total = {'sampleID': 'first', 'towerCountPerBottle': 'sum'}
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
            plt.show
            plt.close()

            fig2 = plt.figure()
            plt.bar(df_size['year'], df_size['zooMeanLength'], color='lightgreen')
            plt.xlabel("Year")
            plt.ylabel("Size")
            plt.ylim(0.00, 2.20)
            plt.title("Daphnia Size Per Year in Site " + sites[i])

            plotpath = os.path.join(desiredFolder, "Size/{}.png".format(sites[i]))
            fig2.savefig(plotpath)
            plt.show
            plt.close()