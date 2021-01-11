
"""
Purpose: Stackoverflow Q59205435
Date created: 2019-12-05

Desc: Compare two data frames and find number of nulls

Ref URI: https://stackoverflow.com/questions/59205435/compare-two-data-frames-and-find-number-of-nulls/59205715#59205715

Contributor(s):
    Mark M.
"""



import pandas as pd
import numpy as np

ddict1 = {
    'c1': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c2': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c3': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c4': [1.0, 3.0, 5.0, 3.0, 7.0],
    'Nº Línea Cliente': ['Hay Algo', 'Hay Algo', 'Hay Algo', 'Hay Algo', np.NaN],
    'c6': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c7': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c8': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c9': [1.0, 3.0, 5.0, 3.0, 7.0],
    'c10': [1.0, 3.0, 5.0, 3.0, 7.0]
 }


ddict2 = {
    'ID_val': [i for i in range(1, 6)],
    'Tipo_Validacion': [1, 2, 3, 4, 1],
    'Campo_a_Validar': ['Nº Línea Cliente',
                        'Nº Línea Cliente',
                        'Nº Línea Cliente',
                        'Nº Línea Cliente',
                        'TIPO DE GARANTIA 1'],

 }


df = pd.DataFrame(ddict1)
dfP1 = pd.DataFrame(ddict2)

##############################
### User-provided attempt ####
if pd.isnull(df["Nº Línea Cliente"]).values.ravel().sum() > 0:
    nulos = pd.isnull(df["Nº Línea Cliente"]).values.ravel().sum()
    print("Hay {} valores nulos".format(nulos))
    dfP1['Numeros_de_Nulos'] = None
else:
    print ("No hay valores nulos")
dfP1.head()




##############################
##### Proposed solution ######
# Count number of NULL values in column 'Nº Línea Cliente'
nulos = df['Nº Línea Cliente'].isnull().sum()

# If nulos is greater than zero
if nulos > 0:
    # Create a column of nulls (You can use zero for NaN)
    dfP1['Numeros_de_Nulos'] = None
    # dfP1['Numeros_de_Nulos'] = 0
    # dfP1['Numeros_de_Nulos'] = np.NaN

    # Use DataFrame.loc[<index>, <column name>] to set a new value
    dfP1.loc[0, 'Numeros_de_Nulos'] = nulos




