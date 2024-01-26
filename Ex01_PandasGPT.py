# *1. **DataFrame Básico**:
# Crie um DataFrame com as colunas 'Nome', 'Idade' e 'Cidade' para representar informações pessoais de algumas pessoas.
import pandas as pd
import numpy as np

# Criando Dataframe
base = {'Nome': ['Lucas', 'Bruno', 'Luana', 'Juliana'],
        'Idade': [28, 35, 25, 89],
        'Cidade': ['Aparecida de Goiania', 'Goiania', 'Samavi', 'Samavi']}
base = pd.DataFrame(base)
print(base)

""" 2. **Seleção de Dados**:
   Escreva código para selecionar todas as pessoas com idade acima de 30 anos no DataFrame criado no exercício 1.
"""
pessoas_acima_30_anos = base[base['Idade'] > 30]
print("Pessoas com idade acima de 30 anos:")
print(pessoas_acima_30_anos)

''' 3. **Agregação de Dados**:
   Calcule a média de idade das pessoas na cidade deseja.'''
idade_media_em_Samavi = base.groupby('Cidade')['Idade'].mean()
print(idade_media_em_Samavi)
'''4. **Classificação de Dados**:
   Ordene o DataFrame do exercício 1 em ordem decrescente de idade.
'''
print('Ordenando o dataframe em ordem descente de acordo com a idade')
ordem_decrescente_de_idade = base.sort_values(by='Idade', ascending=False)
print(ordem_decrescente_de_idade)
