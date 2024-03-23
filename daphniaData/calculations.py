import matplotlib.pyplot as plt
import pandas as pd
from sites import site_stats
import numpy as np
import os

desiredFolder = './figures'


class Calculations:

    # calculate and plot abundance of Daphnia per liter per site using formula:
    # sum(adjCountPerBottle[i])/towsTrapsVolume[i], where i = unique sample ID
    @staticmethod
    def site_count(df):
        avg = df.groupby(['sampleID', 'siteID_x', 'year'], as_index=False).apply(
            lambda x: pd.Series({'count': x['adjCountPerBottle'].sum() // x['towsTrapsVolume'].mean()}))

        agg_function = {'siteID_x': 'first', 'count': 'sum'}

        df_count = avg.groupby(['siteID_x']).aggregate(agg_function)
        site = df_count['siteID_x']
        count = df_count['count']
        # print(df_count)

        # plot Daphnia count per site
        fig0 = plt.figure()
        plt.bar(site, count, color='lightblue')
        plt.xlabel("Sites")
        plt.ylabel("Count")
        plt.title("Daphnia Abundance Per Liter (2015 - 2022)")

        plot_path = os.path.join(desiredFolder, "DataPerSite/CountPerSite.png")
        fig0.savefig(plot_path)
        # plt.show()
        plt.close()

    # calculate and plot yearly abundance of Daphnia per liter in a given site
    def yearly_count(site_name:str, df):
        dataSite = df[df.siteID_x == site_name]
        df2 = pd.DataFrame(dataSite)
        avg = df2.groupby(['sampleID', 'siteID_x', 'year'], as_index=False).apply(
            lambda x: pd.Series({'count': x['adjCountPerBottle'].sum() // x['towsTrapsVolume'].mean()}))

        agg_function = {'year': 'first', 'count': 'sum'}

        df_count = avg.groupby(['year']).aggregate(agg_function)
        site = df_count['year']
        count = df_count['count']
        # print(df_count)

        # plot Daphnia count per site
        fig0 = plt.figure()
        plt.bar(site, count, color='lightpink')
        plt.xlabel("Year")
        plt.ylabel("Count")
        plt.title("Daphnia Abundance Per Liter in Site {}".format(site_name))

        plot_path = os.path.join(desiredFolder, "DataPerSite/{} CountPerYear.png".format(site_name))
        fig0.savefig(plot_path)
        # plt.show()
        plt.close()

    # calculate and plot monthly abundance of Daphnia per liter give site and year
    def daphnia_count_yearly(siteName: str, siteYear, df):
        dataSite = df[df.siteID_x == siteName]
        dataSite = dataSite[dataSite.year == siteYear]
        df2 = pd.DataFrame(dataSite)

        if df2.size != 0:
            avg = df2.groupby(['sampleID', 'siteID_x', 'month'], as_index=False).apply(
                lambda x: pd.Series({'count': x['adjCountPerBottle'].sum() // x['towsTrapsVolume'].mean()}))
            # print(avg)
            agg_function = {'month': 'first', 'count': 'sum'}
            df_count = avg.groupby(['month']).aggregate(agg_function)

            fig1, ax = plt.subplots()
            ax2 = ax.twinx()
            ax.bar(df_count['month'], df_count['count'], color='green')
            df_count2 = site_stats(siteName, siteYear)
            ax2.plot(df_count2['month'], df_count2['waterTemp'], color='black', marker="*")
            plt.xlabel("Month")
            ax.set_ylabel("Count")
            ax2.set_ylabel('Temp')
            plt.title("Monthly Daphnia Abundance in " + siteName + "({})".format(siteYear))

            plot_path = os.path.join(desiredFolder, "{}/{} count.png".format(siteName, siteYear))
            fig1.savefig(plot_path)
            # plt.show()
            plt.close()

    # calculate and plot monthly average length of Daphnia per liter give site and year
    def daphnia_size_monthly(siteName: str, siteYear, df):
        dataSite = df[df.siteID_x == siteName]
        dataSite = dataSite[dataSite.year == siteYear]
        df2 = pd.DataFrame(dataSite)

        if df2.size != 0:
            agg_function = {'month': 'first', 'zooMeanLength': 'mean'}
            df_count = df2.groupby(df2['month']).aggregate(agg_function)

            fig1, ax = plt.subplots()
            ax2 = ax.twinx()
            ax.bar(df_count['month'], df_count['zooMeanLength'], color='blue')
            df_count2 = site_stats(siteName, siteYear)
            ax2.plot(df_count2['month'], df_count2['waterTemp'], color='black', marker="*")
            plt.xlabel("Month")
            ax.set_ylabel("Size")
            ax2.set_ylabel('Temp')
            plt.title("Monthly Average Daphnia Size in Site " + siteName + "({})".format(siteYear))

            plot_path = os.path.join(desiredFolder, "{}/{} size.png".format(siteName, siteYear))
            fig1.savefig(plot_path)
            # plt.show()
            plt.close()


