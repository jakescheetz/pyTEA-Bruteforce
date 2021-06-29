---
description: Do I plug the ethernet cable into the monitor to hack it?
---

# Networking

## Intro

One thing to note here: if you don't have networking experience before taking this exam, please really pay attention to this stuff. Although there isn't a lot of "commands" to know per say, almost everything you will learn in this space deals with networking in some way shape or form so it is crucial to have a good idea as to how systems communicate in networks and how they're basically structured. There will be some links to helpful online tools for networking topics you'll need to know. 

![trying to figure out what does what in networks ](../../.gitbook/assets/giphy-1-.gif)

### **route**

```bash
route
```

* identify the gateway for the network you're connected to

```bash
ip route add <x.x.x.0/x> via <y.y.y.y>
```

* add a route manually
* Where x is the currently unreachable IP and y is the IP of the gateway for that network
* calculate subnet for x based on netmask

### ip a & ifconfig

```bash
ip a
```

* can give you the IP address on a specified network interface and the netmask

```bash
ifconfig
```

* deprecated version of _ip a_ but gives the same results

### Online Tools

{% embed url="https://www.aelius.com/njh/subnet\_sheet.html" %}

* used to get the subnet from the identified netmask









