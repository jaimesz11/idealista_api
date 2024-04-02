import base64
import requests as rq
import json
import pandas as pd
import os
from idealista.api_idealista import variables_idealista


def get_oauth_token(api_key, api_secret):
    """
    Esta función devolverá el token personalizado
    """
    api_key = api_key
    api_secret = api_secret

    # Concatenación de campos de la API
    message = api_key + ':' + api_secret

    # Codificar el mensaje
    auth = 'Basic  ' + base64.b64encode(message.encode('ascii')).decode('ascii')  # Formato para idealista

    headers_dic = {"Authorization": auth,
                   "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}  # Definir encabezado

    params_dic = {"grant_type": "client_credentials",  # Definir parámetros de la petición
                  "scope": "read"}

    # Realizar la petición
    response = rq.post('https://api.idealista.com/oauth/token',
                       headers=headers_dic,
                       params=params_dic)

    # Extraer el token
    token = json.loads(response.text)['access_token']

    return token


def define_search_url():
    """
    Esta función combina los parámetros con la url para crear la búsqueda personalizada
    """
    url = (
            variables_idealista.base_url +
            variables_idealista.country +
            '/search?operation=' + variables_idealista.operation +
            '&propertyType=' + variables_idealista.property_type +
            '&maxItems=' + variables_idealista.maxItems +
            '&order=' + variables_idealista.order +
            '&center=' + variables_idealista.center +
            '&distance=' + variables_idealista.distance +
            '&sort=' + variables_idealista.sort +
            '&numPage=%s' +
            '&maxPrice=' + variables_idealista.maxprice +
            '&minPrice=' + variables_idealista.minprice +
            '&language=' + variables_idealista.language +
            '&minSize=' + variables_idealista.minsize +
            '&bedrooms=' + variables_idealista.bedrooms +
            '&bathrooms=' + variables_idealista.bathrooms +
            '&exterior=' + variables_idealista.exterior +
            '&elevator=' + variables_idealista.elevator +
            '&terrance=' + variables_idealista.terrance +
            '&newDevelopment=' + variables_idealista.newDevelopment
    )

    return url


def search_api(token, url):
    """
    Esta función utilizará el token y la URL creadas anteriormente y devolverá los resultados de búsqueda
    """

    headers = {'Content-Type': 'Content-Type: multipart/form-data;',  # Definir encabezado
               'Authorization': 'Bearer ' + token}

    content = rq.post(url, headers=headers)  # Devolver resultado del request

    result = json.loads(content.text)  # Transformar el resultado en formato JSON

    return result


def results_to_df(results):
    """
    Esta función guardará los resultados del json en un marco de datos y devolverá el marco de datos resultado
    """
    df = pd.DataFrame.from_dict(results['elementList'])

    return df


def concat_df(df, df_tot):
    """
    Esta función tomará el marco de datos principal (df_tot) y lo combinará con el marco de datos individual dado,
    devolviendo el marco de datos principal
    """
    pd.concat([df_tot, df])

    return df_tot


def df_to_csv(df):
    """
    Esta función tomará un marco de datos dado y lo guardará como un archivo csv
    """
    df = df.reset_index()
    # Comprobamos si la ruta donde deseamos guardar existe, si no, la creamos
    if not os.path.exists(os.path.dirname(variables_idealista.file_path)):
        os.makedirs(os.path.dirname(variables_idealista.file_path))

    df.to_csv(variables_idealista.file_path, index=False)
