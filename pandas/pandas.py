import pandas as pd

# Reading csv without header
inp = pd.read_csv('data.txt', header=None)

# Retrieving particular columns by indexes, since column headers are not there
X_df = inp[inp.columns[0:2]]

# Converting dataframe to numpy ndarray
X_nd = X_df.values