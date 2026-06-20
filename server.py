import socket
import threading

HOST, PORT = '0.0.0.0', 5000

clientes = []
lock = threading.Lock()


def broadcast(mensagem, remetente_conn=None):
    with lock:
        for conn, addr, apelido in clientes:
            if conn != remetente_conn:
                try:
                    conn.sendall(mensagem.encode('utf-8'))
                except:
                    pass


def handle_client(conn, addr):
    conn.sendall("Digite seu apelido: ".encode('utf-8'))

    apelido = conn.recv(1024).decode('utf-8').strip() or str(addr)

    with lock:
        clientes.append((conn, addr, apelido))

    broadcast(f"[Servidor] {apelido} entrou no chat!", conn)

    conn.sendall(
        f"[Servidor] Bem-vindo, {apelido}! /sair para sair.\n".encode()
    )

    try:
        while True:
            dados = conn.recv(1024)

            if not dados:
                break

            msg = dados.decode('utf-8').strip()

            if msg.lower() == '/sair':
                break

            texto = f"[{apelido}]: {msg}"

            broadcast(texto, conn)
            conn.sendall((texto + "\n").encode('utf-8'))

    except ConnectionResetError:
        pass

    finally:
        with lock:
            clientes[:] = [
                (c, a, n)
                for c, a, n in clientes
                if c != conn
            ]

        broadcast(f"[Servidor] {apelido} saiu do chat.")
        conn.close()


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servidor.bind((HOST, PORT))
servidor.listen(10)

print(f"Servidor TCP em {HOST}:{PORT}")

while True:
    conn, addr = servidor.accept()

    threading.Thread(
        target=handle_client,
        args=(conn, addr),
        daemon=True
    ).start()