import pandas as pd 
import dash 
from dash import dcc,html 
import plotly.express as px 


app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
    #------------------------------------------------------------------
        html.H1("Dropdown"), 
        dcc.Dropdown(
            id = "dp-1",
            options=[{"label": "Rio Grande do Sul", "value": "RS"},
                     {"label": "São Paulo", "value": "SP"},
                     {"label": "Rio de Janeiro", "value": "RJ"}],
                value = 'RS', #Valor settado 
                style = {"margin-bottom": '50px'}
        ),
    #-------------------------------------------------------------------
        html.Label("Checklist"), 
        dcc.Checklist(
             id = "cl-1",
            options=[{"label": "Rio Grande do Sul", "value": "RS"},
                     {"label": "São Paulo", "value": "SP"},
                     {"label": "Rio de Janeiro", "value": "RJ"}],
            value = ["RS"],#valor settado 
            style = {"margin-top": '25px'}
        ),
    #-------------------------------------------------------------------
    
        html.Label("Text Input"), 
        dcc.Input(value = "Teste",#o que aparece dentro do input 
                  type = "text"), 
        
    #-------------------------------------------------------------------
        html.Label("Slider"),
        dcc.Slider(min = 0,
                   max = 9,
                   marks = {i : "Label {}".format(i) if i == 1 else str(i) for i in range(1,6)},
                   value = 5)#valor original
    ]
)




if __name__ == '__main__':
    app.run_server(debug = True)