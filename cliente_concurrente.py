import socket
import time

#Creo el socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado")
#Conecto al servidor
my_socket.connect(('localhost',6667))
print("Conexion establecida")

contador = 0
while contador<1:
    #Enviamos datos
    print("Contador: ", contador)
    datos = my_socket.recv(1024)
    print(datos.decode('utf-8'))
    mensaje = 'Hola Soy el Cliente 1'
    print("Enviando: ", mensaje)
    time.sleep(5)
    my_socket.sendall(mensaje.encode())

    bytes_recibidos = 0
    bytes_esperados = len(mensaje)

    fecha = my_socket.recv(2048)
    print("Fecha: ", fecha.decode('UTF-8'))

    while bytes_recibidos<bytes_esperados:
        data = my_socket.recv(2048)
        bytes_recibidos += len(data)
        print("Recibiendo del servidor: ", data)

    tiempo = my_socket.recv(1024)
    print("Tiempo: ", tiempo.decode('UTF-8'))

    contador = contador+1

print("Cerrando socket")
my_socket.close()


