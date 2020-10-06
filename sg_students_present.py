import pandas as pd
import plotly.express as px
import numpy as np
import csv

def get_data_source(data_path):
    marks = []
    days_present  = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['marks']))
            days_present.append(float(row['days_present']))
        
    return{'x': marks, 'y': days_present}

def find_corelation(data_source):
    corelation = np.corrcoef(data_source['x'], data_source['y'])
    print(corelation[0,1])

def plotGraph(data_source):
    df = pd.read_csv('Student Marks vs Days Present.csv')
    fig = px.scatter(df, x = 'marks', y = 'days_present')
    fig.show()

def setup():
    data_path = 'Student Marks vs Days Present.csv'
    data_source = get_data_source(data_path)
    find_corelation(data_source)
    plotGraph(data_source)

setup()
