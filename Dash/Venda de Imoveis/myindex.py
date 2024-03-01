import pandas as pd 

import plotly.express as px 

import dash 
from dash import html,dcc
from dash.dependencies import Output, Input

import dash_bootstrap_components as dbc 
from dash_bootstrap_templates import load_figure_template
 
from app import *
from components import sidebar


content = html.Div(id = 'page_content')

app.layout = dbc.Container(children = [
    dbc.Row([
        dbc.Col(dbc.location(id = 'url')),
        dbc.Col([
            dbc.Row(),
            dbc.Row(), 
            dbc.Row() 
                ])
            ])
])













