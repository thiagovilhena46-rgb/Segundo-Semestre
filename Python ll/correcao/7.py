import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../CSVs/california_housing_train.csv')

plt.scatter(df['longitude'], df['latitude'], c=df['median_house_value'])