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
    palette = ["#193D3D","#193E3E","#193e3e","#1e4b4b","#28686a","#2d777a","#318589","#4b9598","#65a4a6","#72acae","#7fb3b5","#8cbbbc","#98c2c3", "#b9d6d6", "#E3EBEB", "#e7eded", "#ebefef", "#f3f3f3", "#F1F2F2", "#ffffff"]
    ax = sns.set(font="Tahoma", style="darkgrid")
    sns.countplot(y='Country',data=df, order=df['Country'].value_counts(ascending=False).index[:20], palette=palette)
    plt.title(label="Number of attacks by country (top 20)", fontsize=18)
    try: 
        ax.bar_label(container=ax.containers[0], labels=df['Country'].value_counts(ascending=False).values)
    except AttributeError:
        pass
    return plt.show()



def histogram (df):
    months = [calendar.month_abbr[i] for i in range(1, 13)]
    df_month = df[df['Month'].isin(months)]
    country_lst = list(df.Country.value_counts()[df.Country.value_counts()>100].index)
    df_month['Country_tag']=[i if i in country_lst else 'OTHER' for i in df_month['Country']]
    months = [i.strftime("%b") for i in pd.to_datetime(df_month['Month'], format='%b').sort_values()]
    
    return sns.histplot(x=months, data=df_month, hue='Country_tag', multiple="stack")

def violin_plot (df):
    ax = sns.set(rc={"figure.figsize": (12.,6.)})
    sns.set(font="Tahoma", style="darkgrid")
    ax = sns.violinplot(x=df.Age, color='lightseagreen')
    ax = ax.axvline(x=df.Age.median(), c="red", label="Median")
    plt.title(label="Distribution of victim's ages ", fontsize=18)
    ax = plt.legend()
    return plt.show()

def lineplot(df):
    df_year = pd.DataFrame(df['Year'].value_counts())
    df_year = df_year[df_year.index>1900]
    ax = sns.set(rc={"figure.figsize": (12.,6.)})
    ax = sns.set(font="Tahoma", style="darkgrid")
    ax = sns.lineplot(data=df_year, x=df_year.index, y=df_year.Year, color='lightseagreen')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count') 
    plt.title(label="Number of attacks per year since 1900", fontsize=18)
    return plt.show()


def treemap_plot(df):
    color = ["#193e3e","#1e4b4b","#28686a","#2d777a","#318589","#4b9598","#65a4a6","#72acae","#7fb3b5","#8cbbbc","#98c2c3", "#b9d6d6"]
    df_activity = pd.DataFrame(df['Activity'].value_counts()[:12]) # TOP 12 BC THREESHOLD OF 50 ATTACKS
    label = df_activity.index.str.strip() + ": "+df_activity.Activity.apply(lambda x: str(x)).str.strip()
    #label = list(df_activity.index)
    sizes = list(df_activity['Activity'])
    squarify.plot(sizes=sizes, label=label, alpha=1, color=color)
    plt.rcParams['text.color'] = 'white'
    plt.yticks(color='w')
    plt.xticks(color='w')
    plt.title(label="Principal activities prone to shark attacks", fontsize=18, color='black')
    return plt.show()


def histogram (df):
    #plt.rcdefaults() 
    months = [calendar.month_abbr[i] for i in range(1, 13)]
    df_month = df[df['Month'].isin(months)]
    country_lst = list(df.Country.value_counts()[df.Country.value_counts()>100].index)
    df_month['Country_tag'] = [i if i in country_lst else 'OTHER' for i in df_month['Country']]
    months = [i.strftime("%b") for i in pd.to_datetime(df_month['Month'], format='%b').sort_values()]
    palette = ["#193e3e","#1e4b4b","#28686a","#2d777a","#318589","#4b9598","#65a4a6","#72acae"]
    sns.histplot(x=months, data=df_month, hue='Country_tag', multiple="stack", palette=palette)
    plt.title(label="Monthly distribution of shark attacks by country", fontsize=18)
    plt.rcParams['text.color'] = 'black'
    return plt.show()