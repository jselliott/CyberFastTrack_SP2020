# FM18
## Forensics (Medium)

![FM18](FM18.png)

This challenge requires you to load the **Evidence.E01** file provided for several of the challenges. This is a raw disk image from a Windows PC that we can examine to answer the questions.

For this, we can use Autopsy to create a case and attach the disk image using the web interface:

![FM18](FM18_1.png)
![FM18](FM18_2.png)

Next we can browse to the Steam directory and see what we can find in the logs at:

```C:/Programs Files (x86)/Steam/Logs```

![FM18](FM18_3.png)

In the content_log.txt file we can see the App ID of the game that was launched.

![FM18](FM18_4.png)

A quick google search reveals the correct answer: **adventure capitalist**
