import pandas as pd

# importando a base e atribuído a variavel data.
data = pd.read_excel(
    "C:\\Users\\Lucas\\Documents\\Aprendendo Python\\Introdução ao Pandas\\base.xlsx")

base_estatistica = data

print(base_estatistica.head())
print(base_estatistica[['Rank','Days In Top 10','Viewership Score']])
 