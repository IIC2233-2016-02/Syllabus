__author__ = 'Florencia'

import json


def jsonToDict(path):
    with open(path, encoding="utf-8") as json_file:
        json_str = json_file.read()
        json_data = json.loads(json_str)

    return json_data


def dictToJson(path, data):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=3)


if __name__ == '__main__':

    #ejemplo

    data = jsonToDict("programonMoves.json")

    for elem in data:
        elem["name"] = elem["name"].lower()

    dictToJson("programonMoves2.json", data)
