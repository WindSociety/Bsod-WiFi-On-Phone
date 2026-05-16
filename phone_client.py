import socket

# === НАСТРОЙКИ ===
SERVER_IP = '192.168.1.XX'   # ЗДЕСЬ УКАЖИ IP ТВОЕГО КОМПЬЮТЕРА
SERVER_PORT = 9999
# ================

def send_command(cmd):
    """Отправляет команду на сервер и выводит ответ"""
    try:
        # Создаем сокет и устанавливаем соединение
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            print(f"[*] Отправка: {cmd}")
            s.sendall(cmd.encode('utf-8'))
            
            # Получаем ответ от сервера
            response = s.recv(4096).decode('utf-8')
            print(f"[+] Ответ: {response}")
    except ConnectionRefusedError:
        print("[-] Ошибка: Сервер не найден. Убедись, что сервер запущен, а IP и порт указаны верно.")
    except Exception as e:
        print(f"[-] Ошибка: {e}")

if __name__ == "__main__":
    print("Управление ПК через Termux")
    print("Введите /help для списка команд или /exit для выхода.")
    
    while True:
        # Получаем команду от пользователя
        user_input = input("> ").strip()
        
        if user_input.lower() == "/exit":
            print("Выход.")
            break
        elif user_input.lower() == "/help":
            print("Доступные команды: /bsod, /exit, /help")
        else:
            # Отправляем команду на сервер
            send_command(user_input)