from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/uncertainties.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=px.scatter(df, x="time", y="depth_uncertainty", color="method_id", hover_name="publicid", log_y=True)),
    dcc.Graph(figure=px.scatter(df, x="time", y="latitude_uncertainty", color="method_id", hover_name="publicid", log_y=True)),
    dcc.Graph(figure=px.scatter(df, x="time", y="longitude_uncertainty", color="method_id", hover_name="publicid", log_y=True)),
    # dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

if __name__ == '__main__':
    app.run(debug=True)
