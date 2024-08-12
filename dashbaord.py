from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from data import data
import pandas as pd
import plotly.express as px

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

app = Dash()


app.layout = html.Div(children=[
    html.H1(children='Energy Consumption Graphs'),
    dcc.Dropdown(id='consumer-dropdown',
                 options=[{'label' : str(i), 'value' : str(i)}
                          for i in data.columns.unique()],
                 searchable=True,
                 multi=True),
    dcc.Graph(id='consumption-graph')
    
])

@app.callback(
    Output(component_id='consumption-graph', component_property='figure'),
    Input(component_id='consumer-dropdown', component_property='value')
)

def update_graph(selected_consumer):
    line_fig = px.line(data, 
                       x= 'Month', y= selected_consumer,
                       title=f'Energy Consumption of {selected_consumer}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)

