import dash
from dash import html, dcc, Dash
from dash.dependencies import Input, Output
from data import data
import pandas as pd
import plotly.express as px
# import dash_bootstrap_components as dbc

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

app = Dash(__name__, use_pages=True)


app.layout = html.Div([
     html.H1(children='Energy consumption of site'),
     
     html.Div([
         dcc.Link(page['name']+"   |   ", href=page['path'])
         for page in dash.page_registry.values()         
     ]),
     html.Hr(),

     dash.page_container
])



if __name__ == '__main__':
    app.run_server(debug=True)
