import dash 
from dash import html, dcc 
from dash.dependencies import Input,Output
import plotly.express as px 


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H2("Altere o valor abaixo para ver o callback em ação!", id = 'h2-principal'),
        html.Div(["ENTRADA:", 
                dcc.Input(value = "", type = 'text', id = 'ipt-1')]),
        html.Br(),
        html.Div(
            id = "my-output"
        )
    ]
)

@app.callback(
    Output(component_id="my-output", component_property="children"),#quem eu quero alterar? e oq 
    [Input(component_id="ipt-1", component_property="value")]
)
def update_layout_div(value):
    return "Saída {}".format(value)



if __name__ == '__main__': 
    app.run_server(debug = True)