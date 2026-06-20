import socket
import threading
import sys

HOST, PORT = '127.0.0.1', 5000


def receber(conn):
    while True:
        try:
            dados = conn.recv(1024)

            if not dados:
                break

            print(dados.decode('utf-8'), end='', flush=True)

        except:
            break


if len(sys.argv) >= 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

threading.Thread(
    target=receber,
    args=(conn,),
    daemon=True
).start()

while True:
    entrada = input()

    if entrada.strip().lower() == '/sair':
        conn.sendall('/sair'.encode())
        break

    if entrada.strip():
        conn.sendall(entrada.encode('utf-8'))

conn.close()