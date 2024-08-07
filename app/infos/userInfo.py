import os
import configparser

CONFIG_FILE = 'config.ini'

config = configparser.ConfigParser()

def load_rid(section):
    if config.read(CONFIG_FILE) and config.has_section(section):
        return config.get(section, 'rid', fallback=-1)
    return -1

def load_country(section):
    if config.read(CONFIG_FILE) and config.has_section(section):
        return config.get(section, 'country', fallback='Belgium')
    return 'Belgium'

restaurantId = load_rid('restaurent')
country = load_country('country')
# abPath = 'D:/work/Stage fr/XudoX.be/project/testFile'
abPath = '.'



def save_path(section, path):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, 'path', path)
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def load_path(section):
    if config.read(CONFIG_FILE) and config.has_section(section):
        return config.get(section, 'path', fallback=abPath)
    return abPath

def save_export_path(path):
    save_path('export', path)

def load_export_path():
    return load_path('export')

def save_import_path(path):
    save_path('import', path)

def load_import_path():
    return load_path('import')
    

# def save_selected_path(path):
#     with open(CONFIG_FILE, 'w') as file:
#         file.write(path)

# def load_selected_path():
#     if os.path.exists(CONFIG_FILE):
#         with open(CONFIG_FILE, 'r') as file:
#             return file.read().strip()
#     return abPath