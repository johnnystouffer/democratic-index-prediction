from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objects as go

# Load Data
df = pd.read_csv('fixed_data/final_pivot.csv')
pie = pd.read_csv('fixed_data/world_predictions.csv')
all_data = pd.read_csv('fixed_data/all.csv')
difference = pd.read_csv('fixed_data/difference.csv')

# Initialize Dash App
app = Dash(__name__, external_stylesheets=['assets/style.css'])
server = app.server

"""
CHOROPLETH MAP
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
    {
        'label': str(year),
        'method': 'update',
        'args': [{'visible': [y == year for y in df.columns[2:]]}, {'title': f"Global Democratic Index - {year}"}]
    }
    for year in df.columns[2:133]
]

map_fig = go.Figure(data=traces)
map_fig.update_layout(
    title='Global Democratic Index',
    geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'),
    sliders=[{'active': 0, 'currentvalue': {'prefix': 'Year: '}, 'pad': {'t': 50}, 'steps': slider_steps}],
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    font=dict(color='white', family='Verdana', size=12),
    margin=dict(l=20, r=20, t=50, b=20)
)
map_fig.update_geos(bgcolor='#222222')

"""
BAR CHART
"""

bar_fig = go.Figure(data=go.Bar(
    y=all_data['Change'],
    x=all_data['Country'],
    marker=dict(color=all_data['Change'], colorscale='Greens', cmin=all_data['Change'].min(), cmax=all_data['Change'].max())
))

bar_fig.update_layout(
    title='Predicted Change In Fastest Developing and Influential Countries',
    xaxis_title='Country',
    yaxis_title='Change In Index from 2030-2022',
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    font=dict(color='white', family='Verdana', size=12),
    margin=dict(l=20, r=20, t=70, b=20),
    height=400
)

"""
LINE PLOT
"""

line_fig = go.Figure(data=go.Scatter(
    x=difference['Year'],
    y=difference['Difference'],
    mode='lines',
    fill='tozeroy',
    line=dict(width=2, color='#009900')
))

line_fig.update_layout(
    title='Difference in Average Index Value Between Years',
    xaxis_title='Year',
    yaxis_title='Difference',
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    font=dict(color='white', family='Verdana', size=12),
    margin=dict(l=20, r=20, t=70, b=20),
    height=400
)

"""
STACKED LINE PLOT
"""

stack = pie.melt(id_vars=['Entity', 'Year'], var_name='Type', value_name='Proportion')
stack = stack.sort_values(by=['Year', 'Type'])

stack_fig = go.Figure()
legend_order = ['Authoritarian', 'Partially Authoritarian', 'Partial Democracy', 'Liberal Democracy']
colors = ['#228B22', '#008000', '#006400', '#004400']

for i, t in enumerate(legend_order):
    data = stack[stack['Type'] == t]
    stack_fig.add_trace(go.Scatter(
        x=data['Year'],
        y=data['Proportion'],
        mode='lines',
        stackgroup='one',
        line=dict(width=0.5, color=colors[i]),
        name=t
    ))

stack_fig.update_layout(
    title='Proportion of each Type of Democracy Over Time',
    xaxis_title='Year',
    yaxis_title='Proportion',
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    font=dict(color='white', family='Verdana', size=12),
    margin=dict(l=20, r=20, t=70, b=20),
    height=400
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
        marker=dict(colors=['#003300', '#004400', '#006600', '#008800'])
    ))

data[0]['visible'] = True

pie_fig = go.Figure(data=data)
pie_fig.update_layout(
    title='Proportion of Each Regime Type over the Years',
    plot_bgcolor='#222222',
    paper_bgcolor='#222222',
    font=dict(color='white', family='Verdana', size=12),
    margin=dict(l=20, r=20, t=70, b=20),
    height=400,
    sliders=[{
        'active': 0,
        'currentvalue': {'prefix': 'Year: '},
        'pad': {'t': 50},
        'steps': [{'label': str(year), 'method': 'update', 'args': [{'visible': [y == year for y in years]}]} for year in years]
    }]
)

"""
APP LAYOUT
"""

app.layout = html.Div(
    className="dashboard",
    children=[
        html.Div(className="navbar", children=[html.Nav(html.H1("DEMOCRATIC INDEX: Analysis and Predictions", className="dashboard-title"))]),
        html.Div(className="content", children=[
            html.Div(className="graph-container", children=[dcc.Graph(figure=map_fig, style={'width': '100%', 'height': '80vh'})]),
            html.Div(className="image-container", children=[html.Img(src="assets/what_is_dem.png", style={'width': '80vw'}, className="image")]),
            html.Div(className="subplots-container", style={'rowGap': '5px', 'columnGap': '5px', 'width': '90vw', 'height':'auto'}, children=[
                html.Div(className="subplot", style={'width': '50%'}, children=[dcc.Graph(figure=line_fig)]),
                html.Div(className="subplot", style={'width': '50%'}, children=[dcc.Graph(figure=stack_fig)])
            ]),
            html.Div(className="subplots-container", style={'rowGap': '5px', 'columnGap': '5px', 'width': '90vw', 'height':'auto'}, children=[
                html.Div(className="subplot", style={'width': '50%'}, children=[dcc.Graph(figure=pie_fig)]),
                html.Div(className="subplot", style={'width': '50%'}, children=[dcc.Graph(figure=bar_fig)])
            ]),
            html.Div(className="image-container", children=[html.Img(src="assets/sum.png", style={'width': '80vw'}, className="image")])
        ])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
