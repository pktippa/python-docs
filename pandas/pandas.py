import pandas as pd

# Reading csv without header
inp = pd.read_csv('data.txt', header=None)

# Reading csv and set name of columns
inp = pd.read_csv('data.txt', names=['column1', 'column2'])

# Reading csv and set index
inp = pd.read_csv('data.txt', index_col=['column1'])
inp = pd.read_csv('data.txt', index_col=0)

# Reset index
inp = inp.reset_index()
inp.reset_index(inplace = True)

# Show top 5 row
inp.head(5)

# Show last 5 row
inp.tail(5)

# Retrieving particular columns by indexes, since column headers are not there
X_df = inp[inp.columns[0:2]]

# Converting dataframe to numpy ndarray
X_nd = X_df.values