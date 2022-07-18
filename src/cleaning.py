import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import re
import numpy as np
import squarify 

# General function to delete columns and clean NaN's
def drop_cols_nans (lst, df):
#Delete a list of useless cols
    df = df.drop(lst, axis=1)

#Check rows filled with NaN's and delete them
    df = df[~df.isna().all(1)] 

    return df


# Cleaning function specific to Shark Attacks dataset

def clean_shark(df):
#Change all elements in 'Country' into uppercase
    df['Country'] = df['Country'].str.upper()
    
    #Matching a pattern in the date column to create a new 'month' column
    df["Month"] = df.Date.apply(lambda x: "".join(re.findall(r"[A-Za-z]{3}-",x)).replace("-",""))
    
    #Strip the right space from the name of the column 'Sex' and its values
    df['Sex'] = df['Sex '].str.rstrip()
    df = df.drop("Sex ", axis=1)
    
    # looking for elements with two digits in 'Age' (RegEx)
    df['Age'] = df['Age'].dropna().apply(lambda x: re.findall(r"\d{2}",x))  
    df['Age'] = df['Age'].str[0] # Dropping extra values in Age (sometimes more than one in one row
    df['Age'] = df['Age'].astype(float) #Convert all values into floats so we can later operate with them
    
    # 'Fatal (Y/N)' strip spaces left and right, convert all into uppercase, change column name to 'Fatal' and drop 'Fatal (Y/N)'
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].str.rstrip().str.lstrip().str.upper()
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].replace({'M': 'UNKNOWN','2017':'UNKNOWN'}).fillna("UNKNOWN") #dealing with NaNs    
    df['Fatal'] = df['Fatal (Y/N)']
    df = df.drop("Fatal (Y/N)", axis=1)
    
    return df

## original function with the whole thing

def clean_df(df):
    '''
    This function takes a DataFrame as input and applies some cleaning techniques to return a clean DataFrame
    Arg: 1 df
    Returns: ..
    '''
    #Delete useless cols
    columns_to_delete = ["Case Number", "pdf", "href formula", "href", "Case Number.1", "Case Number.2", "original order", "Unnamed: 22", "Unnamed: 23"]
    df = df.drop(columns_to_delete, axis=1)
    
    #Check rows filled with NaN's and delete them
    df = df[~df.isna().all(1)] 
    
    #Change all elements in 'Country' into uppercase
    df['Country'] = df['Country'].str.upper()
    
    #Matching a pattern in the date column to create a new 'month' column
    df["Month"] = df.Date.apply(lambda x: "".join(re.findall(r"[A-Za-z]{3}-",x)).replace("-",""))
    
    #Strip the right space from the name of the column 'Sex' and its values
    df['Sex'] = df['Sex '].str.rstrip()
    df = df.drop("Sex ", axis=1)
    
    # looking for elements with two digits in 'Age' (RegEx)
    df['Age'] = df['Age'].dropna().apply(lambda x: re.findall(r"\d{2}",x))  
    df['Age'] = df['Age'].str[0] # Dropping extra values in Age (sometimes more than one in one row
    df['Age'] = df['Age'].astype(float) #Convert all values into floats so we can later operate with them
    
    # 'Fatal (Y/N)' strip spaces left and right, convert all into uppercase, change column name to 'Fatal' and drop 'Fatal (Y/N)'
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].str.rstrip().str.lstrip().str.upper()
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].replace({'M': 'UNKNOWN','2017':'UNKNOWN'}).fillna("UNKNOWN") #dealing with NaNs    
    df['Fatal'] = df['Fatal (Y/N)']
    df = df.drop("Fatal (Y/N)", axis=1)
    
    return df