import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

dash.register_page(__name__, name='Year Graph')

layout = html.Div([
    html.H1(children='Energy consumption across the whole year'),
    html.Div(id='dropdown2'),
    dcc.Graph(id='consumption-graph')

])
#create dropdown
@callback(
        Output('dropdown2', 'value'),
        Input('stored-data', 'data')
)

def add_dropdown(data):
    df = pd.DataFrame(data)
    return html.Div([
        dcc.Dropdown(id='consumer-dropdown',
                    options=[{'label' : str(i), 'value' : str(i)}
                            for i in df.columns[1:].unique()],

                    searchable=True,
                    clearable=False,
                    multi=True),
    ])

#update graph
@callback(
    Output(component_id='consumption-graph', component_property='figure'),
    Input(component_id='consumer-dropdown', component_property='value'),
    Input('stored-data', 'data')
)

def update_graph_1(selected_consumer, data):
    df_1 = pd.DataFrame(data)
    line_fig = px.bar(df_1, x= 'Month', y= selected_consumer, barmode ='group', title=f'Energy Consumption of {selected_consumer}')
    return line_fig