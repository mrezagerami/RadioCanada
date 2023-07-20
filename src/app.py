import dash
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import requests
import csv

import polar
import bar_chart
import sunburst
import network

app = Dash(__name__)
server = app.server
app.title = 'Radio Canada Data Visualization Project | INF8808'

dataframe = pd.read_csv('f:/RC50000.csv')
#dataframe = pd.read_csv('./RC1000-1.csv')

polar_fig = polar.generate_polar(dataframe)
bar_fig = bar_chart.generate_bar_chart(dataframe)
sunburst_fig = sunburst.generate_sunburst(dataframe)
network_fig = network.generate_network(dataframe)

app.layout = html.Div(
    children=[
        html.H1("Radio Canada Data Visualization", style={'text-align': 'center'}),
        html.H3("Our project is focused on visualizing the user journey to create an account on Radio Canada's platform, including the utilization of referral codes, visit times, and establishing connections. By analyzing and visualizing these aspects, we strive to improve user experience, optimize the account creation process, and identify key connections between user actions.", style={'text-align': 'center'}),
        html.H2("Polar Chart"),
        dcc.Graph(
            id='polar-chart',
            figure=polar_fig
        ),
        html.H3("This polar chart provides unique insights into website visit distribution across time periods. The chart is divided into 24 sectors, representing one-hour intervals, and incorporates hue variations to indicate visit ratios. By examining the chart, we can identify peak times and high visitation rates.", style={'text-align': 'center'}),
        html.Br(),

        html.H2("Bar Chart"),
        dcc.Graph(
            id='bar-chart',
            figure=bar_fig
        ),
        html.H3("The bar chart here visually represents the correlation between referral sources and the likelihood of site visitors accessing specific areas. It features two axes: the horizontal axis displays various referral sources and on the vertical axis, the chart presents the number of visits to different sections of the Radio Canada website. This visualization helps us understand the impact of different referral sources on user engagement with specific areas of the site.", style={'text-align': 'center'}),
        html.Br(),

        html.H2("Sunburst Chart"),
        dcc.Graph(
            id='sunburst-chart',
            figure=sunburst_fig
        ),
        html.H3("The focus here is to understand the frequency of different user paths leading to account creation. To accomplish this, we have chosen a sunburst model as our primary visualization tool. The sunburst model provides a graphical representation of the user paths and includes a tooltip displaying the percentage of account creation and the specific user paths. This hierarchical representation helps enhance our understanding of the concept. The chart showcases the initial action at the center, followed by subsequent layers representing common actions leading to account creation, such as visiting specific website sections like sports and videos.", style={'text-align': 'center'}),
        html.Br(),

        html.H2("Network Chart"),
        html.Iframe(
            srcDoc=network_fig,
            width='100%',
            height='800px',
            style={'border': 'none'}
        ),
        html.H3("The network diagram here provides a concise representation of connections between different sections of the website. Nodes represent individual sections, while lines depict the paths between them. This diagram is useful for understanding complex systems, analyzing social networks, and visualizing information flow. In the context of the Canadian Radio website, the network diagram showcases interconnections among sections and visitation rates for each route. The chart helps identify popular paths and interactions between sections, especially in relation to account creation.", style={'text-align': 'center'}),
        html.Br(),
    ],
    style={'text-align': 'center'}
)



if __name__ == "__main__":
    app.run_server(debug=True)
