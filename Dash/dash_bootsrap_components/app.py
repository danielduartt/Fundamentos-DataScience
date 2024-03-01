import dash_bootstrap_components as dbc
from dash import html, dcc, Dash
import dash

app = Dash(external_stylesheets=[dbc.themes.DARKLY])

server = app.server

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div("Column"), style={'background-color': '#ff0000', 'color': 'white', 'padding': '10px'}, md = 6),
        dbc.Col(html.Div("Column"), md = 3 ),
        dbc.Col(html.Div("Column"), md = 3)
    ]),
])

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
