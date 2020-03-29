# NH01
## Network (Hard)

![NH01](NH01.png)

For this challenge, we need to find the username that was used to log in. There are a lot of different protocols in this capture, so this is where the Statistics -> Protocol Hierarchy function in Wireshark helps to discover where to focus.


![NH01](NH01_1.png)


Since we're looking specifically for authentication information, LDAP and Kerberos both catch my attention. We can filter the Kerberos packets using "kerberos.CNameString"

Doing this greatly reduces the number of packets we need to look through, and after a short search we see what we're looking for.

![NH01](NH01_2.png)
