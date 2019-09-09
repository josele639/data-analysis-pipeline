import requests
import os
import pandas as pd
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')
token = os.getenv('token', 'No value found')


def api_datosPeliculas(lista, adr):
    count = 0
    for i in lista:
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}".format(i, token))
        print(response.status_code)
        if response.status_code == 200:
            gas = response.json()
            peli={}
            peli['imdb_id'] = gas['imdb_id']
            peli['budget'] = gas['budget']
            peli['revenue'] = gas['revenue']
            peli['vote_average'] = gas['vote_average']
            peli = pd.DataFrame(peli, index=[0])
            adr = adr.append(peli)
        count += 1
        print("Se han hecho", count, "request, quedan:", len(lista) - count)

    return adr