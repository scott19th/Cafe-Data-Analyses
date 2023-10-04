import pandas as pd
import plotly.express as px
import os

# create a variable with path to data files
path_to_files = ("./store_sales_data/")

# creat a list of the files in the directory
store_files = [f for f in os.listdir(path_to_files) if f.endswith('.csv')]

# iterate over the files in the list
for file_name in store_files:
    # create a full path to each file
    file_path = os.path.join(path_to_files, file_name)

    # Read the data into dataframe
    Sunburst_Sales = pd.read_csv(file_path)

    # clean data by removing null sales products
    # Sunburst_Sales = Sunburst_Sales[['Name', 'Accounting group', 'Net amount']]
    Sunburst_Sales = Sunburst_Sales[Sunburst_Sales['Net amount'] != 0.00]

    # Extract a title from the file name.
    chart_title = file_name.replace(".csv", "").replace("_", " ").title()

    # create sunburst
    fig = px.sunburst(Sunburst_Sales,
                      path=['Accounting group', 'Name'],
                      values='Net amount')

    # update the layout to include a title using chart_title variable
    fig.update_layout(
        title_text=f"Sunburst Chart for {chart_title}",
        title_x=0.5,
    )
    # Update hover data to include £ symbol
    fig.update_traces(
        hovertemplate='<b>%{label} </b> <br> £%{value}<extra></extra>'
    )
    # write sunburst chart into html file
    fig.write_html(os.path.join(
        path_to_files, f"sunburst_{file_name.replace('.csv', '.html')}"))

   # show fig in browser
    fig.show()
