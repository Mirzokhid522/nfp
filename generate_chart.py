import plotly.express as px
import pandas as pd

# Load your data
df = pd.read_csv('nfp.csv') 

# Create the chart with both data series
fig = px.line(df, x='Date', y=['Trend', 'Seasonally_Adjusted'], 
              title='Employment Trends')

# Apply Dark Mode Styling
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_color='white',
    # Ensure axes and grid lines are visible against the black background
    xaxis=dict(showgrid=True, gridcolor='#333333', tickcolor='white'),
    yaxis=dict(showgrid=True, gridcolor='#333333', tickcolor='white'),
    legend=dict(font=dict(color='white'))
)

# Save as index.html
fig.write_html("index.html")
print("Dark mode chart successfully generated as index.html!")