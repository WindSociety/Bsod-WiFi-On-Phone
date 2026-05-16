#🌐 Bilingual Tutorial: PC + Phone

🇷🇺 Русская версия

Требования

· ПК: Windows 10/11, Python 3, права администратора.
· Телефон: Android, Termux (скачать с F-Droid), Wi-Fi (общая сеть с ПК).

📱 Настройка телефона (Termux)

1. Установи необходимые пакеты:
   ```bash
   pkg update -y && pkg upgrade -y
   pkg install python git -y
   ```
2. Склонируй репозиторий:
   ```bash
   cd ~
   git clone https://github.com/WindSociety/Bsod-WiFi-On-Phone.git
   cd Bsod-WiFi-On-Phone
   ```
3. Отредактируй phone_client.py, указав IP своего ПК:
   ```bash
   nano phone_client.py
   ```
   Измени строку SERVER_IP = '192.168.1.XX' (IP можно узнать на ПК командой ipconfig).
      Сохрани: Ctrl+O, Enter, Ctrl+X.
4. Запусти клиент:
   ```bash
   python phone_client.py
   ```
   Появится приглашение >. Доступные команды: /bsod, /exit, /help.

🖥️ Настройка ПК (Windows)

1. Скачай или создай файлы pc_server.py и bsod_trigger.py в одной папке (например, C:\WindSociety).
2. Открой командную строку от имени администратора и запусти сервер:
   ```cmd
   cd C:\WindSociety
   python pc_server.py
   ```
3. Сервер начнёт слушать порт 9999. Не закрывай это окно.

🚀 Запуск и проверка

· На ПК запущен pc_server.py.
· На телефоне запущен phone_client.py.
· Введи /bsod на телефоне → через несколько секунд на ПК появится синий экран смерти.

⚠️ Важно

· BSOD перезагружает ПК – сохраните данные.
· Используйте только на виртуальной машине, если не готовы к риску.
· ПК и телефон должны быть в одной сети.
· Запускайте сервер от администратора.

🔧 Возможные проблемы

Ошибка Решение
ConnectionRefusedError Сервер не запущен или неверный IP.
Permission denied (Termux) Клонируй репозиторий в ~/ (мы так и сделали).
BSOD не происходит Запусти pc_server.py и bsod_trigger.py вручную от админа, проверь брандмауэр.
No address associated with hostname Неверный IP ПК в phone_client.py.

---

🇬🇧 English version

Requirements

· PC: Windows 10/11, Python 3, Administrator rights.
· Phone: Android, Termux (from F-Droid), Wi-Fi (same network as PC).

📱 Phone setup (Termux)

1. Install required packages:
   ```bash
   pkg update -y && pkg upgrade -y
   pkg install python git -y
   ```
2. Clone the repository:
   ```bash
   cd ~
   git clone https://github.com/WindSociety/Bsod-WiFi-On-Phone.git
   cd Bsod-WiFi-On-Phone
   ```
3. Edit phone_client.py with your PC’s IP address:
   ```bash
   nano phone_client.py
   ```
   Change SERVER_IP = '192.168.1.XX' (find PC IP via ipconfig on Windows).
      Save: Ctrl+O, Enter, Ctrl+X.
4. Run the client:
   ```bash
   python phone_client.py
   ```
   Commands: /bsod, /exit, /help.

🖥️ PC setup (Windows)

1. Create or download pc_server.py and bsod_trigger.py in a folder (e.g. C:\WindSociety).
2. Open Command Prompt as Administrator and start the server:
   ```cmd
   cd C:\WindSociety
   python pc_server.py
   ```
3. The server will listen on port 9999. Keep this window open.

🚀 Run & test

· PC server is running (pc_server.py).
· Phone client is running (phone_client.py).
· Type /bsod on phone → after a few seconds, the PC will show a Blue Screen of Death.

⚠️ Important

· BSOD will restart your PC – save all work.
· Use only on a virtual machine if you are not ready for data loss.
· PC and phone must be on the same Wi-Fi network.
· Run the server as Administrator.

🔧 Troubleshooting

Error Solution
ConnectionRefusedError Server not running or wrong IP.
Permission denied (Termux) Clone to ~/ as shown.
BSOD does not happen Run pc_server.py and bsod_trigger.py manually as Admin, check firewall.
No address associated with hostname Wrong PC IP in phone_client.py.

---

🔗 Repository: https://github.com/WindSociety/Bsod-WiFi-On-Phone

You can copy this entire block as README.md into your repo. It contains both languages – just leave it as is.
