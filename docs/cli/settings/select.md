Эта команда позволяет включить или отключить параметр `--select` на сохранение своего состояния.

!!! info

    Когда эта опция активирована, вызов `--select` сохранит состояние, и в последующих вызовах без нее будет применяться сохраненный выбор.

#### Options

```shell
-e, --enable [true|false]  Включить/Выключить сохранение --select. [обязательно]
-v, --verbose              Подробный вывод.
--help                     Показать это сообщение и выйти.
```

#### Example

```shell
aurora-cli settings localization --language ru
```

!!! info

    Подробнее о дополнительных настройках можно ознакомиться в разделе [Settings](../../settings.md).