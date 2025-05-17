import plotly.express as px
from collection import data

# Filter for 2019–2024
filtered_data = data[data['year'] >= 2019].copy()

# Plot histogram
fig = px.histogram(
    filtered_data,
    x='L',
    color='role',
    marginal='box',  # Adds boxplot to show distribution shape
    nbins=30,
    title='Luminance Histogram by Role (2019–2024)',
    labels={'L': 'Luminance (L*)'},
    barmode='overlay',
    opacity=0.7
)

fig.update_layout(
    height=600,
    xaxis_title='Luminance (L*)',
    yaxis_title='Count'
)

fig.show()