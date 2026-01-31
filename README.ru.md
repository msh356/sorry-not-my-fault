<h1 align="center">Sorry, Not My Fault!</h1>

<hr>

SNMF! - это открытая замена [NotMyFault](https://learn.microsoft.com/ru-ru/sysinternals/downloads/notmyfault), предназначенная для Linux

## Доступные методы:

- `sysrq` - вызывает kernel panic, используя SysRQ
- `modulepanic` - вызывает kernel panic, подгружая собственный модуль с функцией `panic()`
- `modulebug` - вызывает kernel panic, подгружая собственный модуль с функцией `BUG()`

## Модули ядра

В 2 из 3 способов вызова kernel panic в систему подгружается модуль, вызывающий краш.

Для сборки этих модулей, вы должны перейти в папку modules и в каждой папке выполнить следующую команду:

```shell
make; sudo make install; make clean
```

После этого, модули начнут работать
