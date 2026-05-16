import socket
import os

# === НАСТРОЙКИ (измени IP на свой) ===
SERVER_IP = '192.168.1.35'   # сюда введи IPv4-адрес своего ПК
SERVER_PORT = 9999
# ===================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def send_command(cmd):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(cmd.encode())
        response = s.recv(4096).decode()
        s.close()
        return response
    except Exception as e:
        return f"Error: {e}"

def main():
    clear()
    print("=== WindSociety Remote Control ===")
    print(f"Connected to {SERVER_IP}:{SERVER_PORT}")
    print("Commands: /bsod, /exit, /help")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "/exit":
            print("Bye.")
            break
        elif cmd == "/help":
            print("Available commands: /bsod, /exit, /help")
        elif cmd == "/bsod":
            print(send_command("/bsod"))
        else:
            print("Unknown command. Type /help")

if __name__ == "__main__":
    main()
