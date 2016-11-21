import googlemaps

API_KEY = "AIzaSyC13mub1u4I-tLhcdCCnBoC53shydShtfI"
DIR_INICIO = "Av Libertador Bernardo O'Higgins 328, Santiago, Región Metropolitana"
DIR_DESTINO = "Av Vicuña Mackenna 4860, Macul, La Florida, Región Metropolitana"

g = googlemaps.Client(key=API_KEY)
results = g.directions(DIR_INICIO, DIR_DESTINO, mode="driving")
print(results[0]['legs'])
