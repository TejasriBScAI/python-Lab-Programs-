import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

def main():
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                  'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        'Sales': [120, 150, 170, 160, 180,
                  200, 210, 230, 220, 240],
        'Profit': [30, 40, 45, 42, 50,
                   55, 60, 65, 63, 70],
        'Region': ['East', 'West', 'North', 'South', 'East',
                   'West', 'North', 'South', 'East', 'West']
    }

    df = pd.DataFrame(data)

    print("Dataset")
    print(df)

    # Line Chart
    line_fig = px.line(
        df,
        x='Month',
        y='Sales',
        title='Monthly Sales Trend',
        markers=True
    )

    # Bar Chart
    bar_fig = px.bar(
        df,
        x='Month',
        y='Profit',
        color='Region',
        title='Monthly Profit by Region'
    )

    # Scatter Plot
    scatter_fig = px.scatter(
        df,
        x='Sales',
        y='Profit',
        color='Region',
        size='Profit',
        hover_data=['Month'],
        title='Sales vs Profit'
    )

    # Create Dash App
    app = Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(
            children='Sales Dashboard',
            style={'textAlign': 'center'}
        ),

        dcc.Graph(
            id='line-chart',
            figure=line_fig
        ),

        dcc.Graph(
            id='bar-chart',
            figure=bar_fig
        ),

        dcc.Graph(
            id='scatter-chart',
            figure=scatter_fig
        )
    ])

    app.run(debug=True)

if __name__ == '__main__':
    main()