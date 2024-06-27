Приложение доступно на [PyPi](https://test.pypi.org/project/aurora-cli/).
Менеджер пакетов `pip` доступен на большинстве дистрибутивов Linux.

!!! info

    На данный момент приложение 3й версии размещено на `test.pypi.org`.
    Когда оно стабилизируется будет выложено, как основная версия.

Установка приложения доступна на дистрибутивах с наличием Python `3.8.10+` версии.
Была проверена на Ubuntu `20.04` & ALT Linux `10`, разработка ведется на `22.04`.
На Ubuntu `22.04` работает без дополнительных манипуляций с установкой, на других дистрибутивах возможны нюансы.


#### Ubuntu 22.04+

```shell
sudo apt update
sudo apt install python3-pip

python3 -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple aurora-cli
```

#### Ubuntu 20.04

```shell
sudo apt update
sudo apt install python3-pip
sudo apt install libpangocairo-1.0-0

python3 -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple aurora-cli
```

#### ALT Linux 10

```shell
su -
apt-get update
apt-get install sudo
control sudowheel enabled
exit
```

```shell
sudo apt-get install pip
sudo apt-get install python3-modules-sqlite3

python3 -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple aurora-cli
```

#### Dependencies

Для работы всех компонентов приложения требуются следующие зависимости:

- `sudo` - Platform SDK требует наличе `sudo`.
- `git` - Flutter SDK клонируется из репозитория.
- `git-lfs` - Подтянет большие файлы, если такие будут.
- `ssh` - Подключение к устройствам и эмулятору происходит по SSH.
- `curl` - Требуется для работы Flutter SDK.
- `tar` - Установка Platform SDK происходит из архива.
- `unzip` - Нужна для распаковки архивов.
- `bzip2` - Нужна для распаковки архивов.
- `ffmpeg` - Конвертация формата `webm` в человеческий `mp4`.
- `vscode` - Есть методы, помогающие работе с VS Code.
- `clang-format` - Форматирование С++ кода.
- `gdb-multiarch` - Позволяет запускать отладку С++ для приложений Flutter.
- `virtualbox` - Эмулятор работает через него, необходим для установки эмулятора.