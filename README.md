<h1 align="center">Sorry, Not My Fault!</h1>
🇺🇸/[🇷🇺](README.ru.md)
<hr>

SNMF! is an open-source replacement for [NotMyFault](https://learn.microsoft.com/ru-ru/sysinternals/downloads/notmyfault), designed for Linux.

## Available Methods:

- `sysrq` – triggers a kernel panic using SysRQ  
- `modulepanic` – triggers a kernel panic by loading a custom module with a `panic()` function  
- `modulebug` – triggers a kernel panic by loading a custom module with a `BUG()` function  

## Kernel Modules

In 2 out of 3 methods for triggering a kernel panic, a module is loaded into the system that causes the crash.

To build these modules, you need to go to the `modules` folder and run the following command in each subfolder:

```shell
make; sudo make install; make clean
```

After that, the modules will be ready to use.
