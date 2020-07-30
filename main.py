from functions import run

semestre = '2020-2'
ramos = [
    {'nrc': 17865, 'sigla': 'CAR1500', 'sec': 1},
    {'nrc': 16922, 'sigla': 'ICS2122', 'sec': 1},
    {'nrc': 14352, 'sigla': 'ICS2813', 'sec': 1},
    {'nrc': 20437, 'sigla': 'ICS3105', 'sec': 1},
    {'nrc': 13579, 'sigla': 'ICS3413', 'sec': 1},
    {'nrc': 12426, 'sigla': 'LET056E', 'sec': 1},
    {'nrc': 20536, 'sigla': 'LET218E', 'sec': 1}
]

run(semestre, ramos, interval=60)
