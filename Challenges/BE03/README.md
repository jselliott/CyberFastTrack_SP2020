# BE03
## Binary Exploit (Easy)

![BE03](BE03.png)

For this challenge we are given a web service that accepts input with a teaser message that you can't break it or something.

*(Sorry I forgot to screenshot this)*

However, we can test this by passing a whole lot of input to the command and see what happens. If you're not familiar with binary exploits, a really good way to pass input it by using python on your command line, especially if it requires sending untypeable characters.

We can do this by piping our python output into the netcat command:

```
python -c "print 'A'*1000" | nc be03.allyourbases.co 9000
```

This will print out 1000 A's and then send it straight to the server, overflowing the buffer and triggering it to reveal the flag.

