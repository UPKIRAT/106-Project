import pandas as pd
import plotly.express as px
import numpy as np
import csv

def get_data_source(data_path):
    coffee_cups = []
    sleep  = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_cups.append(float(row['coffee']))
            sleep.append(float(row['sleep']))
        
    return{'x': coffee_cups, 'y': sleep}

def find_corelation(data_source):
    corelation = np.corrcoef(data_source['x'], data_source['y'])
    print(corelation[0,1])

def plotGraph(data_source):
    df = pd.read_csv('cups of coffee vs hours of sleep.csv')
    fig = px.scatter(df, x = 'coffee', y = 'sleep')
    fig.show()

def setup():
    data_path = 'cups of coffee vs hours of sleep.csv'
    data_source = get_data_source(data_path)
    find_corelation(data_source)
    plotGraph(data_source)

setup()
