#===================================== BIBLIOTECA ==========================================

import pandas as pd 
import numpy as np 

import plotly.express as px 
import plotly.graph_objects as go

import dash 
from dash import html, dcc
from dash.dependencies import Output, Input

import dash_bootstrap_components as dbc 
from dash_bootstrap_templates import load_figure_template

#======================================= CONFIGS =========================================

load_figure_template('minty')
app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])
server = app.server

#========================================= DATA ==========================================

df = pd.read_csv("supermarket_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

#========================================= CARDS =========================================

card_menu = dbc.Card(
    [
        dbc.CardHeader(html.H2("EMSERH", style={"font-family": "Voltaire", "font-size": "40px"})),
        dbc.CardBody(
            html.Div([
                html.H5("Cidades: ", className='test'),
                dcc.Checklist(
                    options=[{"label": city, "value": city} for city in df["City"].unique()],
                    value=df["City"].unique(),
                    id="check-cities",
                    inline=True,
                    inputStyle={"margin-right": "5px", "margin-left": "20px"}
                ),
                html.H5("Variável de análise: ", style={"font-size": "20px"}),  # Corrigido o estilo font-size
                dcc.RadioItems(
                    options=[
                        {"label": "Faturamento", "value": "gross income"},
                        {"label": "Rating", "value": "Rating"}
                    ],
                    value="gross income",
                    id="radio-options",
                    inline=True
                )
            ])
        )
    ],
    color="primary",
    inverse=True,
    style={"height": '100vh', 'margin': '20px', "padding": "10px"}
)

#========================================= LAYOUT ========================================

app.layout = html.Div([
    dbc.Row([
        dbc.Col(card_menu, sm=2),
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(id='city_fig'), sm=4),
                dbc.Col(dcc.Graph(id='gender'), sm=4),
                dbc.Col(dcc.Graph(id='pay_fig'), sm=4)
            ]),
            dbc.Row([dbc.Col(dcc.Graph(id='income_dates'))]),
            dbc.Row([dbc.Col(dcc.Graph(id='income_fig'))])
        ], sm=10)
    ])
])

#======================================== CALLBACKS ======================================
@app.callback(
    [Output('city_fig', "figure"),
     Output('pay_fig', "figure"),
     Output('income_fig', "figure"),
     Output('gender', "figure"),
     Output('income_dates', "figure")],
    [Input("check-cities", "value"),
     Input("radio-options", "value")]
)
def render_graph(check_value, radio_value):
    operation = np.sum if radio_value == "gross income" else np.mean
    df_filt = df[df["City"].isin(check_value)]
    df_city = df_filt.groupby("City")[radio_value].apply(operation).reset_index()
    df_gender = df_filt.groupby("Gender")[radio_value].apply(operation).reset_index()
    
    df_payment = df_filt.groupby("Payment")[radio_value].apply(operation).reset_index()
    df_product = df_filt.groupby(["City", "Product line"])[radio_value].apply(operation).reset_index()
    df_dates = df_filt.groupby("Date")[radio_value].apply(operation).reset_index()
    
    fig_city = px.bar(df_city, x="City", y=radio_value)
    fig_payment = px.bar(df_payment, x=radio_value, y="Payment", orientation="h")
    fig_product = px.bar(df_product, x=radio_value, y="Product line", color="City", orientation="h")
    fig_gender = px.bar(df_gender, y="Gender", x=radio_value, color="Gender", barmode='group')
    fig_date = px.bar(df_dates, y=radio_value, x='Date')
    
    for fig in [fig_city,fig_payment,fig_product,fig_gender,fig_date]:
        fig.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=300, template = 'minty')
    
    fig_product.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=500, template = 'minty')
    
    return fig_city, fig_payment, fig_product, fig_gender, fig_date

#========================================= RUN SERVER ====================================

if __name__ == '__main__': 
    app.run_server(port=8050, debug = True)
