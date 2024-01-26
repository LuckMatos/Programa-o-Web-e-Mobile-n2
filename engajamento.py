import pandas as pd
import numpy as np

base = pd.read_excel(
    'C:\\Users\\Lucas\\Downloads\\08. Analisando o engajamento no Instagram.xlsx')  # importando base
base = base.drop("Visualizações", axis=1)

# Após identificar os valores válidos dentro da base atribuimos aos valores nulos para tratar.
base.loc[base.Carrossel.isnull(), "Carrossel"] = 'N'
print(base.head())  # Exbindo base  para analise exploratória.

# filtrando as coluncas necessárias para análise
filtro = base[['Tipo', 'Curtidas', 'Comentários', 'Interacoes']]
print(filtro)

curtida = base.Curtidas.sum()  # Somanda o total de Curtidas
print(f'O total em Curtidas é {curtida:.2f}')
coment = base.Comentários.sum()
print(f'O total em Comentários é {coment:.2f}')
interacoes = base.Interacoes.sum()
print(f'O total em Interações é {interacoes:.2f}')


# Utilizando método info() para saber a quantidade de valores nulos ( NAN)
#print(base.info())
# Utilizando a método LOC para localizar os falores nulos da coluna Carrossel.
#print(base.loc[base.Carrossel.isnull()].head())
print(base.sort_values(by='Curtidas',ascending= False).head())
print('--'*20)
print(base.sort_values(by='Curtidas',ascending= False).tail())
print("--Grupo--")
grupo =base.groupby(['Tipo','Pessoas',])[['Curtidas', 'Comentários' ]].mean()
print(grupo)
base.loc[base.Tags.isnull(),'Tags'] = 'Sem Tag'

print(base.groupby("Tags")['Curtidas'].count()) # Agrupando o dataframe TAGS e contando quantas curtidas cada TAGs.