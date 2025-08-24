import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load your dataset (adjust path if needed)
df = pd.read_csv(r"E:\New folder\ML_Projects\EDA_+_Visualization.csv") 
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("📊 Student Mental Health & Lifestyle Dashboard"), width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.histogram(df, x="Diet_Quality", title="Diet Quality")), width=6),
        dbc.Col(dcc.Graph(figure=px.scatter(df, x="Sleep_Hours", y="GPA_numeric", color="Stress_Level", title="Sleep vs GPA")), width=6)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=px.histogram(df, x="Stress_Level", color="Gender", barmode="group", title="Stress by Gender")), width=6),
        dbc.Col(dcc.Graph(figure=px.box(df, x="Exercise_Frequency", y="GPA_numeric", title="Exercise vs GPA")), width=6)
    ]),
])

if __name__ == "__main__":
    app.run(debug=True)
