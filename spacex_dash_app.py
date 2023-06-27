# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
#spacex_df.head(5)

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                            options=[
                                                {'label': 'All Sites', 'value': 'ALL'},
                                                {'label': 'CCAFS LC-40', 'value': 'site1'},
                                                {'label': 'CCAFS SLC-40', 'value': 'site2'},
                                                {'label': 'KSC LC-39A', 'value': 'site3'},
                                                {'label': 'VAFB SLC-4E', 'value': 'site4'},
                                            ],
                                            value='ALL',
                                            placeholder="Select a Launch Site here",
                                            searchable=True
                                             ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=2500,
                                                marks={0:'0',
                                                       2500:'2500',
                                                       5000:'5000',
                                                       7500:'7500',
                                                       10000: '10000'},
                                                value=[min_payload, max_payload] ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# add callback decorator
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'))

# Add computation to callback function and return graph
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(filtered_df, values = 'class')
        names = 'Pie Chart All Sites'
        title = 'Space X Sites Success'
        return fig
    else:    
        if  entered_site == 'site1':
            launch_site = 'CCAFS LC-40'
        elif entered_site == 'site2':
            launch_site = 'CCAFS SLC-40'    
        elif entered_site == 'site3':
            launch_site = 'KSC LC-39A'    
        elif entered_site == 'site4':
            launch_site = 'VAFB SLC-4E'        
        else:
            pass    

        filtered_df = spacex_df[spacex_df['Launch Site'] == launch_site]
        class_value = filtered_df.groupby('class').size()
        fig = px.pie(values = class_value)
        names = 'Pie Chart for Site ' 
        title = 'Space X Success for Site ' + launch_site
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'),
			   Input(component_id='payload-slider', component_property='value'))

# Add computation to callback function and return graph
def get_scatter_plot(entered_site, payload_value):
    if entered_site == 'ALL':
        fig1 = px.scatter(spacex_df,x='Payload Mass (kg)',y='class', color='Booster Version Category',
        title = 'Correaltion between Payload and Success for all Sites')
        return fig1
    else:    
        if  entered_site == 'site1':
            launch_site = 'CCAFS LC-40'
        elif entered_site == 'site2':
            launch_site = 'CCAFS SLC-40'    
        elif entered_site == 'site3':
            launch_site = 'KSC LC-39A'    
        elif entered_site == 'site4':
            launch_site = 'VAFB SLC-4E'        
        else:
            pass    

        filtered_df = spacex_df[spacex_df['Launch Site'] == launch_site]
        fig1 = px.scatter(filtered_df,x='Payload Mass (kg)',y='class', color='Booster Version Category',
        title = 'Space X Success for Site ' + launch_site)
        return fig1


# Run the app
if __name__ == '__main__':
    app.run_server()
