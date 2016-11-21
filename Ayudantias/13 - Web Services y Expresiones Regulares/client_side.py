import requests
import webbrowser
import dropbox

APP_KEY = "Por buscar :)"
APP_SECRET = "Por buscar :)"


def print_entries(path, space):
    for entry in dbx.files_list_folder('{}'.format(path)).entries:
        print(''*space, entry.name)
        if isinstance(entry, dropbox.files.FolderMetadata):
            if dbx.files_list_folder("{}".format(entry.path_lower)).entries:
                print_entries(entry.path_lower, space+1)

url1 = "https://www.dropbox.com/1/oauth2/authorize?response_type=code&client_id={}".format(APP_KEY)
webbrowser.open_new(url1)
CODE = input("Ingrese codigo: ")

url2 = "https://api.dropboxapi.com/1/oauth2/token"
params = {"code": CODE, "grant_type": "authorization_code", "client_id": APP_KEY, "client_secret": APP_SECRET}
response = requests.post(url2, params=params)
diccionario = response.json()
print(response.status_code)

dbx = dropbox.Dropbox(diccionario["access_token"])
print_entries('', 0)
