import pandas as pd
from matplotlib import pyplot as plt

#adding a comment here
# 5+4 = 7
df = pd.read_csv('../data/dataset.csv')

df.plot()
plt.savefig('../results/plot.png', dpi=300)
