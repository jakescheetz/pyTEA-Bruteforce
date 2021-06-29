---
description: >-
  if we just look at enough Facebook profiles then we'll be able to hack the
  whole planet!!!!
---

# Information Gathering / Enumeration

## **Intro**

This is the most important part of the penetration testing process- read, read again and then read well. It is very well put in the course: imagine your target is a dartboard and your attacks are the darts. You would much rather gather more information about the dartboard to make the surface area larger to ensure you cannot miss with your darts \(or attacks\) than have a really small dartboard and waste your time throwing darts trying to hit the target. The name of the game in enumeration is reading, documenting and covering your bases. If you truly paint as much of a picture of the target as possible you'll naturally lead yourself down the right path!

![we. need. more. enumeration.](../../.gitbook/assets/giphy.gif)



### **nslookup / whois**

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

### **nmap**

I recommend creating a directory for the results of nmap scans and utilizing the output capabilities to come back to these results later. nmap is extremely powerful in pentests and the results can provide highly valuable information

```bash
mkdir ./nmap
```

#### **nmap \(initial\)** 

```bash
nmap -sC -sV -v3 x.x.x.x -oN ./nmap/initial
```

* useful to get a good quick picture of the machine and see if there are any services running on some common ports

#### **nmap \(full\)** 

```bash
nmap -p- -v3 -A x.x.x.x -oN ./nmap/full
```

* useful to see anything that is running on a non-standard port
  * remember you can put any service on any port
  * ex. SSH does not have be running on port 22, it could very well be on port 4444

#### **nmap \(udp\)**

```bash
nmap -p- -sU -sV -sC -v3 x.x.x.x -oN ./nmap/udp
```

* You're also going to want to make sure all of your bases are covered and you can ensure nothing important is open on UDP as well

#### **nmap \(OS detection\)**

```bash
nmap -O -Pn -v3 x.x.x.x -oN ./nmap/os
```

* If you've already performed the other scans, the full scans should try to identify the host OS but sometimes it's worth a shot to just run a dedicated OS identification scan

### **fping**

```bash
fping -a -g x.x.x.0/24 2>/dev/null
```

* performing a ping sweep to identify hosts on the network







