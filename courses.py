from functions import run

semestre = '2021-1'
ramos = [
    # Pregrado
    # {'nrc': 15218, 'sigla': 'ICS3313', 'sec': 3},
    # {'nrc': 10207, 'sigla': 'IHI2315', 'sec': 1},
    # {'nrc': 10725, 'sigla': 'IIC2133', 'sec': 1},
    {'nrc': 10732, 'sigla': 'IIC2143', 'sec': 1},

    # Práctica II
    # {'nrc': 24183, 'sigla': 'ING2005', 'sec': 1},
    # {'nrc': 11844, 'sigla': 'ING2001', 'sec': 1},

    # Magíster
    {'nrc': 18871, 'sigla': 'IIC3697', 'sec': 1},
    {'nrc': 10930, 'sigla': 'IIC3724', 'sec': 1},
    {'nrc': 11856, 'sigla': 'ING4921', 'sec': 1},
]

if __name__ == '__main__':
    run(semestre, ramos, interval=60)
