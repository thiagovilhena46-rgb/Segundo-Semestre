import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../CSVs/california_housing_train.csv')
plt.hist(df['median_house_value'])

plt.show()