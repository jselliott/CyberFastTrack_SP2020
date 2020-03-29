# WM02
## Web Exploit (Medium)

![WM02](WM02.png)

This challenge displays a new meme every time you relead the page. If you examine it, you see that the memes are being loaded in an iframe which points to:

`http://wm02.allyourbases.co/proxy.php?url=http://127.0.0.1/memes/index.php`

So it's using a proxy script to load a URL that it needs to retrieve, in this case the meme generating script. So we want to direct this script to load something that it shouldn't load, something we don't have access to.

If you check **robots.txt** again, you'll actually see a directory which is hidden from bots and is also password protected. But luckily we have a man on the inside with the proxy script.

We simply have to change the URL on the proxy addrees to access it:

`http://wm02.allyourbases.co/proxy.php?url=http://127.0.0.1/restricted/flag.txt`

(Sorry I don't have a screenshot, but I remember it was something like this)
