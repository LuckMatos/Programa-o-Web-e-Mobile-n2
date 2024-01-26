'''5. **Formatação de Números**:
   Crie um DataFrame com números de ponto flutuante e formate-os para exibir apenas duas casas decimais e com uma vírgula como separador de milhares.
'''
import pandas as pd

base = {'numero': [1.2000, 2.000, 4.000, 4.669, 10.000]}
base = pd.DataFrame(base)
print(base.info())
tratamento = str(base.apply(lambda x: f'{x:.2f}'.replace('.', ',')))
print(tratamento)
