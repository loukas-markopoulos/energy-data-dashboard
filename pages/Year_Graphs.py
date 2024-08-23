import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

dash.register_page(__name__, name='Year Graph')

layout = html.Div([
    html.H1(children='Energy consumption across the whole year'),
    html.Div(id='dropdown2'),
    dcc.Graph(id='consumption-graph'),
    dcc.Store(id='stored-data', storage_type='memory'),
])
#create dropdown
@callback(
        Output('dropdown2', 'children'),
        Input('stored-data', 'data')
)

def add_dropdown(data):
    if data is not None:
        df = pd.DataFrame.from_dict(data)
        options=[{'label' : str(i), 'value' : str(i)}
                                for i in df.columns[1:].unique()],
        options_correct = options[0]
        return html.Div([
            dcc.Dropdown(id='consumer-dropdown',
                        options=options_correct,
                        value=None,
                        searchable=True,
                        clearable=False,
                        multi=True),
        ])

#update graph
@callback(
    Output(component_id='consumption-graph', component_property='figure'),
    Input(component_id='consumer-dropdown', component_property='value'),
    State('stored-data', 'data')
)

def update_graph_1(selected_consumer, data):
    if data is not None:
        df_1 = pd.DataFrame.from_dict(data)
        line_fig = px.bar(df_1, x= 'Month', y= selected_consumer, barmode ='group', title=f'Energy Consumption of {selected_consumer}')
        return line_fig
