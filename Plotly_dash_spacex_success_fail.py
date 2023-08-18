import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into a pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Create a dash application
app = dash.Dash(__name__)

# Create a list of launch site names
launch_site_names = spacex_df["Launch Site"].unique()
dropdown_options = [{"label": "All Sites", "value": "All"}] + [
    {"label": site, "value": site} for site in launch_site_names
]

# Create an app layout
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40},
        ),
        # Dropdown to select launch site
        dcc.Dropdown(
            id="site-dropdown",
            options=dropdown_options,
            value="All",
            placeholder="Select Site",
            searchable=True,
        ),
        html.Br(),
        # Pie chart to show the total successful launches count for all sites
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (Kg):"),
        # Slider to select payload range
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            marks={0: "0", 100: "100"},
            value=[min_payload, max_payload],
        ),
        # Scatter chart to show the correlation between payload and launch success
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)


# Callback to update pie chart based on dropdown selection
@app.callback(Output("success-pie-chart", "figure"), [Input("site-dropdown", "value")])
def update_pie_chart(selected_site):
    if selected_site is None or selected_site == "All":
        site_success_count = (
            spacex_df[spacex_df["class"] == 1].groupby("Launch Site")["class"].count()
        )
        fig = px.pie(
            names=site_success_count.index,
            values=site_success_count.values,
            title="Successful Launches by Site",
        )
    else:
        selected_site_df = spacex_df[spacex_df["Launch Site"] == selected_site]
        success_count = selected_site_df[selected_site_df["class"] == 1][
            "class"
        ].count()
        failure_count = selected_site_df[selected_site_df["class"] == 0][
            "class"
        ].count()
        fig = px.pie(
            names=["Success", "Failure"],
            values=[success_count, failure_count],
            title=f"Success vs. Failure for {selected_site}",
        )
    return fig


# Callback to update scatter chart based on dropdown selection and payload range
@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")],
)
def update_scatter_chart(selected_site, payload_range):
    if selected_site == "All":
        filtered_df = spacex_df[
            (spacex_df["Payload Mass (kg)"] >= payload_range[0])
            & (spacex_df["Payload Mass (kg)"] <= payload_range[1])
        ]
    else:
        selected_site_df = spacex_df[spacex_df["Launch Site"] == selected_site]
        filtered_df = selected_site_df[
            (selected_site_df["Payload Mass (kg)"] >= payload_range[0])
            & (selected_site_df["Payload Mass (kg)"] <= payload_range[1])
        ]

    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title="Payload vs. Launch Outcome",
    )
    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
