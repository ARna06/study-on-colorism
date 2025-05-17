import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
from collection import data

# Assuming `data` is already created and cleaned from the previous script

### --- ANOVA: Does luminance differ by role? --- ###
model_role = ols('L ~ C(role)', data=data).fit()
anova_table_role = sm.stats.anova_lm(model_role, typ=2)
print("ANOVA - Luminance by Role:\n", anova_table_role)

### --- ANOVA: Does luminance differ by year? --- ###
model_year = ols('L ~ C(year)', data=data).fit()
anova_table_year = sm.stats.anova_lm(model_year, typ=2)
print("\nANOVA - Luminance by Year:\n", anova_table_year)

### --- Linear Regression: Luminance trend over time by role --- ###
# Center year for better interpretation
data['year_centered'] = data['year'] - data['year'].mean()
model_time = ols('L ~ year_centered + C(role)', data=data).fit()
print("\nRegression - Luminance over time:\n", model_time.summary())

### --- Effect Size (Cohen's d) --- ###
def cohen_d(group1, group2):
    """Calculate Cohen's d for two groups."""
    diff = group1.mean() - group2.mean()
    n1, n2 = len(group1), len(group2)
    pooled_std = np.sqrt(((n1 - 1)*group1.std()**2 + (n2 - 1)*group2.std()**2) / (n1 + n2 - 2))
    return diff / pooled_std

# Cohen's d: Actor vs Actress
actor_lum = data[data['role'] == 'actor']['L']
actress_lum = data[data['role'] == 'actress']['L']
d_actor_vs_actress = cohen_d(actor_lum, actress_lum)
print(f"\nCohen's d (Actor vs Actress): {d_actor_vs_actress:.3f}")

# Cohen's d: Lead vs Side roles
lead_lum = data[data['role_type'] == 'lead']['L']
side_lum = data[data['role_type'] == 'side']['L']
d_lead_vs_side = cohen_d(lead_lum, side_lum)
print(f"Cohen's d (Lead vs Side roles): {d_lead_vs_side:.3f}")