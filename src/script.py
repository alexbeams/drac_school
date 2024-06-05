import pandas as pd
from matplotlib import pyplot as plt

#adding a comment here
# adding another comment here
# adding yet another comment here
df = pd.read_csv('../data/dataset.csv')

# this code generates a plot
df.plot()
plt.savefig('../results/plot.png', dpi=300)
