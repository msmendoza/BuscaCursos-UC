"""
functions.py
Python Version: 3.8.1

Created by Mauro S. Mendoza Elguera at 07-01-20
Pontifical Catholic University of Chile

"""

import requests as req
from bs4 import BeautifulSoup


def vacantes(sigla, sec, url):
    """
    Entrega las vacantes libres y ocupadas de determinado ramo UC.

    :param str sigla: Sigla del ramo (e.g. 'ICS3143')
    :param int sec: Integer con la sección del ramo (e.g. 1)
    :param str url: Link en BuscaCursos
    :rtype: dict
    :return: Diccionario con las vacantes ocupadas y desocupadas
    """

    url = url.format(sigla)
    response = req.get(url=url)
    soup = BeautifulSoup(markup=response.text, features='html5lib')

    filtered_tr_tags = [i for i in soup.find_all(name='tr') if len(i) == 33]
    td_tags = filtered_tr_tags[sec - 1].find_all(name='td')

    vc = {
        'ocupadas':
            int(td_tags[11].contents[0]) - int(td_tags[12].contents[0]),
        'libres': int(td_tags[12].contents[0])
        # 'ocupadas': 5,
        # 'libres': 25
    }
    return vc


if __name__ == '__main__':
    # TODO
    #       - Modificar los gráficos para separar las vacantes por escuelas
    #       - Recordar QPieSlice y como es que se podían añadir PieSlices
    #         hacia dentro del gráfico
    #       - Mejor la interacción y apariencia de los gráficos.

    post_data = {
        'nrc': '14135',
        'termcode': '2020-1',
        'cantidad_dis': '30',
        'cantidad_min': '30',
        'cantidad_ocu': '0',
        'nombre': 'Optimización+Avanzada',
        'sigla': 'ICS3153',
        'seccion': '1'
    }

    response = req.post(
        url='http://buscacursos.uc.cl/informacionVacReserva.ajax.php?'
            'nrc=14135&'
            'termcode=2020-1&'
            'cantidad_dis=30&'
            'cantidad_min=30&'
            'cantidad_ocu=0&'
            'nombre=Optimizaci%C3%B3n+Avanzada&'
            'sigla=ICS3153&'
            'seccion=1',
    )
    soup = BeautifulSoup(markup=response.text, features='html5lib')
    for i in [i.contents for i in soup.find_all('td')]:
        print(i)
