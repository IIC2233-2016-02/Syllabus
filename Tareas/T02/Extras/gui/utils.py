import os


PATH = os.path.dirname(__file__)
REL_PATH = PATH[PATH.index(os.getcwd()) + len(os.getcwd()) + 1:]


def get_asset_path(name, sep=os.sep):
    return REL_PATH + sep + "assets" + sep + name
