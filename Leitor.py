
import serial
import time ## utilizado no delay
import mysql.connector
from datetime import datetime
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='automação_de_porta',
)
while True:
    cursor = conexao.cursor()
    comando = f'SELECT * FROM frequencia_lab Where tranca = 1 '
    cursor.execute(comando)
    resultado = cursor.fetchall()
    if resultado:
        comand = f'SELECT laboratorio FROM frequencia_lab  where  tranca = 1'
        cursor.execute(comand)
        results = cursor.fetchall()
        if results:
            porta = "COM3"
            velocidade = 9600
            comand = serial.Serial(porta, velocidade)
            for row in results:
                lab_ = row[0]
                if lab_ == 'lab_1':
                    print('Abrir a porta 1')
                    comand.write(b'A')
                    time.sleep(2)
                    comand.write(b'a')
                elif lab_ == 'lab_2':
                    print('Abrir a porta 2')
                    comand.write(b'B')
                    time.sleep(2)
                    comand.write(b'b')
                elif lab_ == 'lab_3':
                    print('abrir a porta 3')
                    comand.write(b'B')
                    time.sleep(2)
                    comand.write(b'b')
                elif lab_ == 'lab_4':
                    print('abrir a porta 4')
                    comand.write(b'C')
                    time.sleep(2)
                    comand.write(b'c')
                else:
                    print('lab não encontrado')
                break
            if resultado != 0:
                    coman = f'update frequencia_lab set tranca = 0'
                    cursor.execute(coman)
                    conexao.commit()
        else:
            print('resultado não encontrado')
    print(resultado)
    cursor.close()
    cursor.close()
    time.sleep(5)