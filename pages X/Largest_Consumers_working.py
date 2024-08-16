import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

dash.register_page(__name__, name='Largest Consumer')

layout = html.Div([
    html.H1(children='Largest consumers per month'),
    html.Div(id='dropdown1'),
    dcc.Graph(id='max-consumers')

])

#update dropdown
@callback(
        Output('dropdown1', 'value'),
        Input('stored-data', 'data')
)

def add_dropdown(data):
    pd.DataFrame.from_dict(data)
    return dcc.Dropdown(id='month-highest-consumer',
                    options=[{'label' : str(i), 'value' : str(i)}
                            for i in data['Month'].unique()],

                    multi=False,),
#update graph
@callback(
    Output(component_id='max-consumers', component_property='figure'),
    Input(component_id='month-highest-consumer', component_property='value'),
    Input('stored-data', 'data')
 )

def update_graph(selected_month, data):
    pd.DataFrame.from_dict(data)
    df_2_1 = data
    consumer_no = 61
    for i in range(12):
        if df_2_1.loc[i]['Month'] == f'{selected_month}':
            month_data = df_2_1.loc[i]
            length = month_data.count()

            if month_data.iloc[-1] == 0:
                filtered_month_data = month_data[(length - (2*consumer_no)):(length - consumer_no)]
            else:
                filtered_month_data = month_data[(length - consumer_no):length]
            
            df_2_2 = pd.DataFrame([filtered_month_data])
            df_2_2 = df_2_2.T
            df_2_2 = df_2_2.rename(columns={df_2_2.columns[0]: 'Consumption'})
            sorted_df = df_2_2.sort_values(by='Consumption', ascending=False)

            line_fig = px.bar(sorted_df, x= sorted_df.index, y= 'Consumption', title=f'Energy Consumption in {selected_month}')
            break

    return line_fig