---
description: >-
  In this guide I will simply be sharing how I studied, what I used to prep,
  useful tools to know, important commands to understand, and some areas I
  recommend paying extra attention to
---

# Ultimate eJPT Guide; how to pass the eJPT

### What this guide is and what it isn't

Firstly, it's important to be clear what this guide is and what it is not. There are a lot of "braindumps" out there that you _could_ use. However, that is exactly what this guide is **NOT**. For those of you unfamiliar with what a braindump is- it is basically where someone sits for an exam and then immediately tries to regurgitate the material and answers onto a forum, website, or blog. Not only is this flat out against the purpose of certification exams but if you do this you're only cheating yourself from the knowledge you would have gained from just sitting down and learning the material. With that out of the way, let's get to what this post actually is and how it can help you. This post is meant to highlight things that I felt were particularly helpful or useful when looking back on my eJPT journey. I want everyone to experience that same feeling of accomplishment that I did when I passed my exam: 

![Me \(and hopefully you after you read this blog\) after passing my eJPT](../.gitbook/assets/tenor.gif)

### Background

To give you all some context for my competency level going into the eJPT- I was fairly confident with using linux and with security concepts before the eJPT. I had interned on a Security Incident Response team for two years, passed the security+, and got system owns on a handful of active boxes on HackTheBox. The course that goes along with the exam, PTS from INE, is designed so that an absolute beginner could succeed as well. If you like to be more comfortable than ambitious with cert exams though I would say a combination of the security+, the beginer path on TryHackMe, and the PTS course from INE is plenty to get you comfortable with the required tools. 

### Extra Resources

I will list some extra resources to look through that are by no means required, but could be helpful for someone wanting other places to look: 

For my readers out there: "Penetration Testing A Hands On Introduction to Hacking" by Georgia Weidman is a fantastic read. While some of the things can be outdated and out of the scope of the eJPT, you will learn enough from the book itself to absolutely smash the eJPT

For my video watchers: there aren't a lot of "great" video series to watch for this but John Hammond, IPPSec, and myself :\) fantastically cover HackTheBox walkthroughs for retired boxes on YouTube and those can be good to get you to understand the methodologies of compromising a machine. 

### Big Time Topics

In this section, I am going to present you with topics from the PTS course that are crucial to passing the exam- you may want to pay extra attention to learning these and learning them well. It will pay off! Note: the eJPT exam is _**VERY**_  heavily designed around the PTS course so I recommend that you learn any and all of the material from that and then return to this list for things to brush up on. At that point, you should be familiar with these terms, their meanings, the context, etc. and the list should a great compiled overview. 

#### Networking

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



#### Information Gathering / Enumeration 

This is the most important part of the penetration testing process- read and read well. It is very well put in the course: imagine your target is a dartboard and your attacks are the darts. You would much rather gather more information about the dartboard to make the surface area larger to ensure you cannot miss with your darts \(or attacks\) than have a really small dartboard and waste your time throwing darts trying to hit the target. 

**nslookup**

```bash
nslookup example.com
```

```bash
nslookup 1.2.3.4
```

* nslookup can only be used on the domain of a site
  * ex. google.com works but google.com/blog does not

**nmap**

I recommend creating directories for the results of nmap scans and utilizing the output capabilities to come back to these results later. nmap is extremely powerful in pentests and the results can provide highly valuable information

```bash
mkdir ./nmap
```

nmap \(quick\) 

```bash
nmap -sC -sV x.x.x.x -oN ./nmap/quick
```







