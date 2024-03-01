from dash import Dash,html, dcc, callback_context
from dash.dependencies import Input,Output


app = Dash(__name__)



app.layout = html.Div([
    html.Button(id = 'button-1', children = "Button 1"),
    html.Button(id = 'button-2', children = "Button 2"),
    html.Button(id = 'button-3', children = "Button 3"),
    html.Div(id = 'output')
])

@app.callback(
    Output("output", 'children'),
    [Input("button-1", "n_clicks"),
     Input("button-2", "n_clicks"),
     Input("button-3", "n_clicks")]
)
def display(bnt1,bnt2,bnt3):
    id_trigger = callback_context.triggered[0]["prop_id"].split(".")[0]  
    return f"{id_trigger} foi clicado"





if __name__ == '__main__':
    app.run_server(debug = True)