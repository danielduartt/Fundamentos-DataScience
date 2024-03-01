import pandas as pd 
import numpy as np 

import plotly.express as px 
import plotly.graph_objects as go

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server 

#========================== Manipulação de Dados ==================
df = pd.read_csv('supermarket_sales.csv')
df["Date"] = pd.to_datetime(df["Date"])

card_Menu = [
    dbc.CardHeader("MENU"),
    dbc.CardBody(html.Div([
            html.H5("Cidades: ", className='test'),
            dcc.Checklist(
                options=[{"label": city, "value": city} for city in df["City"].unique()],
                value=df["City"].unique(),
                id="check-cities",
                inline=True
            ),
            html.H5("Variável de análise: ", style = {"font-size": "20px"}),  # Corrigido o estilo font-size
            dcc.RadioItems(
                options=[
                    {"label": "Faturamento", "value": "gross income"},
                    {"label": "Rating", "value": "Rating"}
                ],
                value="gross income",
                id="radio-options",
                inline=True
            )
        ]))
]

#=============================== Layout ===========================
app.layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Card(card_Menu, color = 'primary', inverse = True, style = {"height": "100vh", "margin-top": "10px","margin-left": "10px"}), sm=4),
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(id='city_fig')),
                dbc.Col(dcc.Graph(id='pay_fig'))
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='income_fig'))
            ])
        ])
    ])
])

#================================= Callbacks ====================================
@app.callback(
    [Output('city_fig', "figure"),
     Output('pay_fig', "figure"),
     Output('income_fig', "figure")],
    [Input("check-cities", "value"),
     Input("radio-options", "value")]
)
def render_graph(check_value, radio_value):
    operation = np.sum if radio_value == "gross income" else np.mean
    df_filt = df[df["City"].isin(check_value)]
    df_city = df_filt.groupby("City")[radio_value].apply(operation).reset_index()
    df_payment = df_filt.groupby("Payment")[radio_value].apply(operation).reset_index()
    df_product = df_filt.groupby(["City", "Product line"])[radio_value].apply(operation).reset_index()
    
    fig_city = px.bar(df_city, x="City", y=radio_value)
    fig_payment = px.bar(df_payment, x=radio_value, y="Payment", orientation="h")
    fig_product = px.bar(df_product, x=radio_value, y="Product line", color="City", orientation="h")
    
    fig_city.update_layout(margin=dict(l=0, r=0, t=20, b=50), height=200, template = 'plotly_dark')
    fig_payment.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=200, template = 'plotly_dark')
    fig_product.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=500, template = 'plotly_dark')
    
    return fig_city, fig_payment, fig_product

#================================= Run_server ========================
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
