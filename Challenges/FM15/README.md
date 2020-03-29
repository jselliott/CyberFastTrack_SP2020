# FM15
## Forensics (Medium)

![FM15](FM15.png)

This challenge requires you to load the **Evidence.E01** file provided for several of the challenges. This is a raw disk image from a Windows PC that we can examine to answer the questions.

For this, we can use Autopsy to create a case and attach the disk image using the web interface:

![FM15](FM15_1.png)
![FM15](FM15_2.png)

After we have mounted the image, we can see the a windows file structure. If we believe that the user downloaded a file, then we would obviously want to start by examining his documents folders. This search leads us to:

`C:/Users/agency_worker_1337/Documents/Work/Plutonium Rhombus/`

Where we see an image file, along with a Zone.Identifier file which identifies what "zone" a file came from for security purposes in Windows. Clicking on the file, it reveals that the image was downloaded from a remote server, and lists the location.

![FM15](FM15_3.png)

This location **\\192.168.16.18\internal_only\CEO\Private** can be submitted for credit.
