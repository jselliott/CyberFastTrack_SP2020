# BX11
## Binary Exploit (Extreme)

![BX111](BX11.png)

For this challenge, we are given one big hint in the brief where it mentions using the correct **FORMAT**

I didn't take a screen shot at the time but the server responds with:

```
The user object UID=073
Please enter a sevice request:
```

At first, I tried to send different base-encodings and different file formats to see if something different would happen other than an "Invalid service request" message.

Finally, I remembered this blog post about a big Tesla bug bounty and how he started by trying to use format string exploits:

[Cracking my windshield and earning $10,000 on the Tesla Bug Bounty Program](https://samcurry.net/cracking-my-windshield-and-earning-10000-on-the-tesla-bug-bounty-program/)

Here is a good explanation of what is happening if you need a refresher:

[OWASP - Format String Attack](https://owasp.org/www-community/attacks/Format_string_attack)

I started by sending "A%x" and sure enough, it responded with "Unknown format string", so I knew I was getting somwhere.

Next I sent "A%n" and saw the message:

```
Object validated: The 
```

So I sent a payload with more format expressions using python:

```
python -c "print 'A'+'%n'*10" | nc bx11.allyourbases.co 9016
```
and the server responded with:

```
Object validated: The user object UID=073
```

followed by the flag.
