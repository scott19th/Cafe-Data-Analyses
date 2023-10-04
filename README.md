# Hospitality Data Analyses

This repositary is to display some of the Python scripts I have created to perform data analyses on a hospitality business.

The business name and all data have been changed for privacy but the files were created to solve real world problems and provide insights to influence future decision making.

These projects include:

**Sankey Diagram** - The company needed a better understanding of the flows of capital through the business. I used Python script and the plolty library to create to create a visulisation of the companies Cost of Sales. This involved linking 17 Values accross 13 source nodes and 9 target nodes. I used a custom colour pallet to match company brand colours.

**Popular Products** - The company was able to view best selling departments and products data for each store however it was only able to be viewed one store at a time and onlt in .csv format which did not give a dynamic visual representation of the data. I created a directory to house the .csv exports. Using Python I created a list of the .csv files and then iterated over them to create a plotly sunburst chart for each store. The name of the file was used to create the chart title and zero sale products are automatically stripped out.

**Automation of Order Sheets** - Using python to create an engineering soloution to automate the manual process of exporting, sorting online sales orders into both a bakery bake list and drivers delivery sheets.

Problem: The online sales were being exported into a CSV. Each morning an administrator was required to come in early morning to sort the cake orders into a bake list for the bakery team as well as a delivery sheet for the drivers based on the customer Postcodes

Soloution: ......  This enabled us to reduce the start time of the administrator Monday to Friday and remove the need for a administrator to work over the weekend completely which saved an estimated £16,744 in labour costs from the busienss

