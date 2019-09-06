import requests
import os

response = requests.get("http://www.omdbapi.com/?t=el+padrino&y=2004&apikey=e2831448")
data = response.json()
print(data)



"""github_token = e2831448
def authRequest(url, params={}):
   headers = {
      "Authorization": "token {}".format(github_token)
   }
   response = requests.get(url,headers=headers, params=params)
   print(response.status_code)
   #print(response.headers)
   return response.json()

data = authRequest("http://www.omdbapi.com/?t=el+padrino&y=2004")
print(data)

http://www.omdbapi.com/?apikey=[yourkey]&"""