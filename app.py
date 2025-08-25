from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

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
        id='sales_graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)




