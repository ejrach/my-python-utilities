# This script uses Pandas and Bokeh to provide a scatter plot based off large amounts of data.
# Data is read in through an xlsx file and plots X vs Y based off column titles.
# There is some math performed prior to plotting.
#
# To install Pandas:    $ pip3 install pandas
# To install Bokeh:     $ pip3 install bokeh

import pandas

from bokeh.plotting import figure, output_file, show

# Define constants here
EXCEL_INPUT = "data.xlsx"
HTML_OUTPUT = "MyChart.html"
X_AXIS_DATA_COLUMN = "Temperature"
Y_AXIS_DATA_COLUMN = "Pressure"
CHART_TITLE = "Temperature and Air Pressure"
X_AXIS_TITLE = "Temperature (°C)"
Y_AXIS_TITLE = "Pressure (hPa)"

# Prepare some data from excel
df = pandas.read_excel(EXCEL_INPUT)

# Reading from an HTTP link
#df=pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx", sheet_name=0)

df[X_AXIS_DATA_COLUMN] = df[X_AXIS_DATA_COLUMN]/10
df[Y_AXIS_DATA_COLUMN] = df[Y_AXIS_DATA_COLUMN]/10

p = figure(plot_width=1000, plot_height=800, tools='pan')

# Chart name defintions
p.title.text = CHART_TITLE
p.title.text_color = "Gray"
p.title.text_font = "arial"
p.title.text_font_style = "bold"
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.xaxis.axis_label = X_AXIS_TITLE
p.yaxis.axis_label = Y_AXIS_TITLE

# Plot point Details
# p.circle(x,y)
p.circle(df[X_AXIS_DATA_COLUMN], df[Y_AXIS_DATA_COLUMN], size=0.5)

# Prepare the output file
output_file(HTML_OUTPUT)

show(p)
