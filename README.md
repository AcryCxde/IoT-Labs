# IoT Fire Detection System

## Подключиться к MQTT клиенту:

- **Просмотр данных:** 
  ```bash
  mosquitto_sub -h test.mosquitto.org -t iot_lab1/smoke_level
  ```

- **Установка режима:**  
  - **Ручной:** 
    ```bash
    mosquitto_pub -h test.mosquitto.org -t "iot_lab1/mode" -m "manual"
    ```
  - **Автоматический:** 
    ```bash
    mosquitto_pub -h test.mosquitto.org -t "iot_lab1/mode" -m "auto"
    ```

- **Активация актуатора (доступна только в ручном режиме):** 
  ```bash
  mosquitto_pub -h test.mosquitto.org -t "iot_lab1/actuator" -m "activate"
  ```

## Запуск программы:
**Запустите исполняемый файл `main.py`.**

## Работа с Telegram-ботом:

Чтобы взаимодействовать с системой через Telegram, используйте бота с именем [@IoT_fire_detection_bot](https://t.me/IoT_fire_detection_bot).

### Порядок запуска:

1. **Запустите исполняемый файл `main.py`.**
2. **Запустите бота** командой `/start` в чате с ботом.
3. **Пользуйтесь доступными командами** в боте для управления системой.

### Доступные команды бота:

- `/start` - Главное меню.
- `/data` - Получить данные с устройства.
- `/manual` - Установить ручной режим.
- `/auto` - Установить автоматический режим.
- `/actuator` - Активировать актуатор (доступно только в ручном режиме).
