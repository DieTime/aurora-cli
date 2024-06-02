"""
Copyright 2024 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from enum import Enum


class TextErrorRu(Enum):
    @staticmethod
    def shell_exec_command_empty():
        return '<red>Ошибка чтения аргументов оболочки.</red>'

    @staticmethod
    def emulator_not_found():
        return '<red>Эмулятор с ОС Аврора не найден.</red>'

    @staticmethod
    def emulator_not_found_running():
        return '<red>Ни одного работающего эмулятора с ОС Аврора не обнаружено.</red>'

    @staticmethod
    def emulator_start_error():
        return '<red>Не удалось запустить эмулятор.</red>'

    @staticmethod
    def emulator_path_not_found():
        return '<red>Не удалось найти путь к эмулятору.</red>'

    @staticmethod
    def route_not_found():
        return '<red>Маршрут не найден.</red>'

    @staticmethod
    def emulator_screenshot_error():
        return '<red>Не удалось сделать скриншот.</red>'

    @staticmethod
    def emulator_already_running_recording():
        return '<red>Эмулятор записи видео уже включен.</red>'

    @staticmethod
    def emulator_not_running_recording():
        return '<red>Не удалось запустить запись видео.</red>'

    @staticmethod
    def emulator_recording_video_start_error():
        return '<red>Не удалось активировать запись видео.</red>'

    @staticmethod
    def emulator_recording_video_stop_error():
        return '<red>Не удалось отключить запись видео.</red>'

    @staticmethod
    def emulator_recording_video_file_not_found():
        return '<red>Не удалось найти файл видеозаписи.</red>'

    @staticmethod
    def emulator_recording_video_convert_error():
        return '<red>Не удалось преобразовать видеозапись.</red>'

    @staticmethod
    def ssh_connect_emulator_error():
        return '<red>Ошибка подключения к эмулятору через SSH.</red>'

    @staticmethod
    def ssh_connect_device_error():
        return '<red>Ошибка подключения к устройству через SSH.</red>'

    @staticmethod
    def ssh_run_application_error(package: str):
        return f'<red>При запуске приложения произошла ошибка:</red> {package}'

    @staticmethod
    def ssh_upload_error():
        return '<red>Не удалось загрузить файлы.</red>'

    @staticmethod
    def ssh_upload_file_not_found(path: str):
        return f'<red>Файл для загрузки не найден:</red> {path}'

    @staticmethod
    def ssh_install_rpm_error():
        return '<red>Ошибка установки пакета RPM.</red>'

    @staticmethod
    def ssh_remove_rpm_error():
        return '<red>Произошла ошибка при удалении пакета.</red>'

    @staticmethod
    def validate_config_error():
        return '<red>Файл конфигурации не прошел валидацию.</red>'

    @staticmethod
    def validate_config_devices_not_found():
        return '<red>Раздел</red> devices <red>не найден.</red>'

    @staticmethod
    def validate_config_devices():
        return '<red>Раздел</red> devices <red>неправильный.</red>'

    @staticmethod
    def validate_config_keys_not_found():
        return '<red>Раздел</red> keys <red>не найден.</red>'

    @staticmethod
    def validate_config_keys():
        return '<red>Раздел</red> keys <red>неправильный.</red>'

    @staticmethod
    def validate_config_key_not_found(path: str):
        return f'<red>Не найден файла ключа:</red> {path}'

    @staticmethod
    def validate_config_cert_not_found(path: str):
        return f'<red>Не найден файл сертификата:</red> {path}'

    @staticmethod
    def validate_config_workdir_not_found():
        return '<red>Не удалось найти и создать</red> workdir <red>директорию.</red>'

    @staticmethod
    def validate_config_workdir_error_create(path: str):
        return f'<red>Директория</red> {path} <red>не найдена.</red>'

    @staticmethod
    def validate_config_arg_path(path: str):
        return f'<red>Указанный файл конфигурации не существует:</red> {path}'

    @staticmethod
    def config_arg_path_load_error(path: str):
        return f'<red>Чтение файла конфигурации завершился с ошибкой:</red> {path}'

    @staticmethod
    def index_error():
        return '<red>Введен неверный индекс.</red>'

    @staticmethod
    def index_and_select_at_the_same_time():
        return '<red>Выберите один аргумент</red> --select <red>или</red> --index<red>.</red>'

    @staticmethod
    def dependency_not_found(dependency: str):
        return f'<red>Зависимость</red> {dependency} <red>не найдена и необходима для запуска этой команды.</red>'

    @staticmethod
    def request_error():
        return '<red>Ошибка подключения к интернету. Проверьте соединение.</red>'

    @staticmethod
    def request_empty_error():
        return '<red>Запрос дал пустой результат. Произошла ошибка...</red>'

    @staticmethod
    def just_empty_error():
        return '<yellow>Ничего не найдено.</yellow>'

    @staticmethod
    def config_value_empty_error():
        return '<yellow>Не найдены элементы для выбора, проверьте конфигурационный файл.</yellow>'

    @staticmethod
    def flutter_not_found_error():
        return '<red>Не найдено: Flutter SDK.</red>'

    @staticmethod
    def psdk_not_found_error():
        return '<red>Не найдено: Аврора Platform SDK.</red>'

    @staticmethod
    def sdk_not_found_error():
        return '<red>Не найдено: Аврора SDK.</red>'

    @staticmethod
    def sdk_already_installed_error():
        return '<red>Аврора SDK уже установлено.</red>'

    @staticmethod
    def device_not_found_error(host: str):
        return f'<red>Не найдено: Устройство. Host: </red> {host}'

    @staticmethod
    def sign_not_found_error(name: str):
        return f'<red>Не найдено: Ключи подписи. Название: </red> {name}'

    @staticmethod
    def shell_run_app_error(name: str):
        return f'<red>Не удалось запустить приложение:</red> {name}'
