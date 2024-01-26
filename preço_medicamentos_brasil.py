import pandas as pd
import numpy as np

base = pd.read_excel('C:\\Users\\Lucas\\Documents\\Aprendendo Python\\aprendendoPython\\preco_medicamentos.xlsx')
#print(base.head())
print(base.info())
print(base.loc[base[base.TARJA.isnull], 'TARJA'])
