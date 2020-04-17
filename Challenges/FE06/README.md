# FE06
## Forensics (Hard)

![FE06](FE06.png)

* [FE06.jpg](FE06.jpg)

For this challenge we are provided with a JPEG image of a locked trunk along with a hint in the form of the "dollmaker" reference. This seems to refer to the famous Russian nesting dolls, indicating that there is some steganography happening here and there is something inside this image.

Checking with a hex editor we see some hex as the bottom of the file (in ascii) and then the repeating bytes 0xDEADBEEF

![FE06](FE06_1.png)

Using CyberChef to convert from hex and then XOR with DEADBEEF, we reveal "stegception and babushka"

![FE06](FE06_2.png)

Next we attempt to use steghide to extract files from the image. With the password "babushka" we can extract Flag.zip

![FE06](FE06_3.png)

Inside this zip file we see an encrypted flag.txt and can extract it using the other password, "stegeception"

![FE06](FE06_4.png)

Inside this flag file, we see another hex string. However, this one does not use the same XOR encoding as the previous one.

![FE06](FE06_5.png)

Loading it into CyberChef, we can see that the characters are printable and are alphanumeric plus some punctuation. These characters are not valid base 32 or 64. However, they are valid for base 85!

![FE06](FE06_6.png)

After adding From Base-85 to the recipe, we reveal the final flag.

![FE06](FE06_7.png)
