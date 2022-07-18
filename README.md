<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Shark Attacks Data Cleaning
*Peter Berna Williams*

*[Data Analytics FT, Barcelona & July 2022]*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The aim of this project was to apply various data cleaning and wrangling techniques in order to turn a quite analysis-unfriendly dataset into a workable one. Then, different visualization methods enabled an Exploratory Data Analysis. 

## Hypotheses
Pretending to be a consultant for a water adventure company, I drew out the following hypotheses: 
1. The most attacks occur in Australia and USA.
2. Attacks have been deacreasing in the last decades.
3. Attacks tend to happen while the victims were surfing, swimming and generally during unsupervised activites.
4. Attacks are more common in summer, given that more activities are conducted at sea.

## Dataset
The 'Global Shark Attacks' dataset (DataFrame below) was retrieved from Kaggle and includes a wide arrange of informations regarding shark attacks, with the earliest registers dating from BC and the last from June 2018. The dataset is composed by 25723 rows and 24 columns and had a mark of 5.88 out of 10 on Kaggle, meaning that it required a thourough data cleaning process to transform into a more practical dataset.

## Workflow
- The first task was to get rid of columns which lacked insighful information (i.e. 'pdf', 'href' ...) as well as empty rows (only NaNs) which were about 19.000. 
- Then RegEx was used to find patterns in columns where elements did not have the same format ('Date', 'Age'...)
- Some replacement where done when necessary to fill NaNs and group elements. 
- After cleaning the dataset, a series of 5 plots where made to visualize the data relevant to test the hypotheses.
- Finally, some conclusions and recommendations

## How to run the various files
    - Import dataset from 'Input' directory
    - import functions from claning.py and plot.py
    - You can view the plots as a file in the 'Images' directory 

## Links
[Repository](https://github.com/Peter-Berna/shark-attacks-data-cleaning)  
[Dataset](https://www.kaggle.com/datasets/teajay/global-shark-attacks?resource=download)  
[Presentation](https://docs.google.com/presentation/d/12VcBD9KBDXUFwCYwdO_X_LFq9WiiRH9xSjg4mIzZblM/edit?usp=sharing)
