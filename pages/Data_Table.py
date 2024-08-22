import dash
from dash import dcc, html, callback, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import base64
import datetime
import io

dash.register_page(__name__, path='/', name='Data')

layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.A('Click here to select CSV file')
        ]),
        multiple=True,
    ),
    dcc.Store(id='stored-data', storage_type='memory'),
    html.Div(id='output-datatable'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), header = 1)
            df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded), header = 1)
            df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
    
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
            
        ])
    
#    dcc.Store(id='stored-data', data=df.to_dict('records')),

    return html.Div([
        html.H5(filename),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=15
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #    'whiteSpace': 'pre-wrap',
        #    'wordBreak': 'break-all'
        #})
    ])

@callback(Output('output-datatable', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children



def parse_data(contents):
    if isinstance(contents, list):
        contents = contents[0]
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), header = 1)
    df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        
    return df
    

@callback(
        Output('stored-data', 'data'),
        Input('upload-data', 'contents'),
        #State('upload-data', 'filename'),
        #State('upload-data', 'last_modified')
)

def store_data(contents):
    if contents is not None:
        df = parse_data(contents)
        return df.to_dict('records')
