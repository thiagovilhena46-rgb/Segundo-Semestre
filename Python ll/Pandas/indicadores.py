import pandas as pd

titanic = pd.read_csv("titanic.csv")

def faixa_etaria(linhas):
    idade = linhas["Age"]
    if idade < 12:
        return "criança"
    elif idade >=12 and idade < 18:
        return "adolescente"
    elif idade >=18 and idade < 65:
        return "adulto"
    elif idade >= 65:
        return "idoso"
    else:
        return "nada"
        
titanic["faixa_etaria"] = titanic.apply(faixa_etaria, axis=1)

def soma_sibsp_parch(linha):
    return linha["SibSp"] + linha["Parch"]

titanic["Relatives"] = titanic.apply(soma_sibsp_parch, axis=1)

def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""

    percent = (val / total) * 100
    return f"{percent:.2f}%"

mortos = titanic[titanic["Survived"] == 0]
mortos_sem_familia = mortos.Survived[mortos["Relatives"] == 0].count()
print("sem familia: ",mortos_sem_familia)

mortos_com_familia = mortos.Survived[mortos["Relatives"] > 0].count()
print("com familia: ",mortos_com_familia)

masc = titanic.Survived[titanic["Sex"] == "male"].count()
print("Homens:",masc)
fem = titanic.Survived[titanic["Sex"] == "female"].count()
print("Mulheres:",fem)

mortos_h = mortos.Survived[mortos["Sex"] == "male"].count()
print("Homens mortos",mortos_h)
mortas = mortos.Survived[mortos["Sex"] == "female"].count()
print("Mulheres mortas: ",mortas)

primeira = titanic.Survived[titanic["Pclass"] == 1].count()
segunda = titanic.Survived[titanic["Pclass"] == 2].count()
terceira= titanic.Survived[titanic["Pclass"] == 3].count()

print(f"Primeira: {primeira}, Segunda {segunda}, Terceira {terceira}")

mortos_primeira = mortos.Survived[mortos["Pclass"] == 1].count()
mortos_segunda = mortos.Survived[mortos["Pclass"] == 2].count()
mortos_terceira = mortos.Survived[mortos["Pclass"] == 3].count()
print(f"Mortos por classe - Primeira: {mortos_primeira}, Segunda {mortos_segunda}, Terceira {mortos_terceira}")

criança = calculate_percentage(titanic.Survived[titanic["faixa_etaria"] == "criança"].count(),titanic.Survived.count())
print(f"{criança} - criança")

adole = calculate_percentage(titanic.Survived[titanic["faixa_etaria"] == "adolescente"].count(),titanic.Survived.count())
print(f"{adole} - adolescente")

adulto = calculate_percentage(titanic.Survived[titanic["faixa_etaria"] == "adulto"].count(),titanic.Survived.count())
print(f"{adulto} - adulto")

idoso = calculate_percentage(titanic.Survived[titanic["faixa_etaria"] == "idoso"].count(),titanic.Survived.count())
print(f"{idoso} - idoso")


desafio = titanic.groupby("faixa_etaria")["PassengerId"].count().reset_index(name="qtd")
desafio["porcentagem %"] = round(desafio["qtd"] / desafio["qtd"].sum() * 100,2)

print(desafio)
































