from datetime import datetime
from os import system, name
from time import time, sleep

import pandas as pd
import requests as req
from bs4 import BeautifulSoup


def clear():
    """Para realizar un 'Clear Screen' en la Terminal"""
    _ = system('cls') if name == 'cls' else system('clear')


def vacantes(sem, nrc, sigla, sec):
    """Entrega las vacantes libres y ocupadas de determinado ramo UC.

    Parameters
    ----------
    sem : str
      Semestre en el que se toman ramos (ej: '2020-2')
    nrc : int
      NRC del curso (ej: 20437)
    sigla : str
      Sigla del curso (ej: 'ICS3105')
    sec : int
      Sección del curso (ej: 1)

    Returns
    -------
    (pd.DataFrame, str)
      DataFrame con las vacantes ocupadas y disponible por escuelas
      del ramo + el nombre del ramo.
    """
    base_url = 'http://buscacursos.uc.cl'
    url_ = f"{base_url}/informacionVacReserva.ajax.php" \
           f"?nrc={nrc}" \
           f"&termcode={sem}&sigla={sigla}&seccion={sec}"
    # print(url_)
    response = req.post(url=url_)
    soup = BeautifulSoup(markup=response.text, features='html5lib')
    info = soup.find('table').find_all('td')
    name_ = info[5].text.strip()  # Nombre del ramo
    # Eliminamos la info no relativa a la info de las 'Escuelas'
    info = info[18:-3]
    # Eliminamos espacios para los diferentes campos
    info = [i.text.strip() for i in info]
    # Creamos sublistas para cada escuela
    info = [info[9 * i:9 * (i + 1)] for i in range(len(info) // 9)]
    # Llenamos un df con la información
    vacxesc = {}
    if len(info) == 1:  # Para controlar cursos solo con Vacantes Libres
        response = req.get(f"{base_url}/?cxml_semestre={sem}"
                           f"&cxml_sigla={sigla}#resultados")
        soup = BeautifulSoup(markup=response.text, features='html5lib')
        info = soup.find_all('td')
        info = [i.text.strip() for i in info]
        nrc_idx = info.index(f'{nrc}')
        info = info[nrc_idx: nrc_idx + 21]
        # info = [info[21 * i:21 * (i + 1)] for i in range(len(info) // 21)]
        # info = info[sec - 1]  # Extraemos solo la info de la sección pedida
        name_ = info[9]
        T = int(info[13])
        disp = int(info[14])
        oc = T - disp
        esc = 'Vacantes Libres'
        vacxesc.update({esc: (oc + disp, oc, disp)})
    else:
        for esc, _, prog, conc, _, _, _, oc, disp in info:
            esc = esc[5:] if '-' in esc else esc
            if oc == disp == '0':
                continue
            if prog:  # Para los casos donde NO hay escuelas (Sin Vac. Libres)
                prog = prog.split('-')[1]
                vacxesc.update({prog: (int(oc) + int(disp), oc, disp)})
                continue
            if esc in vacxesc:
                conc = conc.split('-')[1]
                conc = conc.replace('Certificado Académico en', 'CA')
                vacxesc.update({conc: (int(oc) + int(disp), oc, disp)})
                continue
            if esc:
                vacxesc.update({esc: (int(oc) + int(disp), oc, disp)})
    df = pd.DataFrame(vacxesc).T
    df.rename(columns={0: 'T', 1: 'O', 2: 'D'}, inplace=True)

    return df, name_


def preprocessing(df):
    """Prepara los datos para ser usado por la librería Dash

    Parameters
    ----------
    df : pd.DataFrame
      Output de la función vacantes()

    Returns
    -------
    pd.DataFrame
      DataFrame listo para ser usado por px.Sunburst()
    """
    columns = ['Vacantes', 'Escuela', 'T_Vacante']
    data = []
    for tup in df.itertuples():
        esc, _, oc, disp = tup

        data.append([disp, esc, 'Disponible'])
        data.append([oc, esc, 'Ocupado'])
    return pd.DataFrame(data, columns=columns)


def run(sem, ramos, interval=60):
    """Inicia la consulta de vacantes.

    Parameters
    ----------
    sem : str
      Semestre en el que se toman ramos (ej: '2020-2')
    ramos : list
      Lista de diccionarios que contienen información de los ramos a
      consultar (ej: [{'nrc': 20437, 'sigla': 'ICS3105', 'sec': 1}, ...])
    interval : int
      Intervalo de tiempo en segundos
    """
    while True:
        clear()
        print(f"\n\033[1m{datetime.now().strftime('%H:%M:%S')}\033[0m\n")
        st = time()
        for ramo in ramos:
            nrc, sigla, seccion = ramo.values()
            vxe, nombre = vacantes(sem, nrc, sigla, seccion)
            print(f"\033[1m{sigla}-{seccion}\033[0m: {nombre}")
            print(vxe, end='\n' * 2)
        print(f"Finished! ({time() - st:3.1f} sec)")

        sleep(interval)


if __name__ == '__main__':
    semestre = '2020-2'
    ramos = [
        # {'nrc': 20437, 'sigla': 'ICS3105', 'sec': 1},
        {'nrc': 11114, 'sigla': 'DPT5502', 'sec': 3}
    ]
    for ramo in ramos:
        nrc, sigla, seccion = ramo.values()
        vxe, nombre = vacantes(semestre, nrc, sigla, seccion)
        print(f"{sigla}-{seccion}: {nombre}")
        print(vxe)
        # print(preprocessing(vxe))
