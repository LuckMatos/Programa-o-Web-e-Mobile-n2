import pandas as pd

# importando a base e atribuído a variavel data.
data = pd.read_excel(
    "C:\\Users\\Lucas\\Documents\\Aprendendo Python\\Introdução ao Pandas\\base.xlsx")

base_est = data
print('-'*20)
print(base_est.head(3))
print('-'*20 + 'Filtro')
base_filtrada = base_est[['Rank', 'Days In Top 10', 'Viewership Score']]
print(base_filtrada)

print('-'*20+'Média, Mediana, Desvio padrão, contagem de itens( Operações básicas) da base filtrada')
media = base_filtrada.mean()
print(f'Média \n{media}')
mediana = base_filtrada.median()
print(f'Mediana\n{mediana}')
std = base_filtrada.std()
print(f'Desvio padrão\n{std}')
contagem = base_filtrada.count()
print(f'Count\n{contagem}')
describe = base_filtrada.describe()
print(f'Descrição da base\n{describe}')


print(base_filtrada[(base_filtrada["Days In Top 10"]>100)])