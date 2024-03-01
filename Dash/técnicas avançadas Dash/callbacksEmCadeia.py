from dash import Dash,html, dcc
from dash.dependencies import Input,Output,State

app = Dash(__name__)
all_options = {
    "USA": ["New York", "San Francisco", "Detroit"], 
    "Canada": ["Montreal", "Toronto", "Ottawa"]
}


app.layout = html.Div(
    [
     dcc.RadioItems(id='rd-countrys', 
                    options = [{'label': i, 'value': i} for i in ["USA", "Canada"]],
                    value = "USA"),
     html.Hr(),
     dcc.RadioItems(id="rd-citys"),
     html.Hr(),
     html.Div(id = 'my-output')
    ]
)

@app.callback(
    Output("rd-citys", "options"), 
    [Input("rd-countrys", 'value')]
)
def update_citys(rd_countrys_value):
    return [{"label": i, "value": i} for i in all_options[rd_countrys_value]]


@app.callback(
    Output('rd-citys', "value"),
    [Input('rd-citys', 'options')]
)
def update_value_from_cities(rd_citys_value, ): 
    return rd_citys_value[0]['value']

@app.callback(
    Output("my-output", 'children'), 
    [Input("rd-countrys", "value"),
     Input("rd-citys", "value")]
)
def update_output(value_country, city_value):
    return f"{value_country}------------{city_value}"







if __name__ == '__main__':
    app.run_server(debug = True)