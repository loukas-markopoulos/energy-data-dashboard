
def parse_data(contents, filename):
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
    return df.to_dicts("records")



def parse_data(contents, list_of_names, list_of_dates):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)

    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), header=1)
    df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
    data = df.to_json(orient='split')

    return data