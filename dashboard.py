import dash
from dash import html, dcc, Dash, callback



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
