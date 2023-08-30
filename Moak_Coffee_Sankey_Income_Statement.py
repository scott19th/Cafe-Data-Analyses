import plotly.graph_objects as go

# Compile Data

source = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13]  # 14 Source Nodes
target = [9, 9, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12, 13, 14, 15, 16, 17]  # 9 Target Nodes
value = [56.8, 49.6, 49.6, 38.1, 26.5, 23.8, 18.4, 2.2, 9.9, 244.4, 30.5, 69.9, 205, 30, 39.9, 136.1, 68.9]  # 17 Values

# Create Labels
label = ['Leith', 'Corstorphine', 'Morningside', 'Comely Bank', 'Royal Mile',
         'Newington', 'Online', 'Events', 'Wholesale+', 'Store Revenue',
         'Other Revenue', 'Revenue', 'Gross Profit', 'Cost of Revenue',
         'Operating Profit', 'Operating Expenses', 'Labour', 'Stock',
         ]

link = dict(source=source, target=target, value=value,)
node = dict(label=label, pad=35, thickness=20)
data = go.Sankey(link=link, node=node)

# Setup our Plotly chart

fig = go.Figure(data)

# Create brand colour palatte

colour_for_nodes = ['#ABCAF8','#ABCAF8','#ABCAF8','#ABCAF8','#ABCAF8','#ABCAF8',
                    '#FFE389', '#FFE389', '#FFE389', '#ABCAF8', '#FFE389', '#ABCAF8',
                    '#9DCEA0', '#FF6961', '#9DCEA0', '#FF6961', '#FF6961', '#FF6961']

colour_for_links = ['#C3D7EE', '#C3D7EE', '#C3D7EE', '#C3D7EE', '#C3D7EE', '#C3D7EE',
                    '#FDFD96', '#FDFD96', '#FDFD96', '#C3D7EE', '#FDFD96', '#C1E1C1',
                    '#F1ADCE', '#C1E1C1', '#F1ADCE', '#F1ADCE', '#F1ADCE']

# Upddate chart with a title and the background colour of the chart

fig.update_layout(
    hovermode='x',
    title= "Moak Cafe - Income Statement June 2023",
    font=dict(size=10, color='black'),
    paper_bgcolor='#FFF3F5',
)

# Add node and link colours

fig.update_traces(node_color = colour_for_nodes, link_color = colour_for_links)

# Add anotations for node amounts

fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.94, showarrow=False, text='<b>£56.8K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.78, showarrow=False, text='<b>£49.6K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.61, showarrow=False, text='<b>£49.6K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.465, showarrow=False, text='<b>£38.1K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.345, showarrow=False, text='<b>£26.5K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.225, showarrow=False, text='<b>£23.8K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.125, showarrow=False, text='<b>£18.4K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=0.04, showarrow=False, text='<b>£9.9K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.018, y=-0.03, showarrow=False, text='<b>£2.2K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.265, y=0.57, showarrow=False, text='<b>£244.4K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.265, y=0.11, showarrow=False, text='<b>£30.5K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.525, y=0.48, showarrow=False, text='<b>£275K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.785, y=0.48, showarrow=False, text='<b>£205K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.785, y=0.14, showarrow=False, text='<b>£69.9K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.98, y=0.56, showarrow=False, text='<b>£136K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.98, y=0.285, showarrow=False, text='<b>£68.9K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.98, y=0.12, showarrow=False, text='<b>£39.9K</b>'))
fig.add_annotation(dict(font=dict(color="#333333",size=10, family="Arial"), x=0.98, y=0.0005, showarrow=False, text='<b>£30K</b>'))


fig.show()