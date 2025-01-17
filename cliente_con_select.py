import socket
import sys

mensajes = [
    'Este mensaje ',
    'es enviado ',
    'en partes.',
]
dir_servidor = ('localhost', 10016)

# Creo socket
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

#conectar el socket al puerto en el cual el servidor está escuchando
print('conectando a {} puerto {}'.format(*dir_servidor),
      file=sys.stderr)
for s in socks:
    s.connect(dir_servidor)
for mensaje in mensajes:
    datos_salientes = mensaje.encode()

    # envío mensajes en ambos sockets
    for s in socks:
        try:
            print('{}: enviando {!r}'.format(s.getsockname(), datos_salientes), file=sys.stderr)
            s.send(datos_salientes)
        except:
            print("este socket esta cerrado")

    # leo respuestas en ambos sockets
    for s in socks:
            try:
                data = s.recv(1024)
                print('{}: recibido {!r}'.format(s.getsockname(),data),file=sys.stderr)
            except:
                print('cerrando socket', s.getsockname(),file=sys.stderr)
                s.close()