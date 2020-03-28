# IE01
# Network Traffic (Easy)

![Brief](IE01.png)

For this challenge we are provided with a PCAP file which contains some network traffic to analyze. The creators would like us to look around and find the banner of a potentially vulernable service running on the host.

* [RE01.pcap](RE01.pcap)

At first, it just looks like a big jumble of packets and it may be difficult to figure out where to start

![img1](IE01_1.png)

However, the best place to start is probably just by starting with common services (FTP, SSH, etc) and seeing what comes up. In quick filter with "ftp", reveals exactly what we're looking for.

![img2](IE01_2.png)

There is a [CVE (CVE-2013-4730)](https://nvd.nist.gov/vuln/detail/CVE-2013-4730) related to this particular FTP server which allows for remote code execution via a buffer overflow in the USER string.

The flag is the banner message **PCMan's FTP Server 2.0**
