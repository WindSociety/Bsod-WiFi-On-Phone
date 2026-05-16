# Bsod-WiFi-On-Phone
en
Here is the full English instruction for your repository WindSociety/Bsod-WiFi-On-Phone.

---

📱💀 BSOD over WiFi – WindSociety Tool

📦 Repository Contents

· phone_client.py – runs on your phone (Termux). Sends commands to PC.
· pc_server.py – runs on Windows PC. Listens for commands and triggers BSOD.
· bsod_trigger.py – called by the server to actually cause the Blue Screen of Death.

---

🖥️ 1. PC Setup (Windows)

Requirements

· Windows 10/11 (real BSOD only works on Windows)
· Python 3 installed
· Phone and PC must be on the same Wi-Fi network

Installation on PC

1. Download or create these files in the same folder:
   · pc_server.py
   · bsod_trigger.py
2. Open Command Prompt as Administrator (important!).
3. Start the server:
   ```cmd
   python pc_server.py
   ```
   You should see: [*] Server listening on port 9999
4. Keep this window open – the server must stay running.

🔁 If Windows Firewall asks for permission, allow it.

---

📱 2. Phone Setup (Android + Termux)

Install Termux

· Download Termux from F-Droid (not Play Store – outdated).
· Open Termux and run:
  ```bash
  pkg update && pkg upgrade -y
  pkg install python -y
  ```

Get the script

Copy phone_client.py to your phone storage (e.g., Download folder).

In Termux, navigate to the script and run:

```bash
cd /storage/emulated/0/Download
python phone_client.py
```

If you get Permission denied, copy the script to Termux home folder:

```bash
cp /storage/emulated/0/Download/phone_client.py ~/
cd ~
python phone_client.py
```

Edit IP address

Before first run, edit phone_client.py and set your PC's local IP:

```python
SERVER_IP = '192.168.1.35'   # change to your PC's IPv4 address
```

To find PC IP: open cmd on PC, type ipconfig – look for IPv4 Address under your active network adapter (Wi‑Fi or Ethernet).

You can edit the file using any text editor on your phone or via nano inside Termux.

---

🚀 3. Running & Commands

1. On PC: pc_server.py is running (admin console).
2. On phone: phone_client.py is running.
3. Phone terminal shows > prompt.
4. Type /bsod and press Enter.
5. On PC, bsod_trigger.py executes → after a few seconds a Blue Screen of Death appears.

Other commands:

· /exit – close phone client.
· /help – show available commands.

---

⚠️ Important Warnings

· BSOD will restart your PC – save all work before testing.
· Run this only on a virtual machine if you are not prepared for data loss.
· bsod_trigger.py works only on Windows.
· PC and phone must be in the same network.
· If command fails: temporarily disable Windows Firewall and double-check IP address.
· Run pc_server.py as Administrator – otherwise BSOD won't trigger (insufficient privileges).

---

🔧 Troubleshooting

Error Solution
ConnectionRefusedError Server not running on PC, or wrong IP/port.
Permission denied in Termux Copy script to ~/ home folder and run from there.
BSOD does not appear Run pc_server.py and bsod_trigger.py manually as Admin. Windows Defender may block it.
No address associated with hostname Wrong PC IP address in phone_client.py.

---

🌐 Repository Link

🔗 https://github.com/WindSociety/Bsod-WiFi-On-Phone

You can add this as README.md to your repo. Need me to translate the code comments or any other part? Just ask.
ru
Полная инструкция по использованию репозитория WindSociety/Bsod-WiFi-On-Phone.

📦 Что внутри репозитория

· phone_client.py – запускается на телефоне (Termux). Отправляет команды.
· pc_server.py – запускается на ПК. Слушает команды, вызывает BSOD.
· bsod_trigger.py – вызывается сервером для реального синего экрана (Windows).

---

🖥️ 1. Настройка ПК (Windows)

Требования

· Windows 10/11 (только для реального BSOD)
· Python 3 установлен
· ПК и телефон в одной Wi-Fi сети

Установка на ПК

1. Скачай репозиторий или создай файлы вручную:
   · pc_server.py
   · bsod_trigger.py
2. Открой командную строку от имени администратора (важно!).
3. Запусти сервер:
   ```cmd
   python pc_server.py
   ```
   Должно появиться: [*] Server listening on port 9999
4. Не закрывай это окно – сервер работает.

🔁 Если антивирус или брандмауэр спросят разрешение – разреши.

---

📱 2. Настройка телефона (Android + Termux)

Установка Termux

· Скачай Termux с F-Droid (не с Play Market, там устаревшая версия).
· Открой Termux, выполни:
  ```bash
  pkg update && pkg upgrade -y
  pkg install python -y
  ```

Скачивание скрипта

Скопируй phone_client.py в память телефона (например, в папку Download).

В Termux перейди в папку со скриптом и запусти:

```bash
cd /storage/emulated/0/Download
python phone_client.py
```

Если ошибка Permission denied – скопируй скрипт в домашнюю папку Termux:

```bash
cp /storage/emulated/0/Download/phone_client.py ~/
cd ~
python phone_client.py
```

Редактирование IP-адреса

Перед первым запуском обязательно укажи IP своего ПК в phone_client.py:

```python
SERVER_IP = '192.168.1.35'   # замени на реальный IPv4-адрес ПК
```

Узнать IP ПК: ipconfig в cmd → строка "IPv4-адрес" в разделе Wi-Fi или Ethernet.

Изменить IP можно через любой текстовый редактор на телефоне или в Termux через nano.

---

🚀 3. Запуск и команды

1. На ПК запущен pc_server.py (окно не закрывай).
2. На телефоне запущен phone_client.py.
3. В терминале телефона появится приглашение >.
4. Введи команду /bsod и нажми Enter.
5. На ПК запустится bsod_trigger.py – через пару секунд появится синий экран смерти.

Другие команды:

· /exit – завершить клиент на телефоне.
· /help – список команд.

---

⚠️ Важные предупреждения

· BSOD вызывает перезагрузку ПК – сохраните все данные на ПК перед тестом.
· Запускайте систему только в виртуальной машине, если не готовы к риску потери данных.
· Скрипт bsod_trigger.py работает только на Windows.
· ПК и телефон должны быть в одной сети.
· Если команда не проходит – проверьте брандмауэр Windows (временно отключите) и IP-адрес.
· pc_server.py нужно запускать от имени администратора – иначе BSOD не сработает (не хватит привилегий).

---

🔧 Устранение неполадок

Ошибка Решение
ConnectionRefusedError Не запущен сервер на ПК или неверный IP/порт.
Permission denied в Termux Скопируй скрипт в домашнюю папку ~/ и запускай оттуда.
BSOD не происходит Запусти pc_server.py и bsod_trigger.py вручную от админа. Возможно, защитник Windows блокирует вызов.
No address associated with hostname Неверный IP-адрес ПК в phone_client.py.

---

🌐 Ссылка на репозиторий

🔗 https://github.com/WindSociety/Bsod-WiFi-On-Phone

Если хочешь, я могу добавить в репозиторий файл README.md с этой инструкцией, а также пример .bat для автозапуска сервера на ПК. Просто напиши.
