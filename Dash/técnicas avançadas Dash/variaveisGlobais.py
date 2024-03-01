import pandas as pd 
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

app = Dash(__name__)

df = pd.DataFrame({
    "Student_id": range(1,11), 
    "Score": [1,5,2,5,2,3,1,5,1,5]
})

app.layout = html.Div([
    dcc.Dropdown( id = 'score', options = [{"label": str(i), "value":i} for i in list(range(1,6))],
                 value = '1'),
    html.Button(id='button-1', children ="No Touch Me, Pls"),
    html.Div(id='output-div'),
    dcc.Store(id="store") #vai guardar por sessão guarda as informações personalizadas 
])


@app.callback(
    Output('store', 'data'),
    [Input('score', 'value')]
)
def update_df(score): 
    filt_df = df[df["Score"] == int(score)]
    return filt_df.to_dict()

@app.callback(
    Output("output-div", "children"),
    [State("button-1", 'n_clicks')
     ,Input("store", "data")]
)
def update_output( n_clicks,input_value):
    filt_df = pd.DataFrame(input_value)
    return len(filt_df)


if __name__ == "__main__":
    app.run_server(debug = True)
