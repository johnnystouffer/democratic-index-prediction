from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

df = pd.read_csv('final_pivot.csv')
pie = pd.read_csv('world_predictions.csv')
all_data = pd.read_csv('all.csv')

dark_green_scale = [[0, '#006400'], [1, '#003300']]

traces = []
for year in df.columns[2:]:
    trace = go.Choropleth(
        locations=df['Code'],
        z=df[year],
        text=df['Entity'],
        colorscale=dark_green_scale,
        autocolorscale=False,
        marker_line_color='white',
        marker_line_width=0.5,
        colorbar_title='Index Value',
        name=str(year),
        visible=False,
    )
    traces.append(trace)

traces[0]['visible'] = True

slider_steps = [
    {'label': str(year), 'method': 'update', 'args': [{'visible': [y == year for y in df.columns[2:]]}, {'title': f"Global Democratic Index - {year}"}]}
    for year in df.columns[2:133]
]

layout = go.Layout(
    title={
        'text': 'GLOBAL DEMOCRATIC INDEX',
        'font': {
            'size': 20,
            'color': 'white',
            'family': 'Kalice',
        },
        'x': 0.5,
        'y': 0.95,
    },
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    sliders=[
        {
            'active': 0,
            'currentvalue': {"prefix": "Year: "},
            'pad': {"t": 50},
            'steps': slider_steps
        }
    ],
    width=1000,
    height=600,
)

map = go.Figure(data=traces, layout=layout)

map.update_layout(
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    width=1400,
    height=800,
    font=dict(color='white', family='Kalice', size=12),
)
map.update_geos(bgcolor='#222222')

app = Dash(__name__, external_stylesheets=['assets/style.css', 'assets/kalice-font.css'])

app.layout = html.Div(
    className="dashboard",
    children=[
        dbc.Navbar(
            className="app-bar",
            children=[
                dbc.Container(
                    className="title-box",
                    children=[
                        html.H1("Democratic Index: Past and Future Predictions", className="dashboard-title")
                    ]
                )
            ]
        ),
        html.Div(
            className="content",
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                className="graph-container",
                                children=[
                                    dcc.Graph(figure=map)
                                ]
                            ),
                            width=6
                        ),
                        # Add other visualizations or components in the remaining columns
                    ]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
