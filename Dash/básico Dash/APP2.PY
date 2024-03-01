import dash 
from dash import html,dcc 
import plotly.express as px 
import pandas as pd 

#Folha de Estilo

external_style = ["https://codepen.io/chriddyp/pen/bWLwgP"]

app = dash.Dash(__name__, external_stylesheets = external_style)

app.layout = html.Div(
    children= [
        html.H1("Hello Dash", id = "h1", style = {"color": "#FF000"}),
        html.Div(children = html.H2("Teste", id = "Teste"))
        ]
 
)


if __name__ == '__main__':
    app.run_server(debug=True)
