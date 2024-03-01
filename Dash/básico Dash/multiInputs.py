import pandas as pd 
import dash 
from dash import html, dcc 
from dash.dependencies import Input, Output
import plotly.express as px 

app = dash.Dash(__name__)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP"]

df = pd.read_csv("country_indicators.csv")
indicador = df["Indicator Name"].unique()

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='dp-esq', 
                     options=[{"label": i, 'value': i} for i in indicador],
                     value="Fertility rate, total (births per woman)"),
        dcc.RadioItems(id='rd-esq',
                       options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                       value="Linear",
                       labelStyle={'display': 'inline-block'}
                       )
    ], id="caixa-esquerda", style={'width': '48%', "display": 'inline-block'}),
    
    html.Div([
        dcc.Dropdown(id='dp-dir', value="Life expectancy at birth, total (years)"),  # Removi as opções do segundo dropdown
        dcc.RadioItems(id='rd-dir',
                       options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                       value="Linear",
                       labelStyle={'display': 'inline-block'}) 
        
    ], id="caixa-direita", style={'width': '48%', "display": 'inline-block', 'float': 'right'}),
    
    html.Div(id='my-output',
             children=[dcc.Graph(id="indicator_graph"),
                       dcc.Slider(id='year-slider',
                                  min=df['Year'].min(),
                                  max=df['Year'].max(),
                                  value=df['Year'].max(),
                                  marks={str(year): str(year) for year in df["Year"].unique()},
                                  step=None)]
             )])

@app.callback(
    Output("indicator_graph", "figure"),
    [Input("dp-dir", 'value'),
     Input("rd-dir", 'value'),
     Input("dp-esq", 'value'),
     Input("rd-esq", 'value'),
     Input("year-slider", 'value')]
)
def graph_update(dp_dir_value, rd_dir_value, dp_esq_value, rd_esq_value, year_value):
    dff = df[df['Year'] == year_value]
    fig = px.scatter(dff, x=dp_esq_value,  # Corrigido aqui
                     y=rd_esq_value,  # Corrigido aqui
                     hover_name=dff['Country Name'],  # Corrigido aqui
                     color='Country Name',
                     title='Indicator Analysis')
    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode='closest', transition_duration=500)
    return fig 

if __name__ == "__main__":
    app.run_server(debug=True)
