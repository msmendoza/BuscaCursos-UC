from os import system, name

import pandas as pd
import requests as req
from bs4 import BeautifulSoup


def clear():
    """Para realizar un 'Clear Screen' en la Terminal"""
    _ = system('cls') if name == 'cls' else system('clear')


def vacantes(url_):
    """Entrega las vacantes libres y ocupadas de determinado ramo UC.

    Parameters
    ----------
    url_ : str
      URL para la POST request de determinado ramo (ej:
      http://buscacursos.uc.cl/informacionVacReserva.ajax.php
      ?nrc=20437
      &termcode=2020-2
      &cantidad_dis=39
      &cantidad_min=40
      &cantidad_ocu=1
      &nombre=Optimizaci%C3%B3n+Din%C3%A1mica
      &sigla=ICS3105
      &seccion=1).
    Returns
    -------
    pd.DataFrame
      DataFrame con las vacantes ocupadas y desocupadas por escuelas
      del ramo.
    """
    response = req.post(url=url_)
    soup = BeautifulSoup(markup=response.text, features='html5lib')
    info = soup.find('table').find_all('td')
    # Eliminamos la info no relativa a la info de las 'Escuelas'
    info = info[18:-3]
    # Eliminamos espacios para los diferentes campos
    info = [i.text.strip() for i in info]
    # Creamos sublistas para cada escuela
    info = [info[9 * i:9 * (i + 1)] for i in range(len(info) // 9)]
    # Llenamos un df con la información
    vacxesc = {}
    for esc, _, _, _, _, _, _, oc, disp in info:
        if oc == disp == '0':
            continue
        vacxesc.update({esc: (int(oc) + int(disp), oc, disp)})
    df = pd.DataFrame(vacxesc).T
    df.rename(columns={0: 'T', 1: 'O', 2: 'D'}, inplace=True)

    return df


if __name__ == '__main__':
    pass
