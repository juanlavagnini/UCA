import socket
import threading #Para poder crear procesos hijo
import datetime

#Creamos el socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("El socket se creo")
#Establecemos la conexion
my_socket.bind(('localhost', 6667))
print("Bind hecho")
#Ponemos el socket en modo escucha
my_socket.listen(1)
print("Socket en modo escucha")

def proceso_hijo(*args):
    conexion = args[0]   #El primer elemento de la lista args es el objeto de socket que representa la conexion de un cliente especifico
    addr = args[1]       #Idem pero segundo elemento a la direccion

    try:
        print("Conexion con {}.".format(addr))  #Imprimo la direccion de la conexion
        conexion.send("Servidor: Conectado con cliente".encode('UTF-8'))
        inicio = datetime.datetime.now()
        mensajeHoy = "Conexion del cliente a las " + inicio.strftime("%Y-%m-%d  %H:%M:%S")
        conexion.send(mensajeHoy.encode('UTF-8'))

        while True:
            data = conexion.recv(1024)
            print("Recibido: ", addr)
            if data:
                print("Enviando mensaje de vuelta al cliente")
                conexion.sendall(data)
            else:
                print("No hay mas datos", addr)
                break
            fin = datetime.datetime.now()
            duracion = fin - inicio
            segundos = duracion.total_seconds()
            mensajeFin = "La conexion duro: " + str(segundos) + " segundos."
            conexion.send(mensajeFin.encode('UTF-8'))
    finally:
        conexion.close()

while 1:
    conexion, addr = my_socket.accept()
    print("Data del cliente", addr)
    threading.Thread(target=proceso_hijo, args=(conexion, addr)).start()

#mensajeHoy = "Conexion del cliente a las " + diaHora.strftime("%Y-%m-%d  %H:%M:%S")
#conexion.send(mensajeHoy.encode())