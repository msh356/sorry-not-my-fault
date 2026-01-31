obj-m := drv.o
PWD := $(shell pwd)
KDIR := /lib/modules/$(shell uname -r)/build

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

install:
	mkdir -p /lib/modules/$(shell uname -r)/extra
	cp drv.ko /lib/modules/$(shell uname -r)/extra/snmf_panic.ko
	depmod -a

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
