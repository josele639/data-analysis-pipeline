import pandas as pd
from apy import api_datosPeliculas

cine = pd.read_csv('../Input/datos_2010.csv')

#Una vez tenemos los datos hacemos una lista de los IDs para recoger los nuevos datos con la API

lista_id = cine["ID"].tolist()
datospeli = pd.DataFrame(columns=('imdb_id','budget','revenue','vote_average'))

datospeli = api_datosPeliculas(lista_id, datospeli)

#Renombro la columna ID para hacer Merge con la principal.
cine = cine.rename(columns={"ID" : "imdb_id"})
#Hago Merge
df_cine = pd.merge(cine, datospeli, how ='inner', on ='imdb_id') 

#Transformo las columnas en Int para poder sacar estadisticas de ellas.
df_cine['budget'] = df_cine.budget.astype(int)
df_cine['revenue'] = df_cine.revenue.astype(int)

#Me quedo solo con las filas que tengan voto medio.
df_cine_vote = df_cine[df_cine.vote_average != 0]

#Exporto este dataframe para trabajarlo despues.
export_csv = df_cine_vote.to_csv (r'../output/df_cine_vote.csv', index = None, header=True)

#Creo un dataframe con las peliculas que tengan Presupuesto y Beneficio.
df_cine_bv = df_cine[df_cine.budget != 0]
df_cine_bv = df_cine_bv[df_cine_bv.revenue != 0]

export_csv = df_cine_bv.to_csv (r'../output/df_cine_bv.csv', index = None, header=True)