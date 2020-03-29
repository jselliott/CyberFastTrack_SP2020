# BX09
## Binary Exploit (Extreme)

![BX09](BX09.png)

This challenge is very unique because you have to actually boot up a homebrew OS and examine how it functions to discover the flag.

You can open the provided ISO image in an archive manager and see the kernel itself which can be opened up in IDA to examine how it functions.

![BX09_1](BX09_1.png)

Looking at the kernel code, nothing really stands out immediately. However, there are a series of interrupt handlers that we can see it accepting input from the keyboard. In the function **irq1_handler()**, we finally see a really good hint. There are several references to functions which include the word "konami". Anyone with nerd cred will immediately think of the famous "Konami Code", so let's give it a shot...

![BX09_2](BX09_2.png)

After creating a simple virtual machine in VirtualBox, and mounting the ISO in the virtual CD drive, we can finally boot up the OS and are presented with a simple screen, waiting for input.

![BX09_3](BX09_3.png)

Here we can enter the konami code on the keyboard: up up down down left right left right B A

This reveals the flag **PleaseDontInterruptMe**

![BX09_4](BX09_4.png)
