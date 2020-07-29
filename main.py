from datetime import datetime
from time import time, sleep

from functions import vacantes, clear

base_url = 'http://buscacursos.uc.cl'
ramos = [
    {'sigla': 'CAR1500',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=17865"
            "&termcode=2020-2"
            "&cantidad_dis=9"
            "&cantidad_min=12"
            "&cantidad_ocu=3"
            "&nombre=Entrenamiento+en+Presentaciones+Orales+Efectivas"
            "&sigla=CAR1500"
            "&seccion=1"},
    {'sigla': 'ICS2122',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=16922"
            f"&termcode=2020-2"
            "&cantidad_dis=100"
            "&cantidad_min=100"
            "&cantidad_ocu=0"
            "&nombre=Taller+de+Investigaci%C3%B3n+Operativa"
            "+%28Capstone%29"
            f"&sigla=ICS2122"
            f"&seccion=1"},
    {'sigla': 'ICS2813',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=14352"
            "&termcode=2020-2"
            "&cantidad_dis=127"
            "&cantidad_min=130"
            "&cantidad_ocu=3"
            "&nombre=Organizaci%C3%B3n+y+Comportamiento+en+la+Empresa"
            "&sigla=ICS2813"
            "&seccion=1"},
    {'sigla': 'ICS3105',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=20437"
            "&termcode=2020-2"
            "&cantidad_dis=39"
            "&cantidad_min=40"
            "&cantidad_ocu=1"
            "&nombre=Optimizaci%C3%B3n+Din%C3%A1mica"
            "&sigla=ICS3105"
            "&seccion=1"},
    {'sigla': 'ICS3413',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=13579"
            "&termcode=2020-2"
            "&cantidad_dis=148"
            "&cantidad_min=150"
            "&cantidad_ocu=2"
            "&nombre=Finanzas"
            "&sigla=ICS3413"
            "&seccion=1"},
    {'sigla': 'LET056E',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=12426"
            "&termcode=2020-2"
            "&cantidad_dis=30"
            "&cantidad_min=30"
            "&cantidad_ocu=0"
            "&nombre=Introduccion+a+la+Lengua+y+Cultura+Catalana"
            "&sigla=LET056E"
            "&seccion=1"},
    {'sigla': 'LET218E',
     'sec': 1,
     'url': f"{base_url}/informacionVacReserva.ajax.php"
            "?nrc=20536"
            "&termcode=2020-2"
            "&cantidad_dis=27"
            "&cantidad_min=30"
            "&cantidad_ocu=3"
            "&nombre=Literatura+Japonesa"
            "&sigla=LET218E"
            "&seccion=1"}
]


def run():
    clear()

    print(f"\n\033[1m{datetime.now().strftime('%H:%M:%S')}\033[0m\n")
    st = time()
    for ramo in ramos:
        sigla, sec, url = ramo.values()
        vxe_ramo = vacantes(url)
        print(f"\033[1m{sigla}-{sec}\033[0m")
        print(vxe_ramo, end='\n' * 2)
    print(f"Finished! ({time() - st:3.1f} sec)")


while True:
    run()
    sleep(30)
