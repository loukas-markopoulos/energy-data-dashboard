import dash
from dash import Dash, dcc, html, dash_table, callback
from dash.dependencies import Input, Output
from data import data
import pandas as pd
import plotly.express as px

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

dash.register_page(__name__, path='/', name='Year Graph')

layout = html.Div([
    html.Div([
        html.H1(children='Energy consumption across the whole year'),
        dcc.Dropdown(id='consumer-dropdown',
                    options=[{'label' : str(i), 'value' : str(i)}
                            for i in data.columns[1:].unique()],

                    searchable=True,
                    clearable=False,
                    multi=True),
        dcc.Graph(id='consumption-graph'),
    ]),
   
])

@callback(
    Output(component_id='consumption-graph', component_property='figure'),
    Input(component_id='consumer-dropdown', component_property='value')
)

def update_graph_1(selected_consumer):
    df_1 = data
    line_fig = px.bar(df_1, x= 'Month', y= selected_consumer, barmode ='group', title=f'Energy Consumption of {selected_consumer}')
    return line_fig