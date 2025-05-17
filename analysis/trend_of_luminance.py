import plotly.express as px
from sklearn.linear_model import LinearRegression
from collection import data

filtered_data = data[data['year'] >= 2019].copy()
avg_luminance = filtered_data.groupby(['year', 'role'])['L'].mean().reset_index()

reg_model = LinearRegression()

fig = px.scatter(
    avg_luminance,
    x='year',
    y='L',
    color='role',
    title='Linear Trend of Luminance by Role Over Time (2019–2024)',
    labels={'L': 'Average Luminance (L*)', 'year': 'Year', 'role': 'Role'},
    height=600
)

for role in avg_luminance['role'].unique():
    role_data = avg_luminance[avg_luminance['role'] == role]
    X = role_data['year'].values.reshape(-1, 1)
    y = role_data['L'].values
    
    reg_model.fit(X, y)
    
    y_pred = reg_model.predict(X)
    
    fig.add_scatter(
        x=role_data['year'],
        y=y_pred,
        mode='lines',
        name=f'{role} Trend Line',
        line=dict(dash='dash', width=2)
    )

fig.show()
