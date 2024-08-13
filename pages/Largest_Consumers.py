import dash
from dash import Dash, dcc, html, dash_table, callback
from dash.dependencies import Input, Output
from data import data
import pandas as pd
import plotly.express as px

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

dash.register_page(__name__, name='Largest Consumer')


layout = html.Div([
    html.Div([
        html.H1(children='Largest consumers per month'),
        dcc.Dropdown(id='month-highest-consumer',
                    options=[{'label' : str(i), 'value' : str(i)}
                            for i in data['Month'].unique()],
                    
                    multi=False),
        
        dcc.Graph(id='max-consumers')
    ])   
])

@callback(
    Output(component_id='max-consumers', component_property='figure'),
    Input(component_id='month-highest-consumer', component_property='value')
 )

def update_graph_2(selected_month):
    df_2_1 = data
    for i in range(12):
        if df_2_1.iloc[i]['Month'] == selected_month:
            if df_2_1.iloc[i][-1] == 0:
                df_2_2 = df_2_1.iloc[i][-122:-61]
            else:
                df_2_2 = df_2_1.iloc[i][-61:0]
        
            pie_chart = px.pie(data_frame=df_2_2)
            return pie_chart