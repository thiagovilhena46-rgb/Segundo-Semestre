import pandas as pd

titanic = pd.read_csv("titanic.csv")

titanic["Age"] = titanic["Age"].fillna
(titanic["Age"].mean())
titanic["Embarked"] = titanic["Embarked"].fillna(titanic["Embarked"].mode()[0])
titanic["Name"] = titanic["Name"].fillna("")

anne = titanic[
    (titanic["Embarked"] == "S") &
    (titanic["Pclass"] == 2) &
    (titanic["Age"] == 29.0) &
    (titanic["Name"].str.contains
     ("Anne", case=False))
]
print(anne)


if anne.iloc[0]["Survived"] == 1:
    print(f"A mulher procurada é {anne.iloc[0]["Name"]}, e ela sobreviveu")
else:
    print(f"A mulher procurada é {anne.iloc[0]["Name"]}, e ela não sobreviveu")




