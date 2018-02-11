#!/usr/bin/python3
"""
Ejercicio URLS Aleatorias: Programa que funciona como Server.
Debe saludar y mostrar un enlace, que nos llevará a la misma 
página pero con una URL distinta genereda aleatoriamente.

Juan Ureña
j.urenag@alumnos.urjc.es
SAT(URJC)
"""
#Importamos paquetes necesarios

import socket
import random

#Creamos TCP socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Comprobamos si está en uso el puerto
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Atamos al puerto
name=socket.gethostname()
mySocket.bind((name, 1235))

#Fijamos número máximo de usuarios a 5
mySocket.listen(5)

#Estamos listos para recibir solicitudes

#Parte Principal

try:
    while True:
#Genero URL aleatoria
        nextNum = random.randrange(999999999)
        nextUrl = 'http://'+name+':1235/' + str(nextNum)
#Recibo mensaje
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
#Envio mensaje
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hola. <a href='" +
                        bytes(nextUrl, 'utf-8') +
                        b"'>Dame otra<a/>" +
                        b"</body></h1></html>" +
                        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
