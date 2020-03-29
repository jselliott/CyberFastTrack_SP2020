# FH10
## Forensics (Hard)

![FH10](FH10.png)

This challenge requires you to load the **Evidence.E01** file provided for several of the challenges. This is a raw disk image from a Windows PC that we can examine to answer the questions.

For this, we can use Autopsy to create a case and attach the disk image using the web interface:

![FH10](FH10_1.png)

After we have mounted the image, we can see the a windows file structure. 

![FH10](FH10_2.png)

A good place to start when searching for applications that have been used by a user is in their AppData folder. A quick look reveals that the user has KeyBase, a chat application.

`C:/Users/agency_worker_1337/AppData/Roaming/Keybase/Cache/`

![FH10](FH10_3.png)

Inside this cache folder, we can see images that were sent in messages dispite the messages themselves being encrypted. In one of the images, we see the flag.

![FH10](FH10_4.jpg)
