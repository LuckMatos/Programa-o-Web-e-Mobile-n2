'''6. **Filtragem de Dados**:
   Filtre o DataFrame criado no exercício 1 para mostrar apenas pessoas cuja idade seja maior que 25 e que vivam em uma cidade diferente de 'Rio de Janeiro'.
'''
import pandas as pd

base = {'Nome': ['Lucas', 'Bruno', 'Luana', 'Juliana', 'Fernando'],
        'Idade': [28, 35, 25, 89, 25],
        'Cidade': ['Aparecida de Goiania', 'Goiania', 'Samavi', 'Samavi', 'Rio de Janeiro']}
base = pd.DataFrame(base)
print('-'*50)

filtro_idade_cidade = base[(base['Idade'] > 25) & (
    base['Cidade'] != 'Rio de Janeiro')]
print(filtro_idade_cidade)

'''7. **Agrupamento e Estatísticas**:
   Agrupe o DataFrame do exercício 1 por 'Cidade' e calcule a soma e a média da idade das pessoas em cada cidade.'''
agrupar_cidade = base.groupby(by=['Cidade'])['Idade']
print(agrupar_cidade.sum())
agrupar_cidade = base.groupby(by=['Cidade', 'Nome'])['Idade']
print(agrupar_cidade.mean())
agrupar_cidade = base.groupby(by=['Cidade'])['Idade']
