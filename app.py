from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = Dash()

df = pd.read_csv('data/output.csv', parse_dates=['Date'])

fig = px.line(df, x="Date", y="Sales", color="Region", labels= {
        "Date": "Time",
        "Sales": "Sales Amount",
        "Region": "Region"
    }
)

app.layout = html.Div(children=[
    html.H1(children='Sales Amount of Pink Morsels with time'),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    ),

    dcc.RadioItems(
        id='region-options',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Initial selected value
        inline=True
    )
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-options', 'value')
)
def update_region(region):
    if region != 'all':
        filtered_df = df[df.Region == region]
        fig = px.line(filtered_df, x="Date", y="Sales", labels= {
            "Date": "Time",
            "Sales": "Sales Amount",
        })
    else:
        fig = px.line(df, x="Date", y="Sales", labels= {
            "Date": "Time",
            "Sales": "Sales Amount",
        })
    return fig

if __name__ == "__main__":
    app.run(debug=True)







