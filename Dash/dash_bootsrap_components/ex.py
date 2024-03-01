import dash 
from dash import html 
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

app.layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Card(card_content, color = 'primary', inverse = True, style = {"height": "100vh", "margin-top": "10px",
                                                                                   "margin-left": "10px"}), sm=4),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color = 'primary', inverse = True), md = 6),
                dbc.Col(dbc.Card(card_content, color = 'secondary', inverse = True), md = 6)
            ]),
            dbc.Row([
                dbc.Col(dbc.Card(card_content, color = 'primary', inverse = True), md = 4),
                dbc.Col(dbc.Card(card_content, color = 'success', inverse = True), md = 4),
                dbc.Col(dbc.Card(card_content, color = 'secondary', inverse = True), md = 4)
            ])
        ])
    ])
    
    
    
    
    
])






if __name__ == '__main__':
    app.run_server(debug = True, port = 8050)