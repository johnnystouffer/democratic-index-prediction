from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('final_pivot.csv')
pie = pd.read_csv('world_predictions.csv')
all_data = pd.read_csv('all.csv')
difference = pd.read_csv('difference.csv')

"""

FIRST VISUALIZATION:
CHLOROPLETH MAP

"""

dark_green_scale = [[0, '#002200'], [1, '#009900']]

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

layout_map = go.Layout(
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
)

map_fig = go.Figure(data=traces, layout=layout_map)

map_fig.update_layout(
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    width=1800,
    height=800,
    font=dict(color='white', family='Kalice', size=12),
)
map_fig.update_geos(bgcolor='#222222')

"""

SECOND VISUALIZATION:
BAR CHART

"""

bar_fig = go.Figure(data=go.Bar(
    y=all_data['Change'],
    x=all_data['Country'],
    orientation='v',
    marker=dict(
        color=all_data['Change'],
        colorscale='Greens',
        cmin=all_data['Change'].min(),
        cmax=all_data['Change'].max()
    )
))

bar_fig.update_layout(
    title={
        'text': 'Predicted Change In Fastest Developing and Influential Countries',
        'font': {
            'size': 24,
            'color': 'white',
            'family': 'Kalice',
        },
        'x': 0.5,
        'y': 0.98,
    },
    xaxis_title='Change',
    yaxis_title='Country',
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    width=800,
    height=600,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray', showline=True, linewidth=1, linecolor='black'),
    yaxis=dict(showgrid=False, showline=False, zeroline=False, tickfont=dict(size=12)),
    font=dict(
        color='white',
        family='Kalice',
        size=16
    )
)

bar_fig.update_traces(marker=dict(colorscale=[[0, '#90EE90'], [1, '#006400']]))

"""
LINE PLOT
"""

scatter_trace = go.Scatter(
    x=difference['Year'],
    y=difference['Difference'],
    mode='lines',
    fill='tozeroy',
    line=dict(width=2, color='#009900'),
    marker=dict(size=6, color='white'),
    name='Difference',
    hovertemplate='Year: %{x}<br>Difference: %{y}<extra></extra>'
)

line_fig = go.Figure(data=[scatter_trace])

line_fig.update_layout(
    title={
        'text': 'Difference in Average Index Value Between Years',
        'font': {'size': 20, 'color': 'white', 'family': 'Kalice'},
        'x': 0.5,
        'y': 0.95,
    },
    xaxis_title='Year',
    yaxis_title='Difference',
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    font=dict(color='white', family='Kalice', size=12),
    width=800,
    height=600,
)

"""
STACKED LINE PLOT
"""

stack = pie.melt(id_vars=['Entity', 'Year'], var_name='Type', value_name='Proportion')

stack_fig = go.Figure()

stack = stack.sort_values(by=['Year', 'Type'])
types = stack['Type'].unique()

color_discrete_sequence = ['#228B22', '#008000', '#006400', '#004400']
legend_order = ['Authoritarian', 'Partially Authoritarian', 'Partial Democracy', 'Liberal Democracy']

for i, t in enumerate(legend_order):

    data = stack[stack['Type'] == t]
    stack_fig.add_trace(go.Scatter(
        x=data['Year'],
        y=data['Proportion'],
        mode='lines',
        stackgroup='one',
        line=dict(width=0.5, color=color_discrete_sequence[i]),
        name=t,
        hovertemplate='Type: ' + t + '<br>Year: %{x}<br>Proportion: %{y:.2f}<extra></extra>',
    ))

stack_fig.update_layout(
    title={
        'text': 'Proportion of each Type of Democracy Over Time',
        'font': {
            'size': 30,
            'color': 'white',
            'family': 'Kalice',
        },
        'x': 0.5,
        'y': 0.95,
    },
    xaxis_title='Year',
    yaxis_title='Proportion',
    hovermode='x unified',
    showlegend=True,
    legend=dict(
        x=0,
        y=0,
        bgcolor='#222222',
        traceorder='normal',
        itemsizing='constant',
        itemclick=False,
        title=dict(text='Type'),
    ),
    font=dict(color='white', family='Kalice', size=12),
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    width=800,
    height=600,
)

"""
PIE CHART
"""

years = pie['Year'].unique()

data = []
for year in years:
    year_data = pie[pie['Year'] == year]

    data.append(go.Pie(
        labels=['Authoritarian', 'Partially Authoritarian', 'Partial Democracy', 'Liberal Democracy'],
        values=[year_data['Authoritarian'].values[0], year_data['Partially Authoritarian'].values[0],
                year_data['Partial Democracy'].values[0], year_data['Liberal Democracy'].values[0]],
        name=str(year),
        visible=False,
    ))

data[0]['visible'] = True  # Set the first year as visible

sliders = [{
    'active': 0,
    'currentvalue': {"prefix": "Year: "},
    'pad': {"t": 50},
    'steps': [{'label': str(year), 'method': 'update', 'args': [{'visible': [y == year for y in years]}]}
              for year in years]
}]

layout_pie = go.Layout(
    title={
        'text': 'Proportion of Each Regime Type over the Years',
        'font': {
            'size': 30,
            'color': 'white',
            'family': 'Kalice',
        },
        'x': 0.5,
        'y': 0.95,
    },
    sliders=sliders
)

pie_fig = go.Figure(data=data, layout=layout_pie)
pie_fig.update_layout(
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    width=800,
    height=600,
    font=dict(color='white', family='Kalice', size=12),
)
pie_fig.update_traces(marker=dict(colors=['#003300', '#004400', '#006600', '#008800']))

"""
END OF VISUALS START OF APP
"""

app = Dash(__name__, external_stylesheets=['assets/style.css'])

# Define the layout
app.layout = html.Div(
    className="dashboard",
    children=[
        html.Div(
            className="navbar",
            children=[
                html.Nav(
                    children=[
                        html.H1("Democratic Index: Past and Future Predictions", className="dashboard-title")
                    ]
                )
            ]
        ),
        html.Div(
            className="content",
            children=[
                html.Div(
                    className="graph-container",
                    children=[
                        dcc.Graph(figure=map_fig)
                    ]
                ),
                html.Div(
                    className="subplots-container",
                    children=[
                        html.Div(
                            className="subplot rounded-corners",
                            children=[
                                dcc.Graph(figure=line_fig)
                            ]
                        ),
                        html.Div(
                            className="subplot rounded-corners",
                            children=[
                                dcc.Graph(figure=stack_fig)
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="subplots-container",
                    children=[
                        html.Div(
                            className="subplot rounded-corners",
                            children=[
                                dcc.Graph(figure=pie_fig)
                            ]
                        ),
                        html.Div(
                            className="subplot rounded-corners",
                            children=[
                                dcc.Graph(figure=bar_fig)
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="image-container",
                    children=[
                        html.Img(src="assets/summary.png", style={'width': '70%', 'height': '90%'}, className="image")
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
