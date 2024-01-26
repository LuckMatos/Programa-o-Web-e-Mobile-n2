# Filtando bases em pandas
import pandas as pd

# importando a base e atribuído a variavel data.
data = pd.read_excel(
    "C:\\Users\\Lucas\\Documents\\Aprendendo Python\\Introdução ao Pandas\\base.xlsx")

base_est = data

print(base_est[base_est["Days In Top 100"]>100])