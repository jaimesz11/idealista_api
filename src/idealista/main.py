import sys
import pandas as pd

from idealista import api_idealista
from idealista import errores
from idealista.info_paquete import __version__, __description__
from idealista.utils import intro
from idealista.utils import consola

ERROR_ENTRADA = 1
ERROR_SALIDA = 2
ERROR_GENERAL = 99


def main():
    """
    Método principal
    """
    # Introducción
    intro(__description__, __version__)

    try:
        with consola.status('') as status:
            # Inicio programa
            # console.print(
            #     '{}'.format('Iniciando programa...'),
            #     style='bold green on black')
            consola.log(f'Iniciando programa...')

            # Crear token para utilizar la API
            str_status = f'Creando token de para la API...'
            consola.log(str_status)
            status.update(status=str_status)
            token = api_idealista.scraper_idealista.get_oauth_token(api_idealista.variables_idealista.api_key,
                                                                    api_idealista.variables_idealista.api_secret)
            print('TOKEN: ' + token)

            # Crear url propia de búsqueda con los parámetros que quiero
            str_status = f'Personalizando búsqueda...'
            consola.log(str_status)
            status.update(status=str_status)
            url_pers = api_idealista.scraper_idealista.define_search_url()
            print('URL: ' + url_pers)

            # Con el token y la URL devolver los resultados de búsqueda
            str_status = f'Trabajando con el token y la URL...'
            consola.log(str_status)
            status.update(status=str_status)
            api_idealista.scraper_idealista.search_api(token, url_pers)

            # Establecer paginación y proceder a la búsqueda con la url paginada
            str_status = f'Estableciendo paginación y procediendo a la búsqueda...'
            consola.log(str_status)
            status.update(status=str_status)
            pagination = api_idealista.variables_idealista.pagination
            first_search_url = url_pers % pagination
            results = api_idealista.scraper_idealista.search_api(token, first_search_url)
            total_pages = results['totalPages']
            consola.print(
                '{}'.format('La búsqueda tiene un total de {} página/s'.format(total_pages),
                            style='bold green on black'))
            consola.print(
                '{}'.format('Se extraerán {} páginas'.format(pagination),
                            style='bold green on black'))

            # Se puede ampliar los resultados a más páginas (podemos sacar 50 resultados por página)

            # Guardar conjunto de datos en un csv
            str_status = f'Extrayendo datos en un dataframe...'
            consola.log(str_status)
            status.update(status=str_status)
            df = api_idealista.scraper_idealista.results_to_df(results)
            df_tot = pd.DataFrame(df)
            df_tot = api_idealista.scraper_idealista.concat_df(df, df_tot)

            # Crear bucle para recoger todos los datos de todas las páginas
            # Como ya tenemos la primera del anterior paso, empezará en la segunda página
            # for i in range (2, total_pages):
            #
            #     url_pers = url_pers % i
            #     results = scraper_ideal.search_api(token, url_pers)
            #     df = scraper_ideal.results_to_df(results)
            #     df_tot = scraper_ideal.concat_df(df, df_tot)

            # Escribir datos a un csv
            str_status = f'Guardando datos a csv...'
            consola.log(str_status)
            status.update(status=str_status)
            api_idealista.scraper_idealista.df_to_csv(df_tot)

            consola.print(f'Se ha guardado el archivo')

            # # Ejemplo de lo guardado
            # str_status = f'Ejemplo del dataframe guardado...'
            # console.print(
            #     '{}'.format('Se muestra un conjunto pequeño de columnas, puesto que hay mucha información'),
            #     style='bold red on black')
            # console.log(str_status)
            # status.update(status=str_status)
            # scraper_ideal.df_to_csv(df_tot)
            # df = pd.read_csv('out\idealista_scraper.csv')
            #
            # # Ejemplo del dataframe para mostrar en consola
            # df_ejemplo = df[variables.columnas_ejemplo]
            # df_ejemplo = df_ejemplo.head(5)
            # print(tabulate(df_ejemplo, tablefmt='fancy_grid', headers=variables.columnas_ejemplo))

            # Proceso finalizado con éxito
            str_status = f'[green]Proceso finalizado con éxito[/green]'
            consola.log(str_status)
            status.update(status=str_status)

    except errores.InputError as err:
        consola.log(f'[traceback.text]Se ha producido un error de entrada:[\]\n'
                    f'[traceback.text]{err}[traceback.text]')

        sys.exit(ERROR_ENTRADA)


if __name__ == "__main__":
    main()
