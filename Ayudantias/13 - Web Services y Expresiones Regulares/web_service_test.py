import requests

API_KEY = "AIzaSyC13mub1u4I-tLhcdCCnBoC53shydShtfI"
DIR_INICIO = "Av+Libertador+Bernardo+O'Higgins+328,Santiago,Región+Metropolitana"
DIR_DESTINO = "Av+Vicuña+Mackenna+4860,Macul,La+Florida,Región+Metropolitana"

request_url = "https://maps.googleapis.com/maps/api/directions/json"
params = dict(origin=DIR_INICIO, destination=DIR_DESTINO, mode='driving', key=API_KEY)
response = requests.get(url=request_url, params=params)
print(response.json())
