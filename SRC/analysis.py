import pandas as pd
import numpy as np 
import re
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import webbrowser

sns.set(style="whitegrid")
sns.set_color_codes("pastel")
# %matplotlib inline

from collections import Counter


df_cine_vote = pd.read_csv('../Output/df_cine_vote.csv')
df_cine_bv = pd.read_csv('../Output/df_cine_bv.csv')


#Nuevo dataframe dividido por géneros y media, max y min.
df_cine_vote_genre = df_cine_vote.groupby(['GENRE'])
df_cine_vote_genre_mean = df_cine_vote_genre.mean()
"""
df_cine_vote_genre.vote_average.mean()

df_cine_vote_genre.max()

df_cine_vote_genre.min()"""

#Nueva columna y agrupación para poder trabajarlo con nuevos datos.
df_cine_bv["ROI"] = ((df_cine_bv["revenue"]-df_cine_bv["budget"])/df_cine_bv["budget"])*100

df_cine_bv_genre = df_cine_bv.groupby(['GENRE'])
mean_roi_genre = (df_cine_bv_genre.ROI.mean().astype(int))
mean_roi_genre = pd.DataFrame(mean_roi_genre).sort_values(['ROI'], ascending=[False])

#Añado la columna de género para poder trabajarla en un gráfico.

mean_roi_genre['GENRE']= mean_roi_genre.index.get_level_values('GENRE')

#Genero los datos y extraigo un gráfico.
genero = Counter(mean_roi_genre["GENRE"].tolist()).most_common(12)
ROI = Counter(mean_roi_genre["ROI"].astype(int).tolist()).most_common(12)

generos = [i[0] for i in genero]
ROIs = [i[0] for i in ROI]


#Grafico 

def graf_roi_imagen():
    N = 12
    ind = np.arange(N)  
    width = 0.90      
    figsize=(17, 5)
    fig= plt.figure(figsize=(15,6))

    p1 = plt.bar(ind, ROIs, width)



    plt.ylabel('ROI')
    plt.xlabel('Generos')
    plt.title('Retorno de la inversión por género')
    plt.xticks(ind,(generos))
    plt.yticks(np.arange(0, 2200, 200))

    plt.savefig('roi.png', dpi=300, bbox_inches='tight')

    plt.show()


#Por último creo el PDF y le meto la fotografia.

def save_show_pdf():
    report = canvas.Canvas("ROI_Generos.pdf", pagesize=letter)

    text = report.beginText(200,650)
    text.setFont("Times-Roman", 12)
    text.textLine("¿Que género habrías elegido en 2010?")
    report.drawText(text)

    report.drawImage("roi.png", 50, 300,width=500, height=250)

    report.save()
    webbrowser.open_new(r'ROI_Generos.pdf')


def genero_roi_vote(genero):
    roi = str(mean_roi_genre.ROI[genero])
    vote = str(round(df_cine_vote_genre_mean.vote_average[genero], 2))
    return print("El ROI del género", genero,"es:", roi,"%","y el voto medio:",vote)

def max_10_pelis(genero):
    max10_genre = pd.DataFrame(df_cine_vote,columns=['TITLE','GENRE','vote_average'])
    max10_genre = max10_genre[max10_genre['GENRE']==genero]
    py = max10_genre.nlargest(10, ['vote_average'])

    return print(py)

def max_10_roi(genero):
    max10_roi = pd.DataFrame(df_cine_bv,columns=['TITLE','GENRE','ROI'])
    max10_roi = max10_roi[max10_roi['GENRE']==genero]
    py = max10_roi.nlargest(10, ['ROI'])
    
    return print(py)





