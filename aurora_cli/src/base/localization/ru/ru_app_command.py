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


class TextCommandRu(Enum):
    @staticmethod
    def command_build_flutter():
        return 'Сборка проекта Flutter для ОС Aurora.'

    @staticmethod
    def command_build_qt():
        return 'Сборка проекта Qt для ОС Aurora.'

    @staticmethod
    def command_debug_dart():
        return 'Отладка Dart для ОС Aurora.'

    @staticmethod
    def command_debug_gdb():
        return 'Отладка GDB для ОС Аврора.'

    @staticmethod
    def command_device_command():
        return 'Выполните команду на устройстве.'

    @staticmethod
    def command_device_upload():
        return 'Загрузите файл в каталог ~/Download устройства.'

    @staticmethod
    def command_device_package_run():
        return 'Запустите пакет на устройстве в контейнере.'

    @staticmethod
    def command_device_package_install():
        return 'Установите пакет RPM на устройство.'

    @staticmethod
    def command_device_package_remove():
        return 'Удалите пакет RPM с устройства.'

    @staticmethod
    def command_emulator_start():
        return 'Запустите эмулятор.'

    @staticmethod
    def command_emulator_screenshot():
        return 'Сделать скриншот эмулятора.'

    @staticmethod
    def command_emulator_recording():
        return 'Запись видео с эмулятора.'

    @staticmethod
    def command_emulator_command():
        return 'Выполните команду на эмуляторе.'

    @staticmethod
    def command_emulator_upload():
        return 'Загрузите файл в каталог ~/Download эмулятора.'

    @staticmethod
    def command_emulator_package_run():
        return 'Запустите пакет на эмуляторе в контейнере.'

    @staticmethod
    def command_emulator_package_install():
        return 'Установите пакет RPM на эмулятор.'

    @staticmethod
    def command_emulator_package_remove():
        return 'Удалите пакет RPM с эмулятора.'

    @staticmethod
    def command_flutter_available():
        return 'Получите доступные версии Flutter для ОС Аврора.'

    @staticmethod
    def command_flutter_installed():
        return 'Получите версии установленных Flutter для ОС Аврора.'

    @staticmethod
    def command_flutter_install():
        return 'Загрузите и установите Flutter для ОС Аврора.'

    @staticmethod
    def command_flutter_remove():
        return 'Удалите Flutter для ОС Аврора.'

    @staticmethod
    def command_flutter_plugins_report():
        return 'Составить отчет по платформо-зависимым плагинам проекта Flutter.'

    @staticmethod
    def command_psdk_available():
        return 'Получить список доступных версий Аврора Platform SDK.'

    @staticmethod
    def command_psdk_installed():
        return 'Получите список установленных Аврора Platform SDK.'

    @staticmethod
    def command_psdk_install():
        return 'Загрузите и установите Аврора Platform SDK.'

    @staticmethod
    def command_psdk_remove():
        return 'Удалить Аврора Platform SDK.'

    @staticmethod
    def command_psdk_clear():
        return 'Удалить снапшоты таргетов.'

    @staticmethod
    def command_psdk_package_search():
        return 'Найдите установленный пакет в таргете.'

    @staticmethod
    def command_psdk_package_install():
        return 'Установите пакеты RPM в таргет.'

    @staticmethod
    def command_psdk_package_remove():
        return 'Удалить пакет из таргета.'

    @staticmethod
    def command_psdk_sign():
        return 'Подписать пакет RPM ключевой парой (с переподпиской).'

    @staticmethod
    def command_psdk_sudoers_add():
        return 'Добавьте разрешения sudoers Аврора Platform SDK.'

    @staticmethod
    def command_psdk_sudoers_remove():
        return 'Удалите разрешения sudoers Аврора Platform SDK.'

    @staticmethod
    def command_psdk_targets():
        return 'Получить список таргетов Аврора Platform SDK.'

    @staticmethod
    def command_psdk_validate():
        return 'Валидация пакетов RPM.'

    @staticmethod
    def command_sdk_available():
        return 'Получите доступные версии Аврора SDK.'

    @staticmethod
    def command_sdk_installed():
        return 'Получите версию установленной Аврора SDK.'

    @staticmethod
    def command_sdk_install():
        return 'Загрузите и запустите установку Аврора SDK.'

    @staticmethod
    def command_sdk_tool():
        return 'Запустите инструмент обслуживания (удаление, обновление).'

    @staticmethod
    def command_sundry_format_dart():
        return 'Форматирование проекта Dart по условиям платформы Flutter для ОС Аврора.'

    @staticmethod
    def command_sundry_format_clang():
        return 'Форматирование проекта С++ по условиям платформы Flutter для ОС Аврора.'

    @staticmethod
    def command_sundry_image_sizes():
        return 'Генерируйте значки разных размеров для приложений.'