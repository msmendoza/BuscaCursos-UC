from functions import run

semestre = '2021-1'
ramos = [
    # Pregrado
    {'nrc': 15218, 'sigla': 'ICS3313', 'sec': 3},
    {'nrc': 10207, 'sigla': 'IHI2315', 'sec': 1},
    {'nrc': 10725, 'sigla': 'IIC2133', 'sec': 1},
    {'nrc': 10732, 'sigla': 'IIC2143', 'sec': 1},
]

if __name__ == '__main__':
    run(semestre, ramos, interval=60)
