import requests
import os
from dotenv import load_dotenv
"""
load_dotenv(dotenv_path='.env')
github_token = os.getenv('github_token', 'No value found')

def authRequest(url, params={}):
   headers = {
      "Authorization": "token {}".format(github_token)
   }
   response = requests.get(url,headers=headers, params=params)
   print(response.status_code)
   #print(response.headers)
   return response.json()

#data = authRequest("https://api.github.com/user/repos?type=private")
data = authRequest("https://api.themoviedb.org/3/movie/tt0068646?api_key=57c748952397091a8284c271e0895302",{"sort":"newest"})
print(data)"""

token = "57c748952397091a8284c271e0895302"
def datosPeliculas(id_peli):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}".format(id_peli,token))
    print(response.status_code)
    gas = response.json()
    print(gas.keys())
    #gas['budget','revenue','vote_average']


datosPeliculas("tt0068646")
