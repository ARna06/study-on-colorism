import plotly.express as px
from collection import data

# Filter and prepare data
filtered_data = data[data['year'] >= 2019].copy()
avg_luminance = filtered_data.groupby(['year', 'role'])['L'].mean().reset_index()

# Plot with Plotly
fig = px.line(
    avg_luminance,
    x='year',
    y='L',
    color='role',
    markers=True,
    title='Average Luminance Over Time by Role (2019–2024)',
    labels={'L': 'Average Luminance (L*)', 'year': 'Year', 'role': 'Role'}
)

fig.update_layout(
    height=600,
    xaxis=dict(dtick=1),
    yaxis_title="Luminance (L*)"
)

fig.show()
