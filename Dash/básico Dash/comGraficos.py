import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Carregar os dados
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df = df.rename(columns={"Unnamed: 0": "year"})

# Estilos externos
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP"]

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Definir o layout da aplicação
app.layout = html.Div(
    id="div_principal",
    children=[
        dcc.Graph(id="graph_with_slider"),
        dcc.Checklist(
            id="Select_continent",
            options=[
                {"label": "Asia", "value": "Asia"},
                {"label": "Europe", "value": "Europe"},
                {"label": "Africa", "value": "Africa"},
                {"label": "Americas", "value": "Americas"},
                {"label": "Oceania", "value": "Oceania"}
            ],
            value=['Africa']
        )
    ]
)

# Definir a callback para atualizar o gráfico com base no valor do checklist
@app.callback(
    Output('graph_with_slider', "figure"),
    [Input('Select_continent', 'value')]
)
def update_figure(selected_continent):
    filtered_df = df[df['continent'].isin(selected_continent)]
    fig = px.scatter(filtered_df, x="gdp per capita", y="life expectancy",
                     size="population", color="continent", hover_name="country",
                     log_x=True, size_max=60)
    fig.update_layout(transition_duration=500)
    return fig

# Executar a aplicação
if __name__ == "__main__":
    app.run_server(debug=True)
