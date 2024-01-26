'''9. **Manipulação de Dados Faltantes**:
 Adicione uma coluna 'Salário' ao DataFrame do exercício 1, mas deixe alguns valores em 
branco (NaN). Em seguida, preencha os valores faltantes com a média dos salários existentes.'''

import pandas as pd

base = {'Nome': ['Lucas', 'Bruno', 'Luana', 'Juliana'],
        'Idade': [28, 35, 25, 89],
        'Salário':[2000,34444,0, 0],
        'Cidade': ['Aparecida de Goiania', 'Goiania', 'Samavi', 'Samavi']}
base = pd.DataFrame(base)
print(base)

media_salario = base.groupby(by= 'Nome')['Salário'].sum()
print(media_salario)