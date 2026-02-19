import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(round(titanic.groupby("Embarked")["Age"].mean().loc["S"],5))


print(titanic.groupby("Embarked")["Age"].mean().sort_values())