import numpy as np
import plotly.graph_objects as go
from collection import data

# Filter data for years 2019–2024
filtered_data = data[data['year'] >= 2019].copy()

# Create a list of unique years and roles
years = sorted(filtered_data['year'].unique())
roles = filtered_data['role'].unique()

# Create boxplots using Plotly
fig = go.Figure()

for role in roles:
    role_data = filtered_data[filtered_data['role'] == role]
    fig.add_trace(go.Box(
        x=role_data['year'],
        y=role_data['L'],
        name=role,
        boxpoints='outliers',
        marker_color=None,
        line=dict(width=1),
        showlegend=True
    ))

# Add percentile markers manually
percentile_lines = []
for (year, role), group in filtered_data.groupby(['year', 'role']):
    q25, q50, q75 = np.percentile(group['L'], [25, 50, 75])
    percentile_lines.extend([
        go.Scatter(x=[year], y=[q25], mode='markers', name=f'{role} - 25th', marker=dict(color='blue', symbol='line-ew')),
        go.Scatter(x=[year], y=[q50], mode='markers', name=f'{role} - 50th (Median)', marker=dict(color='black', symbol='circle')),
        go.Scatter(x=[year], y=[q75], mode='markers', name=f'{role} - 75th', marker=dict(color='red', symbol='line-ew')),
    ])

# Add percentile scatter plots
for trace in percentile_lines:
    fig.add_trace(trace)

# Customize layout
fig.update_layout(
    title="Luminance Distribution by Role with Percentile Overlays",
    xaxis_title="Year",
    yaxis_title="Luminance (L*)",
    boxmode='group',
    width=1000,
    height=600
)

fig.show()
