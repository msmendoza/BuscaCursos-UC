from functions import run

semestre = '2020-2'
ramos = [
    # Major/Título
    {'nrc': 20437, 'sigla': 'ICS3105', 'sec': 1},  # Opti Dinámica
    # A
    {'nrc': 13579, 'sigla': 'ICS3413', 'sec': 1},  # Finanzas
    # B
    {'nrc': 12357, 'sigla': 'IIC2133', 'sec': 1},  # EDD 1
    {'nrc': 24358, 'sigla': 'IIC2133', 'sec': 2},  # EDD 2

    # OFGs
    # A
    {'nrc': 17865, 'sigla': 'CAR1500', 'sec': 1},  # Ent Presentaciones O.
    {'nrc': 12426, 'sigla': 'LET056E', 'sec': 1},  # Catalan
    {'nrc': 20536, 'sigla': 'LET218E', 'sec': 1},  # Lit Japonesa

    # B
    {'nrc': 13477, 'sigla': 'CAR0004', 'sec': 1},  # Taller Tutores
    {'nrc': 14518, 'sigla': 'GEO111', 'sec': 1},  # Geografía de Chile: E y S

    # C


    # Ya tomado
    # {'nrc': 15993, 'sigla': 'MUC1000', 'sec': 1},
    # {'nrc': 14352, 'sigla': 'ICS2813', 'sec': 1},
    # {'nrc': 16922, 'sigla': 'ICS2122', 'sec': 1},

]

if __name__ == '__main__':
    run(semestre, ramos, interval=60)
    pass
