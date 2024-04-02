from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


def obtener_variable_env(variable):
    """
    Retorna el valor de las variables de entorno
    """
    return os.getenv(variable)


def configurar_variables():
    """
    Diccionario para retornar las variables en el archivo .env
    """
    variables = {
        'api_key': obtener_variable_env('api_key'),
        'api_secret': obtener_variable_env('api_secret'),
        'pagination': obtener_variable_env('pagination'),
        'file_path': obtener_variable_env('file_path'),
        'base_url': obtener_variable_env('base_url'),
        'country': obtener_variable_env('country'),
        'language': obtener_variable_env('language'),
        'maxItems': obtener_variable_env('maxItems'),
        'operation': obtener_variable_env('operation'),
        'property_type': obtener_variable_env('property_type'),
        'order': obtener_variable_env('order'),
        'center': obtener_variable_env('center'),
        'distance': obtener_variable_env('distance'),
        'sort': obtener_variable_env('sort'),
        'maxprice': obtener_variable_env('maxprice'),
        'minprice': obtener_variable_env('minprice'),
        'sincedate': obtener_variable_env('sincedate'),
        'publicationDate': obtener_variable_env('publicationDate'),
        'modificationDate': obtener_variable_env('modificationDate'),
        'minsize': obtener_variable_env('minsize'),
        'maxsize': obtener_variable_env('maxsize'),
        'flat': obtener_variable_env('flat'),
        'penthouse': obtener_variable_env('penthouse'),
        'duplex': obtener_variable_env('duplex'),
        'studio': obtener_variable_env('studio'),
        'chalet': obtener_variable_env('chalet'),
        'bedrooms': obtener_variable_env('bedrooms'),
        'bathrooms': obtener_variable_env('bathrooms'),
        'preservation': obtener_variable_env('preservation'),
        'newDevelopment': obtener_variable_env('newDevelopment'),
        'furnished': obtener_variable_env('furnished'),
        'bankOffer': obtener_variable_env('bankOffer'),
        'garage': obtener_variable_env('garage'),
        'terrance': obtener_variable_env('terrance'),
        'exterior': obtener_variable_env('exterior'),
        'elevator': obtener_variable_env('elevator'),
        'swimmingpool': obtener_variable_env('swimmingpool'),
        'airconditioning': obtener_variable_env('airconditioning'),
        'storeroom': obtener_variable_env('storeroom'),
        'rooms': obtener_variable_env('rooms')
    }
    return variables


# Llamar a la función de variables
variables = configurar_variables()

# Credenciales api
api_key = variables['api_key']
api_secret = variables['api_secret']

# Páginas que extraer
pagination = variables['pagination']

# Path y nombre del fichero destino
fecha_ejecucion = datetime.now().strftime('%Y_%m_%d')
nombre_archivo = f'pisos_idealista_{fecha_ejecucion}.csv'
file_path = variables['file_path'] + "\\" + nombre_archivo

# Columnas para extraer ejemplo en consola
# columnas_ejemplo = ['price', 'propertyType', 'size', 'exterior', 'rooms', 'bathrooms', 'municipality', 'address']

# Parámetros
base_url = variables['base_url']
country = variables['country']
language = variables['language']
maxItems = variables['maxItems']
operation = variables['operation']
property_type = variables['property_type']
order = variables['order']
center = variables['center']
distance = variables['distance']
sort = variables['sort']
maxprice = variables['maxprice']
minprice = variables['minprice']
sincedate = variables['sincedate']
publicationDate = variables['publicationDate']
modificationDate = variables['modificationDate']
minsize = variables['minsize']
maxsize = variables['maxsize']
flat = variables['flat']
penthouse = variables['penthouse']
duplex = variables['duplex']
studio = variables['studio']
chalet = variables['chalet']
bedrooms = variables['bedrooms']
bathrooms = variables['bathrooms']
preservation = variables['preservation']
newDevelopment = variables['newDevelopment']
furnished = variables['furnished']
bankOffer = variables['bankOffer']
garage = variables['garage']
terrance = variables['terrance']
exterior = variables['exterior']
elevator = variables['elevator']
swimmingpool = variables['swimmingpool']
airconditioning = variables['airconditioning']
storeroom = variables['storeroom']
rooms = variables['rooms']
