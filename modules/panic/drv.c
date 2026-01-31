#include <linux/module.h>
#include <linux/kernel.h>

static int __init panic_init(void)
{
    panic("sorry, not my fault!");
    return 0;
}

static void __exit panic_exit(void)
{
}

module_init(panic_init);
module_exit(panic_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("msh356");
MODULE_DESCRIPTION("SNMF modulepanic");
