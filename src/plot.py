import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import re
import numpy as np
import squarify 
import calendar

def attacks_country(df):
    df_country = pd.DataFrame(df.Country.value_counts()[:20])
    ax = sns.set(rc={"figure.figsize": (12.,6.)})
    ax = sns.countplot(y='Country',data=df, order=df['Country'].value_counts(ascending=False).index[:20])
    try: 
        ax.bar_label(container=ax.containers[0], labels=df['Country'].value_counts(ascending=False).values)
    except AttributeError:
        pass
    ax = ax.set_title(label='Number of attacks by country (top 20)')
    
    return ax


def histogram (df):
    months = [calendar.month_abbr[i] for i in range(1, 13)]
    df_month = df[df['Month'].isin(months)]
    country_lst = list(df.Country.value_counts()[df.Country.value_counts()>100].index)
    df_month['Country_tag']=[i if i in country_lst else 'OTHER' for i in df_month['Country']]
    months = [i.strftime("%b") for i in pd.to_datetime(df_month['Month'], format='%b').sort_values()]
    
    return sns.histplot(x=months, data=df_month, hue='Country_tag', multiple="stack")

def violin_plot (df):
    violin = sns.violinplot(x=df.Age)
    violin = violin.axvline(x=df.Age.median(), c="red", label="median")
    return plt.legend()

def lineplot(df):
    df_year = pd.DataFrame(df['Year'].value_counts())
    df_year = df_year[df_year.index>1900]
    ax = sns.set(rc={"figure.figsize": (12.,6.)})
    ax = sns.lineplot(data=df_year, x=df_year.index, y=df_year.Year)
    ax.set_title(label='Number of attacks per year since 1800')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count') 
    return ax