import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('predictions.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
continent_data = data[data['Entity'].isin(continents)]
continent_data.drop('Code', axis=1, inplace=True)

country_data = data[~data['Entity'].isin(continents)]
country_data = country_data[country_data['Entity'] != 'World']

world_data = data[data['Entity'] == 'World']
world_data.drop('Code', axis=1, inplace=True)