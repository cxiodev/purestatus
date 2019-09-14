# purestatus
Кастомизируемый динамический статус для вашего профиля ВКонтакте.
TODO: Облизать код!
## Установка
### Windows
1. Установи Python 3.7
2. Установи git
```
git clone https://github.com/newpotsdev/purestatus
cd purestatus
py -m pip install -r requirements.txt
```
### Linux
1. Выполните команду:
```
sudo apt-get update && sudo apt-get install python3.7 && sudo apt-get install git && git clone https://github.com/newpotsdev/purestatus && cd purestatus && python3 -m pip install -r requirements
```
## Настройка
В файле configuration.json содержится JSON текст которым вы можете настроить ПО.
### Документация конфигураций
| Опция                    | Тип           | Описание                          |
| ------------------------ | ------------- | --------------------------------- |
| token                    | string        | Токен вашего аккаунта ВК          |
| status_pattern           | string        | Строка статуса                    |
| time_pattern             | string        | Настройка вывода времени          |
| timezone                 | string        | Тайм-зона                         |
| lifetime_online_settings | dict          | Настройка вечного онлайна         |

## Запуск
```
python purestatus.py
```
