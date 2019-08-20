# This script uses Pandas and Bokeh to provide a line graph based off large amounts of data.
# Data is read in through a CSV file and plots X vs Y based off column titles.
#
# To install Pandas:    $ pip3 install pandas
# To install Bokeh:     $ pip3 install bokeh

# importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# Define constants here
CSV_INPUT = "data.csv"
HTML_OUTPUT = "MyChart.html"
X_AXIS_DATA_COLUMN = "Year"
Y_AXIS_DATA_COLUMN = "Engineering"

# prepare some data from csv
df = pandas.read_csv(CSV_INPUT)
x = df[X_AXIS_DATA_COLUMN]
y = df[Y_AXIS_DATA_COLUMN]
# data is read in like this, as a list...
# x=[1,2,3,4,5]
# y=[6,7,8,9,10]

# prepare the output file
output_file(HTML_OUTPUT)

# create a figure object
f = figure()

# create line plot
f.line(x, y)

# triangle glyphs
# f.triangle(x,y)

# circle glyphs
# f.circle(x,y)

show(f)
