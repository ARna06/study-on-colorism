from collection import data
import plotly.express as px

filtered_data = data

fig = px.box(
    filtered_data,
    x='role',
    y='L',
    points='outliers',  # Show outliers
    color='role',
    title='Luminance Distribution by Role (2015–2024)',
    labels={'L': 'Luminance (L*)'},
    width=800,
    height=600
)

fig.update_layout(
    showlegend=False,
    xaxis_title="Role",
    yaxis_title="Luminance (L*)",
    boxmode="group"
)

fig.show()