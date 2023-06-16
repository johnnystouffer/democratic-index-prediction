# All libraries and data used in the dashboard are imported here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Importing the Index Data
data = pd.read_csv('predictions.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)

# Filtering the data by continents, countries and world 
continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
continent_data = data[data['Entity'].isin(continents)]
continent_data = continent_data[continent_data['Entity'] != 'World']
continent_data.drop('Code', axis=1, inplace=True)

country_data = data[~data['Entity'].isin(continents)]
country_data = country_data[country_data['Entity'] != 'World']

world_data = data[data['Entity'] == 'World']
world_data.drop('Code', axis=1, inplace=True)

# Importing the data for number of each type of government
continent_numbers = pd.read_csv('continent_data.csv')
world_numbers = pd.read_csv('world_data.csv')