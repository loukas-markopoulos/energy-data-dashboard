import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
from Data_Table import global_df

dash.register_page(__name__, name='Year Graph')

data = global_df

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